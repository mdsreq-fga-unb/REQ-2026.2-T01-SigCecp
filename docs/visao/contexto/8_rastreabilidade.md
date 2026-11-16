# 8 Rastreabilidade

Esta é a versão vigente da matriz-síntese e do grafo de rastreabilidade do CECP. A versão original, de 05/09/2026, está nos [documentos arquivados](../../historico/arquivo.md) e não é mais atualizada.

Os vínculos de cada requisito com regras de negócio, RNFs, decisões e pendências estão nas fichas e no [painel do escopo](../../painel.md); esta página mostra a cadeia completa, do objetivo até o RNF. Quando a ficha de um RF muda, a matriz abaixo é atualizada junto.

## 8.1 Matriz-síntese de rastreabilidade

A matriz apresenta a rastreabilidade entre os Objetivos Específicos (OE), as Características do Produto (CP), os Requisitos Funcionais (RF) e os Requisitos Não Funcionais (RNF), conforme a [tabela 2.3](2_solucao_proposta.md#23-caracteristicas-de-produto-mapeadas-com-os-objetivos-especificos-do-produto) e o campo *RNFs aplicáveis* de cada ficha. RF36, RF37 e RF40 foram incorporados ao RF35 ([DEC16](../../painel.md#DEC16)), e RNF04 e RNF05 foram retirados ([DEC17](../../painel.md#DEC17)).

```
OE1
 ├- CP4
 │    ├- RF21 - RNF01, RNF03, RNF11, RNF12, RNF13
 │    ├- RF22 - RNF03, RNF06, RNF10, RNF11, RNF12, RNF13
 │    ├- RF23 - RNF01, RNF06, RNF11, RNF13
 │    ├- RF24 - RNF03, RNF10, RNF11, RNF13
 │    └- RF25 - RNF03, RNF10, RNF11, RNF13
 │
 ├- CP1
 │    ├- RF06 - RNF03, RNF06, RNF11
 │    └- RF07 - RNF01, RNF06, RNF11
 │
 └- CP7
      ├- RF35 - RNF01, RNF02, RNF03, RNF09, RNF13
      ├- RF38 - RNF03, RNF10, RNF13
      ├- RF39 - RNF03, RNF10, RNF13
      ├- RF41 - RNF03, RNF06
      └- RF42 - RNF03, RNF10, RNF11, RNF13


OE2
 ├- CP1
 │    ├- RF03 - RNF01, RNF03, RNF06, RNF11
 │    ├- RF04 - RNF03, RNF06, RNF10, RNF11
 │    └- RF05 - RNF03, RNF10, RNF11
 │
 └- CP5
      ├- RF26 - RNF01, RNF03, RNF06, RNF11, RNF13
      ├- RF27 - RNF01, RNF06, RNF11, RNF13
      └- RF28 - RNF03, RNF06, RNF11, RNF13


OE3
 └- CP5
      └- RF29 - RNF03, RNF10, RNF11, RNF13


OE4
 ├- CP3
 │    ├- RF13 - RNF01, RNF02, RNF07, RNF09
 │    ├- RF14 - RNF01, RNF02, RNF07, RNF09, RNF10
 │    ├- RF15 - RNF02, RNF07, RNF09
 │    ├- RF16 - RNF02, RNF07, RNF09, RNF10
 │    ├- RF17 - RNF01, RNF02, RNF07, RNF09
 │    ├- RF18 - RNF01, RNF02, RNF07, RNF09, RNF10
 │    ├- RF19 - RNF02, RNF07, RNF09, RNF10
 │    └- RF20 - RNF02, RNF07, RNF09
 │
 └- CP6
      ├- RF30 - RNF01, RNF03, RNF11, RNF13
      ├- RF31 - RNF01, RNF06, RNF11, RNF13
      ├- RF32 - RNF03, RNF11, RNF13
      ├- RF33 - RNF03, RNF11, RNF13
      └- RF34 - RNF01, RNF06, RNF10, RNF11, RNF13


OE5
 └- CP2
      ├- RF08 - RNF03, RNF10, RNF11, RNF13
      ├- RF09 - RNF03, RNF06, RNF10, RNF11, RNF13
      ├- RF10 - RNF03, RNF10, RNF11, RNF13
      ├- RF11 - RNF03, RNF06, RNF10, RNF11, RNF13
      └- RF12 - RNF06, RNF11, RNF13


Transversal
 └- Acesso
      ├- RF01 - RNF11, RNF12, RNF13
      ├- RF02 - RNF11, RNF13, RNF08
      └- RF00 - RNF11, RNF13
```

## 8.2 Grafo de rastreabilidade

O grafo abaixo representa a cadeia de rastreabilidade do CECP — do problema central até cada Requisito Funcional — com a situação de cada item por cor, conforme o *Andamento* das fichas em 15/11/2026. Passe o mouse em um nó para ver a descrição.

<div style="position:relative;width:100%;font-family:sans-serif;user-select:none;">
  <div style="display:flex;align-items:center;gap:6px;padding:8px 10px;background:rgba(128,128,128,0.08);border:1px solid rgba(128,128,128,0.2);border-bottom:none;border-radius:8px 8px 0 0;">
    <button id="tz-in" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">+</button>
    <button id="tz-out" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">−</button>
    <button id="tz-reset" style="height:28px;padding:0 10px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:12px;">↺ Reset</button>
    <span style="font-size:11px;opacity:0.5;margin-left:4px;">Scroll para zoom · Arraste para mover · Passe o mouse nos nós para detalhes ·</span>
  </div>
  <div id="tz-wrap" style="width:100%;height:640px;overflow:hidden;border:1px solid rgba(128,128,128,0.2);border-radius:0 0 8px 8px;cursor:grab;box-sizing:border-box;">
    <svg id="tz-svg" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:100%;"></svg>
  </div>
  <div id="tz-tip" style="position:absolute;background:#222;color:#fff;padding:7px 11px;border-radius:6px;font-size:13px;pointer-events:none;display:none;max-width:340px;z-index:200;line-height:1.5;box-shadow:0 2px 8px rgba(0,0,0,0.4);"></div>
</div>

<script>
(function(){
  var R=23, PAD=42, SP=52, GRP_GAP=78, OE_MIN=54, H=600;
  var LY=[55,175,300,430];

  var CP_RF={
    CP1:['RF03','RF04','RF05','RF06','RF07'],
    CP2:['RF08','RF09','RF10','RF11','RF12'],
    CP3:['RF13','RF14','RF15','RF16','RF17','RF18','RF19','RF20'],
    CP4:['RF21','RF22','RF23','RF24','RF25'],
    CP5:['RF26','RF27','RF28','RF29'],
    CP6:['RF30','RF31','RF32','RF33', 'RF34'],
    CP7:['RF35','RF38','RF39','RF41','RF42'],
    ACESSO:['RF01','RF02','RF00']
  };
  var OE_CP={
    OE1:['CP1','CP4','CP7'],
    OE2:['CP1','CP5'],
    OE3:['CP1','CP5'],
    OE4:['CP3','CP6'],
    OE5:['CP2','CP3'],
    TRANSV:['ACESSO']
  };
  var CP_ORDER=['CP1','CP2','CP3','CP4','CP5','CP6','CP7','ACESSO'];
  var OE_ORDER=['OE1','OE2','OE3','OE4','OE5','TRANSV'];

  var EDGES=[
    ['PROB','OG'],
    ['OG','OE1'],['OG','OE2'],['OG','OE3'],['OG','OE4'],['OG','OE5'],['OG','TRANSV'],
    ['OE1','CP1'],['OE1','CP4'],['OE1','CP7'],
    ['OE2','CP1'],['OE2','CP5'],
    ['OE3','CP1'],['OE3','CP5'],
    ['OE4','CP3'],['OE4','CP6'],
    ['OE5','CP2'],['OE5','CP3'],
    ['TRANSV','ACESSO'],
    ['CP1','RF03'],['CP1','RF04'],['CP1','RF05'],['CP1','RF06'],['CP1','RF07'],
    ['CP2','RF08'],['CP2','RF09'],['CP2','RF10'],['CP2','RF11'],['CP2','RF12'],
    ['CP3','RF13'],['CP3','RF14'],['CP3','RF15'],['CP3','RF16'],['CP3','RF17'],['CP3','RF18'],['CP3','RF19'],['CP3','RF20'],
    ['CP4','RF21'],['CP4','RF22'],['CP4','RF23'],['CP4','RF24'],['CP4','RF25'],
    ['CP5','RF26'],['CP5','RF27'],['CP5','RF28'],['CP5','RF29'],
    ['CP6','RF30'],['CP6','RF31'],['CP6','RF32'],['CP6','RF33'],['CP6','RF34'],
    ['CP7','RF35'],['CP7','RF38'],['CP7','RF39'],['CP7','RF41'],['CP7','RF42'],
    ['ACESSO','RF01'],['ACESSO','RF02'],['ACESSO','RF00']
  ];

  var ST={
    PROB:'am',OG:'am',OE1:'am',OE2:'am',OE3:'am',OE4:'am',OE5:'am',TRANSV:'vd',
    CP1:'am',CP2:'vm',CP3:'vd',CP4:'vm',CP5:'vm',CP6:'vm',CP7:'vm',ACESSO:'vd',
    RF01:'vd',RF02:'vd',RF03:'am',RF04:'vm',RF05:'vm',RF06:'am',RF07:'am',RF08:'vm',
    RF09:'vm',RF10:'vm',RF11:'vm',RF12:'vm',RF13:'vd',RF14:'vd',RF15:'vd',RF16:'vd',
    RF17:'vd',RF18:'vd',RF19:'vd',RF20:'vd',RF21:'vm',RF22:'vm',RF23:'vm',RF24:'vm',
    RF25:'vm',RF26:'vm',RF27:'vm',RF28:'vm',RF29:'vm',RF30:'vm',RF31:'vm',RF32:'vm',
    RF33:'vm',RF34:'vm',RF35:'vm',RF38:'vm',RF39:'vm',RF41:'vm',RF42:'vm',RF00:'vd'
  };
  var CL={
    vd:{f:'#4CAF50',s:'#388E3C',t:'#fff'},
    am:{f:'#FFC107',s:'#F9A825',t:'#333'},
    vm:{f:'#F44336',s:'#C62828',t:'#fff'}
  };
  var DESC={
    PROB:'Problema central do CECP — gestão manual e descentralizada, dificultando o controle interno e a prestação de contas',
    OG:'Objetivo Geral — Fortalecer a gestão do CECP por meio de um sistema de gestão de alunos e da instituição, substituindo o controle manual e descentralizado',
    OE1:'OE1 — Centralizar os dados dos alunos em uma base tecnológica única',
    OE2:'OE2 — Garantir o acompanhamento pontual da assiduidade dos alunos nas aulas do CECP',
    OE3:'OE3 — Apoiar a aplicação e o histórico de medidas disciplinares',
    OE4:'OE4 — Facilitar a comunicação entre coordenação, voluntários e famílias',
    OE5:'OE5 — Assegurar transparência na prestação de contas a parceiros e órgãos de fiscalização',
    TRANSV:'Requisitos transversais de acesso e autenticação, aplicáveis a todo o sistema',
    CP1:'CP1 — Gestão e acompanhamento de turmas',
    CP2:'CP2 — Registro de doações e prestação de contas',
    CP3:'CP3 — Gestão de conteúdo institucional',
    CP4:'CP4 — Cadastro e histórico de alunos',
    CP5:'CP5 — Acompanhamento de frequência e disciplinar do aluno',
    CP6:'CP6 — Comunicação com voluntários e famílias',
    CP7:'CP7 — Matrícula online',
    ACESSO:'Acesso e controle de usuários (transversal)',
    RF01:'RF01 — Autenticar usuário',RF02:'RF02 — Controlar acesso',RF00:'RF00 — Encerrar sessão',
    RF03:'RF03 — Cadastrar turma',RF04:'RF04 — Editar turma',RF05:'RF05 — Inativar turma',
    RF06:'RF06 — Associar aluno à turma',RF07:'RF07 — Consultar alunos de uma turma',
    RF08:'RF08 — Registrar doação recebida',RF09:'RF09 — Editar doação recebida',
    RF10:'RF10 — Registrar documentos de prestação de contas',RF11:'RF11 — Editar documentos de prestação de contas',
    RF12:'RF12 — Consultar doações e prestações de contas',
    RF13:'RF13 — Publicar conteúdo institucional',RF14:'RF14 — Editar conteúdo institucional',
    RF15:'RF15 — Consultar conteúdo institucional',RF16:'RF16 — Remover conteúdo institucional',
    RF17:'RF17 — Publicar evento',RF18:'RF18 — Editar evento',RF19:'RF19 — Remover evento',RF20:'RF20 — Consultar eventos',
    RF21:'RF21 — Cadastrar aluno',RF22:'RF22 — Editar aluno',RF23:'RF23 — Consultar ficha do aluno',
    RF24:'RF24 — Inativar aluno',RF25:'RF25 — Remover dados do aluno',
    RF26:'RF26 — Registrar frequência',RF27:'RF27 — Consultar frequência',
    RF28:'RF28 — Emitir alerta de faltas críticas',RF29:'RF29 — Registrar medida disciplinar',
    RF30:'RF30 — Publicar aviso',RF31:'RF31 — Consultar avisos',RF32:'RF32 — Editar aviso',
    RF33:'RF33 — Remover aviso',RF34:'RF34 — Consultar histórico de avisos',
    RF35:'RF35 — Solicitar matrícula online (incorpora RF36, RF37 e RF40)',
    RF38:'RF38 — Registrar consentimento de dados pessoais',
    RF39:'RF39 — Registrar termo de uso de imagem',
    RF41:'RF41 — Emitir comprovante de solicitação',RF42:'RF42 — Analisar solicitações de matrícula'
  };

  /* ── LAYOUT (bottom-up): RF grouped by CP ── */
  var cpX={}, rfX={}, cx=PAD;
  CP_ORDER.forEach(function(cp){
    var rfs=CP_RF[cp], gw=(rfs.length-1)*SP;
    rfs.forEach(function(rf,i){rfX[rf]=cx+i*SP;});
    cpX[cp]=cx+gw/2;
    cx+=gw+GRP_GAP;
  });
  var W=cx-GRP_GAP+PAD;

  var oeIdeal={};
  OE_ORDER.forEach(function(oe){
    var cps=OE_CP[oe];
    oeIdeal[oe]=cps.reduce(function(s,c){return s+cpX[c];},0)/cps.length;
  });
  var sortedOEs=OE_ORDER.slice().sort(function(a,b){return oeIdeal[a]-oeIdeal[b];});
  var oeX={};
  sortedOEs.forEach(function(oe){oeX[oe]=oeIdeal[oe];});
  var j;
  for(j=1;j<sortedOEs.length;j++){
    var pr=sortedOEs[j-1],cu=sortedOEs[j];
    if(oeX[cu]<oeX[pr]+OE_MIN) oeX[cu]=oeX[pr]+OE_MIN;
  }
  for(j=sortedOEs.length-2;j>=0;j--){
    var cu2=sortedOEs[j],nx=sortedOEs[j+1];
    if(oeX[cu2]>oeX[nx]-OE_MIN) oeX[cu2]=oeX[nx]-OE_MIN;
  }

  var pos={};
  pos['PROB']={x:W/2,y:LY[0]};
  pos['OG']={x:W/2,y:(LY[0]+LY[1])/2};
  OE_ORDER.forEach(function(oe){pos[oe]={x:oeX[oe],y:LY[1]};});
  CP_ORDER.forEach(function(cp){pos[cp]={x:cpX[cp],y:LY[2]};});
  CP_ORDER.forEach(function(cp){
    CP_RF[cp].forEach(function(rf){pos[rf]={x:rfX[rf],y:LY[3]};});
  });

  /* ── BUILD SVG ── */
  var NS='http://www.w3.org/2000/svg';
  var svg=document.getElementById('tz-svg');
  var wrap=document.getElementById('tz-wrap');
  var tip=document.getElementById('tz-tip');

  var g=document.createElementNS(NS,'g');
  svg.appendChild(g);

  var didDrag=false;

  EDGES.forEach(function(e){
    var p1=pos[e[0]], p2=pos[e[1]];
    var dx=p2.x-p1.x, dy=p2.y-p1.y, d=Math.sqrt(dx*dx+dy*dy);
    var ln=document.createElementNS(NS,'line');
    ln.setAttribute('x1',p1.x+dx/d*R); ln.setAttribute('y1',p1.y+dy/d*R);
    ln.setAttribute('x2',p2.x-dx/d*R); ln.setAttribute('y2',p2.y-dy/d*R);
    ln.setAttribute('stroke','#888'); ln.setAttribute('stroke-width','1.4');
    ln.setAttribute('opacity','0.5');
    g.appendChild(ln);
  });

  Object.keys(pos).forEach(function(id){
    var p=pos[id], c=CL[ST[id]];
    var grp=document.createElementNS(NS,'g');

    var ci=document.createElementNS(NS,'circle');
    ci.setAttribute('cx',p.x); ci.setAttribute('cy',p.y); ci.setAttribute('r',R);
    ci.setAttribute('fill',c.f); ci.setAttribute('stroke',c.s); ci.setAttribute('stroke-width','2.2');
    ci.style.cursor='pointer';

    var tx=document.createElementNS(NS,'text');
    tx.setAttribute('x',p.x); tx.setAttribute('y',p.y);
    tx.setAttribute('text-anchor','middle'); tx.setAttribute('dominant-baseline','middle');
    tx.setAttribute('fill',c.t); tx.setAttribute('font-size','9');
    tx.setAttribute('font-weight','bold'); tx.setAttribute('font-family','monospace');
    tx.style.cursor='pointer';
    tx.textContent=id;

    grp.addEventListener('mouseenter',function(){
      ci.setAttribute('r',R+3); ci.setAttribute('stroke-width','3');
      tx.setAttribute('text-decoration','underline');
      tip.innerHTML=DESC[id]+'<br><span style="font-size:11px;opacity:0.6;font-style:italic;"></span>';
      tip.style.display='block';
    });
    grp.addEventListener('mousemove',function(ev){
      var br=wrap.getBoundingClientRect();
      var lx=ev.clientX-br.left+14, ly=ev.clientY-br.top-60;
      if(lx+345>br.width) lx=lx-360;
      tip.style.left=lx+'px'; tip.style.top=ly+'px';
    });
    grp.addEventListener('mouseleave',function(){
      ci.setAttribute('r',R); ci.setAttribute('stroke-width','2.2');
      tx.setAttribute('text-decoration','none');
      tip.style.display='none';
    });

    grp.appendChild(ci);
    grp.appendChild(tx);
    g.appendChild(grp);
  });

  /* ── ZOOM / PAN ── */
  var cw=wrap.clientWidth||820, ch=wrap.clientHeight||640;
  var CH=LY[LY.length-1]+R+PAD;
  var sc=Math.min((cw-16)/W,(ch-16)/CH,1);
  var tx0=(cw-W*sc)/2, ty0=Math.max((ch-CH*sc)/2,8);
  var scale=sc, txn=tx0, tyn=ty0, isDragging=false, sx,sy,stx,sty;

  function applyT(){g.setAttribute('transform','translate('+txn+','+tyn+') scale('+scale+')');}
  applyT();

  wrap.addEventListener('wheel',function(ev){
    ev.preventDefault();
    var br=wrap.getBoundingClientRect();
    var mx=ev.clientX-br.left, my=ev.clientY-br.top;
    var ns=Math.min(Math.max(scale*(ev.deltaY<0?1.12:0.89),0.2),4);
    txn=mx-(mx-txn)*(ns/scale); tyn=my-(my-tyn)*(ns/scale); scale=ns; applyT();
  },{passive:false});

  wrap.addEventListener('mousedown',function(ev){
    isDragging=true; didDrag=false;
    sx=ev.clientX; sy=ev.clientY; stx=txn; sty=tyn;
    wrap.style.cursor='grabbing';
  });
  document.addEventListener('mousemove',function(ev){
    if(!isDragging) return;
    if(Math.abs(ev.clientX-sx)>3||Math.abs(ev.clientY-sy)>3) didDrag=true;
    txn=stx+(ev.clientX-sx); tyn=sty+(ev.clientY-sy); applyT();
  });
  document.addEventListener('mouseup',function(){isDragging=false; wrap.style.cursor='grab';});

  document.getElementById('tz-in').addEventListener('click',function(){scale=Math.min(scale*1.2,4);txn=(cw-W*scale)/2;tyn=Math.max((ch-CH*scale)/2,8);applyT();});
  document.getElementById('tz-out').addEventListener('click',function(){scale=Math.max(scale*0.8,0.2);txn=(cw-W*scale)/2;tyn=Math.max((ch-CH*scale)/2,8);applyT();});
  document.getElementById('tz-reset').addEventListener('click',function(){scale=sc;txn=tx0;tyn=ty0;applyT();});
})();
</script>

| Cor | Status |
| :---: | :--- |
| 🟢 Verde | **Totalmente concluído** — entregue e validado com o cliente |
| 🟡 Amarelo | **Parcialmente concluído** — entregue com débito técnico ou dependente de itens incompletos |
| 🔴 Vermelho | **Não iniciado** — previsto em sprint futura ou em andamento sem entrega confirmada |

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 15/11/2026 | Matriz-síntese e grafo movidos do documento arquivado (seção 8.3) para esta página vigente; RNFs alinhados às fichas, RF36, RF37 e RF40 incorporados ao RF35 (DEC16), RNF04 e RNF05 retirados (DEC17) e situação do grafo atualizada | — |  |
