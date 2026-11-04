"""Gera docs/assets/escopo.js a partir das fichas, decisões, regras, RNFs e cronograma.
Uso: python tools/gen_escopo.py [raiz-do-repo]   (rode no CI ou antes do mkdocs build)"""
import re, json, sys
from pathlib import Path
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
E = ROOT / "docs/visao/escopo"

def clean(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<a [^>]*></a>|\*\*|\{[^}]*\}", "", s)
    return re.sub(r"\s*<br>\s*", "\n", s).strip()
def rows(txt):
    return [[c.strip() for c in l.strip().strip("|").split("|")]
            for l in txt.splitlines() if l.startswith("|") and not re.match(r"\|\s*:?-", l)]
def ids(s, p): return list(dict.fromkeys(re.findall(p + r"\d+", s)))

rn = {clean(r[0]): clean(r[1]) for r in rows((E/"regras_de_negocio.md").read_text()) if re.match(r"(<a [^>]*></a>)?\*\*RN\d+", r[0])}
rnf = {}
for f in sorted((E/"rnf").glob("RNF*.md")):
    t = f.read_text(); d = {clean(r[0]): clean(r[1]) for r in rows(t) if len(r) == 2}
    rnf[f.stem] = {"nome": re.match(r"### RNF\d+: (.*)", t)[1], "desc": d.get("Descrição", ""), "crit": d.get("Critério de aceitação", "")}

dec_txt, pen_txt = (E/"decisoes.md").read_text().split("## Pendências", 1)
pen_txt, enc_txt = (pen_txt.split("## Pendências encerradas") + [""])[:2]
dec = [{"id": r[0], "data": clean(r[1]), "texto": clean(r[2]), "rfs": ids(r[3], "RF"), "fonte": clean(r[4])}
       for r in rows(dec_txt) if re.match(r"DEC\d+", r[0])]
pen = [{"id": r[0], "texto": clean(r[1]), "rfs": ids(r[2], "RF"), "acao": clean(r[3])}
       for r in rows(pen_txt) if re.match(r"PEN\d+", r[0])]

pen_enc = [{"id": r[0], "texto": clean(r[1]), "rfs": ids(r[2], "RF"), "acao": clean(r[3])}
           for r in rows(enc_txt) if re.match(r"PEN\d+", r[0])]

its = []
for r in rows((ROOT/"docs/cronograma/6_cronograma.md").read_text()):
    if r[0].startswith("**Itera"):
        nome, _, per = clean(r[0]).partition("\n")
        its.append({"nome": nome, "periodo": per, "foco": clean(r[1]), "entregas": clean(r[2]), "rfs": ids(r[4], "RF")})

cron_nota = " ".join(clean(l).lstrip("> ").strip() for l in (ROOT/"docs/cronograma/6_cronograma.md").read_text().splitlines() if l.startswith("**Critério de transição") or l.startswith("> O cronograma"))

rfs = {}
for f in sorted((E/"requisitos").glob("RF*.md")):
    t = f.read_text(); d = {clean(r[0]): r[1] for r in rows(t.split("#### Andamento")[0]) if len(r) == 2}
    and_ = t.split("#### Andamento")[1].split("####")[0] if "#### Andamento" in t else ""
    mo = d.get("Valor de negócio (MoSCoW)", "")
    rfs[f.stem] = {"nome": re.match(r"### RF\d+: (.*)", t)[1], "estado": d["Estado e versão"].split(",")[0],
        "cp": re.split(r" \(ver", clean(d["CP de origem"]))[0], "ator": clean(d.get("Ator principal", "")),
        "declaracao": clean(d.get("Declaração", "")), "entradas": clean(d.get("Entradas", "")), "pre": clean(d.get("Pré-condições", "")), "proc": clean(d.get("Processamento", "")), "saidas": clean(d.get("Saídas", "")), "pdf": (E/"pdf"/f"{f.stem}.pdf").exists(), "pendente": t.count("[PENDENTE]"), "moscow": mo.split("·")[0].strip(),
        "entrega": "Pós-MVP" if "Pós-MVP" in mo else "MVP", "criterios": clean(d.get("Critérios de aceitação", "")).split("\n"),
        "rns": ids(d.get("Regras de negócio", ""), "RN"), "rnfs": ids(d.get("RNFs aplicáveis", ""), "RNF"),
        "andamento": [[clean(r[0]), clean(r[1])] for r in rows(and_) if r[0] != "Etapa"],
        "decs": [x["id"] for x in dec if f.stem in x["rfs"]], "pens": [x["id"] for x in pen if f.stem in x["rfs"]],
        "its": [i["nome"] for i in its if f.stem in i["rfs"]]}

for k, r in rfs.items():
    r["lacunas"] = ([f"{r['pendente']} campo(s) marcado(s) como pendente na ficha"] if r["pendente"] else []) \
        + [p + ": " + next(x["texto"] for x in pen if x["id"] == p) for p in r["pens"]] \
        + (["Ficha ainda em rascunho"] if r["estado"] == "Rascunho" and r["entrega"] == "MVP" else [])

alertas = []
for f in sorted(rfs):
    for n in rfs[f]["rns"]:
        if n not in rn: alertas.append({"tipo": "Regra inexistente", "texto": f"{f} cita {n}, que não está em regras de negócio", "rf": f})
for x in dec + pen:
    for n in ids(x["texto"], "RN"):
        if n not in rn: alertas.append({"tipo": "Regra inexistente", "texto": f"{x['id']} cita {n}, que não está em regras de negócio"})
for f, r in rfs.items():
    if r["entrega"] == "MVP" and not r["its"]: alertas.append({"tipo": "Sem iteração", "texto": f"{f} está no MVP e em nenhuma iteração do cronograma", "rf": f})
    if r["entrega"] != "MVP" and r["its"]: alertas.append({"tipo": "Pós-MVP agendado", "texto": f"{f} é pós-MVP mas aparece em {', '.join(r['its'])}", "rf": f})
for x in dec:
    if "confirmar" in (x["data"] + x["fonte"]).lower(): alertas.append({"tipo": "Decisão sem fonte ou data", "texto": f"{x['id']} ainda precisa de data ou fonte"})

out = {
    "rfs": rfs,
    "rn": rn,
    "rnf": rnf,
    "dec": dec,
    "pen": pen,
    "pen_enc": pen_enc,
    "its": its,
    "cron_nota": cron_nota,
    "alertas": alertas
}

dest = ROOT / "docs/assets/escopo.js"
dest.parent.mkdir(parents=True, exist_ok=True)

novo = (
    "window.ESCOPO = "
    + json.dumps(
        out,
        ensure_ascii=False,
        indent=2
    )
    + ";\n"
)

if not dest.exists() or dest.read_text(encoding="utf-8") != novo:
    dest.write_text(novo, encoding="utf-8")

print(
    f"{len(rfs)} RFs, "
    f"{len(dec)} decisões, "
    f"{len(pen)} pendências, "
    f"{len(its)} iterações, "
    f"{len(alertas)} alertas"
)