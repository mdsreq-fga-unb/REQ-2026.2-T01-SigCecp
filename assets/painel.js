/* Painel do escopo
 *
 * Lê window.ESCOPO (gerado por tools/gen_escopo.py) e desenha:
 *   - o resumo da Home (#painel-resumo);
 *   - o painel completo (#painel): abas, filtros e ficha lateral.
 *
 * Organização do arquivo:
 *   1. Dados e estado
 *   2. Utilidades de DOM e de URL
 *   3. Cálculos (progresso do MVP, iteração atual)
 *   4. Resumo da Home
 *   5. Painel: estrutura (topo, abas, rodapé)
 *   6. Painel: abas (requisitos, regras, decisões, cronograma, alertas)
 *   7. Ficha lateral do requisito
 *   8. Navegação (hash da URL)
 *   9. Inicialização
 */
(function () {
  'use strict';

  /* ================= 1. Dados e estado ================= */

  const D = window.ESCOPO;
  if (!D) return;

  const RF = D.rfs;
  const root = document.getElementById('painel');
  const resumo = document.getElementById('painel-resumo');

  const ABAS = [
    ['req', 'Requisitos'],
    ['reg', 'Regras e RNFs'],
    ['dec', 'Decisões e pendências'],
    ['cron', 'Cronograma'],
    ['alert', 'Alertas (' + D.alertas.length + ')'],
  ];

  const filtros = { q: '', cp: '', estado: '', entrega: '', pend: '' };
  let abaAtual = 'req';
  let focoAnterior = null; // elemento que tinha o foco antes de abrir a ficha

  /* ================= 2. Utilidades de DOM e de URL ================= */

  const esc = (s) =>
    String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  function el(tag, classe, html) {
    const e = document.createElement(tag);
    if (classe) e.className = classe;
    if (html != null) e.innerHTML = html;
    return e;
  }

  // Marca [PENDENTE] nos textos das fichas
  const marcarPendente = (s) => esc(s).replace(/\[PENDENTE\]/g, '<mark>PENDENTE</mark>');

  // URLs relativas: o MkDocs serve /painel/ (diretório) ou painel.html
  const usaDiretorio = location.pathname.endsWith('/');
  const prefixo = usaDiretorio ? '../' : '';
  const urlFicha = (cod) => prefixo + 'visao/escopo/requisitos/' + cod + (usaDiretorio ? '/' : '.html');
  const urlPdf = (cod) => prefixo + 'visao/escopo/pdf/' + cod + '.pdf';
  const urlFonte = (md) => prefixo + md.replace(/\.md$/, usaDiretorio ? '/' : '.html');

  // Botão em forma de pílula, usado para ligar um item a outro
  function chip(texto, classe, aoClicar, dica) {
    const b = el('button', 'pn-chip ' + (classe || ''), esc(texto));
    b.type = 'button';
    if (dica) b.title = dica;
    b.onclick = aoClicar;
    return b;
  }

  const chipRF = (cod) => chip(cod, RF[cod]?.estado, () => abrirFicha(cod), RF[cod]?.nome);

  function acrescentarChipsRF(destino, codigos) {
    codigos.forEach((c) => destino.append(chipRF(c)));
  }

  // Cartão simples usado nas abas de regras, decisões, cronograma e alertas
  function cartao(id, html, classe) {
    const c = el('div', 'pn-card' + (classe ? ' ' + classe : ''), html);
    if (id) c.id = id;
    return c;
  }

  /* ================= 3. Cálculos ================= */

  const etapaFeita = (etapa) => etapa[1].startsWith('Feito');

  function progressoMvp() {
    const mvp = Object.values(RF).filter((r) => r.entrega === 'MVP');
    return {
      total: mvp.reduce((s, r) => s + r.andamento.length, 0),
      feitas: mvp.reduce((s, r) => s + r.andamento.filter(etapaFeita).length, 0),
    };
  }

  function barraProgresso(estilo) {
    const p = progressoMvp();
    return '<progress max="' + p.total + '" value="' + p.feitas + '"' + (estilo ? ' style="' + estilo + '"' : '') +
      '></progress> MVP: ' + p.feitas + ' de ' + p.total + ' etapas concluídas';
  }

  // "19/10/2026 - 25/10/2026" -> { inicio, fim } (fim exclusivo)
  function intervalo(periodo) {
    const m = periodo.match(/(\d+)\/(\d+)\/(\d+) - (\d+)\/(\d+)\/(\d+)/);
    if (!m) return null;
    return { inicio: new Date(m[3], m[2] - 1, m[1]), fim: new Date(m[6], m[5] - 1, +m[4] + 1) };
  }

  function emAndamento(it) {
    const i = intervalo(it.periodo);
    const agora = new Date();
    return !!i && agora >= i.inicio && agora < i.fim;
  }

  const idIteracao = (nome) => 'it-' + nome.replace(/\D/g, '');

  const comPendencias = () => Object.values(RF).filter((r) => r.lacunas.length).length;

  /* ================= 4. Resumo da Home ================= */

  function renderResumo(alvo) {
    const it = D.its.find(emAndamento);
    alvo.innerHTML =
      '<p><b id="pr-a"></b> <span id="pr-b"></span></p>' +
      '<p>' + barraProgresso('accent-color:#c1121f') + '. ' + comPendencias() +
      ' requisitos com pendências e ' + D.alertas.length +
      ' alertas no <a href="painel/">painel do escopo</a>.</p>';
    // textContent: o texto vem das fontes e não deve ser interpretado como HTML
    alvo.querySelector('#pr-a').textContent = it ? it.nome + ' (' + it.periodo + ')' : 'Fora do cronograma';
    alvo.querySelector('#pr-b').textContent = it ? it.foco.replace(/\s+/g, ' ').slice(0, 240) : '';
  }

  /* ================= 5. Painel: estrutura ================= */

  function render() {
    root.innerHTML = '';
    root.append(criarTopo(), criarAbas(), VIEWS[abaAtual](), criarRodape());
  }

  function criarTopo() {
    const reqs = Object.values(RF);
    const contadores = [
      [reqs.length, 'requisitos'],
      [reqs.filter((r) => r.entrega === 'MVP').length, 'no MVP'],
      [reqs.filter((r) => r.estado === 'Detalhado' || r.estado === 'Validado').length, 'detalhados'],
      [comPendencias(), 'com pendências'],
    ];
    const topo = el('div', 'pn-top');
    contadores.forEach(([n, rotulo]) => topo.append(el('span', '', '<b>' + n + '</b>' + rotulo)));
    topo.append(el('span', '', barraProgresso()));
    return topo;
  }

  function criarAbas() {
    const barra = el('div', 'pn-tabs');
    barra.setAttribute('role', 'tablist');
    ABAS.forEach(([id, rotulo]) => {
      const b = el('button', '', esc(rotulo));
      b.setAttribute('role', 'tab');
      b.setAttribute('aria-selected', id === abaAtual);
      b.onclick = () => { abaAtual = id; render(); };
      barra.append(b);
    });
    return barra;
  }

  function criarRodape() {
    return el('p', 'pn-vazio pn-fonte',
      'Este painel é gerado das fichas dos requisitos, das <a href="' + urlFonte('visao/escopo/regras_de_negocio.md') +
      '">regras de negócio</a>, das <a href="' + urlFonte('visao/escopo/decisoes.md') +
      '">decisões</a> e do <a href="' + urlFonte('cronograma/6_cronograma.md') +
      '">cronograma</a>. Para mudar algo, edite a fonte.');
  }

  // Vai para uma aba e, se informado, rola até o item
  function ir(aba, idItem) {
    fecharFicha();
    abaAtual = aba;
    render();
    if (idItem) document.getElementById(idItem)?.scrollIntoView({ block: 'start' });
  }

  /* ================= 6. Painel: abas ================= */

  /* ---- Requisitos: busca, filtros e lista agrupada por CP ---- */
  function viewRequisitos() {
    const caixa = el('div');
    const barra = el('div', 'pn-filtros');
    const lista = el('div');

    const busca = el('input');
    busca.type = 'search';
    busca.placeholder = 'Buscar por código, nome ou texto';
    busca.value = filtros.q;
    busca.setAttribute('aria-label', 'Buscar requisito');
    busca.oninput = () => { filtros.q = busca.value; desenhar(); };

    const valores = (campo) => [...new Set(Object.values(RF).map((r) => r[campo]))];
    function seletor(chave, rotulo, opcoes) {
      const s = el('select', '', '<option value="">' + rotulo + '</option>' +
        opcoes.map((o) => '<option' + (filtros[chave] === o ? ' selected' : '') + '>' + esc(o) + '</option>').join(''));
      s.setAttribute('aria-label', rotulo);
      s.onchange = () => { filtros[chave] = s.value; desenhar(); };
      return s;
    }
    barra.append(
      busca,
      seletor('cp', 'Todos os CPs', valores('cp')),
      seletor('estado', 'Todos os estados', valores('estado')),
      seletor('entrega', 'MVP e pós-MVP', valores('entrega')),
      seletor('pend', 'Pendências', ['Com pendências'])
    );

    function passaNosFiltros(cod, r) {
      if (filtros.cp && r.cp !== filtros.cp) return false;
      if (filtros.estado && r.estado !== filtros.estado) return false;
      if (filtros.entrega && r.entrega !== filtros.entrega) return false;
      if (filtros.pend && !r.lacunas.length) return false;
      if (filtros.q && !(cod + r.nome + r.declaracao).toLowerCase().includes(filtros.q.toLowerCase())) return false;
      return true;
    }

    function linhaRequisito(cod, r) {
      const pendencias = r.lacunas.length ? ' <small class="pn-pend">' + r.lacunas.length + ' pendência(s)</small>' : '';
      const b = el('button', 'pn-row',
        '<b>' + cod + '</b>' +
        '<span>' + esc(r.nome) + '<br>' + miniAndamento(r) + pendencias + '</span>' +
        '<span class="pn-b ' + r.estado + '">' + r.estado + '</span>' +
        '<span class="pn-b ' + (r.entrega === 'MVP' ? 'mvp' : '') + '">' + r.entrega + '</span>');
      b.onclick = () => abrirFicha(cod);
      return b;
    }

    function desenhar() {
      lista.innerHTML = '';
      let cpAnterior = '';
      let exibidos = 0;
      Object.entries(RF).forEach(([cod, r]) => {
        if (!passaNosFiltros(cod, r)) return;
        if (r.cp !== cpAnterior) { lista.append(el('h3', '', esc(r.cp))); cpAnterior = r.cp; }
        lista.append(linhaRequisito(cod, r));
        exibidos++;
      });
      if (!exibidos) lista.append(el('p', 'pn-vazio', 'Nenhum requisito encontrado. Limpe a busca ou os filtros.'));
    }

    desenhar();
    caixa.append(barra, lista);
    return caixa;
  }

  // Cinco segmentos, um por etapa do andamento
  const miniAndamento = (r) =>
    '<span class="pn-pr" title="Detalhamento, protótipo, início, implementação, aceite">' +
    r.andamento.map((a) => '<i class="' + a[1].split(' ')[0] + '"></i>').join('') + '</span>';

  /* ---- Regras de negócio e RNFs ---- */
  function viewRegras() {
    const caixa = el('div');
    const usadoPor = (campo, cod) =>
      Object.entries(RF).filter(([, r]) => r[campo].includes(cod)).map(([c]) => c);

    caixa.append(el('h3', '', 'Regras de negócio'));
    Object.entries(D.rn).forEach(([cod, texto]) => {
      const c = cartao('rn-' + cod, '<h4>' + cod + '</h4><p>' + esc(texto) + '</p>');
      acrescentarChipsRF(c, usadoPor('rns', cod));
      caixa.append(c);
    });

    caixa.append(el('h3', '', 'Requisitos não funcionais'));
    Object.entries(D.rnf).forEach(([cod, x]) => {
      const c = cartao('rnf-' + cod,
        '<h4>' + cod + ': ' + esc(x.nome) + '</h4><p>' + esc(x.desc) + '</p>' +
        (x.crit ? '<p><small>Critério: ' + esc(x.crit) + '</small></p>' : ''));
      acrescentarChipsRF(c, usadoPor('rnfs', cod));
      caixa.append(c);
    });
    return caixa;
  }

  /* ---- Decisões, pendências abertas e encerradas ---- */
  function viewDecisoes() {
    const caixa = el('div');

    caixa.append(el('h3', '', 'Decisões'));
    D.dec.forEach((d) => {
      const c = cartao('dec-' + d.id,
        '<h4>' + d.id + ' <small>' + esc(d.data) + '</small></h4><p>' + esc(d.texto) + '</p>' +
        '<p><small>Fonte: ' + esc(d.fonte) + '</small></p>');
      acrescentarChipsRF(c, d.rfs);
      caixa.append(c);
    });

    caixa.append(el('h3', '', 'Pendências'));
    D.pen.forEach((d) => {
      const c = cartao('pen-' + d.id,
        '<h4>' + d.id + '</h4><p>' + esc(d.texto) + '</p><p><small>Próximo passo: ' + esc(d.acao) + '</small></p>');
      acrescentarChipsRF(c, d.rfs);
      caixa.append(c);
    });

    if (D.pen_enc?.length) {
      caixa.append(el('h3', '', 'Pendências encerradas'));
      D.pen_enc.forEach((d) => caixa.append(cartao(null,
        '<h4>' + d.id + '</h4><p>' + esc(d.texto) + '</p><p><small>Como foi encerrada: ' + esc(d.acao) + '</small></p>')));
    }
    return caixa;
  }

  /* ---- Cronograma ---- */
  function viewCronograma() {
    const caixa = el('div');
    if (D.cron_nota) caixa.append(el('p', 'pn-vazio', esc(D.cron_nota)));
    D.its.forEach((it) => {
      const atual = emAndamento(it);
      const c = cartao(idIteracao(it.nome),
        '<h4>' + esc(it.nome) + (atual ? ' <span class="pn-b mvp">em andamento</span>' : '') + '</h4>' +
        '<small>' + esc(it.periodo) + '</small><p>' + esc(it.foco) + '</p>' +
        (it.entregas ? '<p><b>Entrega:</b> ' + esc(it.entregas) + '</p>' : ''),
        atual ? 'hoje' : '');
      acrescentarChipsRF(c, it.rfs);
      caixa.append(c);
    });
    return caixa;
  }

  /* ---- Alertas de consistência ---- */
  function viewAlertas() {
    if (!D.alertas.length) return el('p', 'pn-vazio', 'Nenhuma inconsistência encontrada.');
    const caixa = el('div');
    caixa.append(el('p', 'pn-vazio', 'Gerados automaticamente a cada build. Corrija na fonte (ficha, decisões ou cronograma) e o alerta some.'));
    D.alertas.forEach((a) => {
      const c = cartao(null, '<h4>' + esc(a.tipo) + '</h4><p>' + esc(a.texto) + '</p>');
      if (a.rf) c.append(chipRF(a.rf));
      caixa.append(c);
    });
    return caixa;
  }

  const VIEWS = { req: viewRequisitos, reg: viewRegras, dec: viewDecisoes, cron: viewCronograma, alert: viewAlertas };

  /* ================= 7. Ficha lateral do requisito ================= */

  const badge = (texto, classe) => '<span class="pn-b ' + (classe || '') + '">' + texto + '</span>';
  const secao = (titulo, corpo) => '<h5>' + titulo + '</h5>' + corpo;
  const vazio = (texto) => '<p class="pn-vazio">' + texto + '</p>';

  function htmlCabecalho(cod, r) {
    return '<button class="pn-x" aria-label="Fechar">×</button>' +
      '<h2>' + cod + ': ' + esc(r.nome) + '</h2>' +
      badge(r.estado, r.estado) + ' ' + badge(r.entrega, r.entrega === 'MVP' ? 'mvp' : '') + ' ' + badge(esc(r.moscow)) +
      '<p>' + esc(r.declaracao) + '</p>' +
      '<small>' + esc(r.cp) + '. Ator: ' + esc(r.ator) + '</small>';
  }

  const htmlFalta = (r) => !r.lacunas.length ? '' :
    '<div class="pn-al"><b>O que falta</b><ul>' + r.lacunas.map((x) => '<li>' + esc(x) + '</li>').join('') + '</ul></div>';

  function htmlParaImplementar(r) {
    const campos = [['Entradas', r.entradas], ['Pré-condições', r.pre], ['Processamento', r.proc], ['Saídas', r.saidas]];
    return secao('Para implementar',
      '<dl>' + campos.map(([nome, texto]) => '<dt>' + nome + '</dt><dd>' + marcarPendente(texto) + '</dd>').join('') + '</dl>');
  }

  const htmlAndamento = (r) => secao('Andamento',
    '<ol class="pn-st">' + r.andamento.map(([etapa, status]) =>
      '<li class="' + status.split(' ')[0] + '"><b>' + esc(etapa) + '</b><br>' + esc(status) + '</li>').join('') + '</ol>');

  const htmlCriterios = (r) => secao('Critérios de aceitação',
    '<ol>' + r.criterios.map((c) => '<li>' + esc(c.replace(/^\d+\.\s*/, '')) + '</li>').join('') + '</ol>');

  // Os códigos RN/RNF levam à aba de regras (ver o clique delegado em abrirFicha)
  const htmlRegras = (r) => secao('Regras de negócio', !r.rns.length ? vazio('Nenhuma regra vinculada.') :
    '<ul>' + r.rns.map((n) => '<li><b class="pn-ln" data-go="reg|rn-' + n + '">' + n + '</b> ' +
      esc(D.rn[n] || 'regra não encontrada') + '</li>').join('') + '</ul>');

  const htmlRnfs = (r) => secao('Requisitos não funcionais', !r.rnfs.length ? vazio('Nenhum vinculado.') :
    '<ul>' + r.rnfs.map((n) => '<li><b class="pn-ln" data-go="reg|rnf-' + n + '">' + n + '</b> ' +
      esc(D.rnf[n]?.nome || '') + '<br><small>' + esc(D.rnf[n]?.crit || '') + '</small></li>').join('') + '</ul>');

  // Decisões, pendências e iteração ligadas ao requisito
  function blocoRelacionados(r) {
    const bloco = el('div');

    bloco.append(el('h5', '', 'Decisões'));
    r.decs.forEach((id) => bloco.append(
      chip(id, '', () => ir('dec', 'dec-' + id), (D.dec.find((d) => d.id === id) || {}).texto)));
    if (!r.decs.length) bloco.append(el('span', 'pn-vazio', 'Nenhuma decisão registrada.'));

    if (r.pens.length) {
      bloco.append(el('h5', '', 'Pendências'));
      r.pens.forEach((id) => bloco.append(chip(id, '', () => ir('dec', 'pen-' + id))));
    }

    bloco.append(el('h5', '', 'Iteração'));
    r.its.forEach((nome) => bloco.append(chip(nome, '', () => ir('cron', idIteracao(nome)))));
    if (!r.its.length) bloco.append(el('span', 'pn-vazio', 'Fora do cronograma atual.'));
    return bloco;
  }

  function linksDaFicha(cod, r) {
    const p = el('p', '', '<a href="' + urlFicha(cod) + '">Abrir ficha completa</a>' +
      (r.pdf ? ' &nbsp; <a href="' + urlPdf(cod) + '">Ver protótipo (PDF)</a>' : ''));
    p.style.marginTop = '1.2rem';
    return p;
  }

  const removerFicha = () => document.querySelectorAll('.pn-ov,.pn-dr').forEach((e) => e.remove());

  function fecharFicha() {
    removerFicha();
    focoAnterior?.focus?.();
    focoAnterior = null;
  }

  function abrirFicha(cod) {
    const r = RF[cod];
    focoAnterior = document.activeElement;
    removerFicha();

    const fundo = el('div', 'pn-ov');
    fundo.onclick = fecharFicha;

    const gaveta = el('aside', 'pn-dr');
    gaveta.setAttribute('role', 'dialog');
    gaveta.setAttribute('aria-label', cod + ' ' + r.nome);
    gaveta.innerHTML = htmlCabecalho(cod, r) + htmlFalta(r) + htmlParaImplementar(r) + htmlAndamento(r) +
      htmlCriterios(r) + htmlRegras(r) + htmlRnfs(r);
    gaveta.append(blocoRelacionados(r), linksDaFicha(cod, r));

    // Clique em elementos com data-go="aba|id" leva ao item correspondente
    gaveta.onclick = (e) => {
      const alvo = e.target.closest('[data-go]');
      if (!alvo) return;
      const [aba, id] = alvo.dataset.go.split('|');
      ir(aba, id);
    };
    const fechar = gaveta.querySelector('.pn-x');
    fechar.onclick = fecharFicha;

    document.body.append(fundo, gaveta);
    fechar.focus();
    history.replaceState(null, '', '#' + cod); // permite compartilhar o link da ficha
  }

  /* ================= 8. Navegação (hash da URL) ================= */

  // Códigos aceitos em #CODIGO e a aba/prefixo de id que cada um abre
  const ROTAS = [
    [/^RNF\d+$/, 'reg', 'rnf-'],
    [/^RN\d+$/, 'reg', 'rn-'],
    [/^DEC\d+$/, 'dec', 'dec-'],
    [/^PEN\d+$/, 'dec', 'pen-'],
    [/^it-\d+$/, 'cron', ''],
  ];

  function rotear() {
    const h = decodeURIComponent(location.hash.slice(1));
    if (RF[h]) { abaAtual = 'req'; render(); abrirFicha(h); return; }
    const rota = ROTAS.find(([regex]) => regex.test(h));
    if (rota) { ir(rota[1], rota[2] + h); return; }
    if (ABAS.some(([id]) => id === h)) { abaAtual = h; render(); }
  }

  /* ================= 9. Inicialização ================= */

  if (resumo) renderResumo(resumo);

  if (root) {
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') fecharFicha(); });
    render();
    rotear();
    addEventListener('hashchange', rotear);
  }
})();