"""Hook do MkDocs: regenera docs/assets/escopo.js antes de cada build, serve ou gh-deploy."""
import hashlib, json, re, subprocess, sys
from pathlib import Path

ABAS = ["req", "reg", "dec", "cron", "alert"]  # mesmas abas de docs/assets/painel.js

def on_pre_build(config):
    root = Path(config["config_file_path"]).resolve().parent
    subprocess.run([sys.executable, str(root / "tools" / "gen_escopo.py"), str(root)], check=True)

def on_page_markdown(markdown, page, config, files):
    """O painel abre itens por #CODIGO via JavaScript; declara essas âncoras para o MkDocs validar os links."""
    if page.file.src_uri != "painel.md":
        return markdown
    js = (Path(config["docs_dir"]) / "assets" / "escopo.js").read_text(encoding="utf-8")
    d = json.loads(js[js.index("{"):js.rindex("}") + 1])
    codigos = [*ABAS, *d["rfs"], *d["rn"], *d["rnf"],
               *(x["id"] for x in d["dec"] + d["pen"] + d["pen_enc"]),
               *("it-" + re.sub(r"\D", "", it["nome"]) for it in d["its"])]
    spans = "".join(f'<span id="{c}"></span>' for c in codigos)
    return markdown + f'\n\n<div hidden>{spans}</div>\n'

def on_post_page(output, page, config):
    """Acrescenta ?v=<hash do conteúdo> aos arquivos do painel, para o navegador não usar uma cópia antiga em cache."""
    assets = Path(config["docs_dir"]) / "assets"
    def versao(m):
        arq = assets / m[2]
        return m[0] if not arq.exists() else f'{m[1]}{m[2]}?v={hashlib.md5(arq.read_bytes()).hexdigest()[:8]}"'
    return re.sub(r'((?:src|href)="[^"]*assets/)(escopo\.js|painel\.js|painel\.css)"', versao, output)
