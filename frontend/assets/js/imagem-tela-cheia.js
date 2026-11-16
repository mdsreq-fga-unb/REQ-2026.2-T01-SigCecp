// Abre em tela cheia as imagens marcadas com [data-tela-cheia] (detalhe de conteúdo e de evento).
// Com mais de uma imagem na página, as setas (na tela e no teclado) passam de uma para outra.
(function () {
    const gatilhos = Array.from(document.querySelectorAll("[data-tela-cheia]"));
    if (!gatilhos.length) return;

    const modal = document.createElement("dialog");
    modal.className = "tela-cheia";
    modal.setAttribute("aria-label", "Imagem em tela cheia");
    modal.innerHTML =
      '<button type="button" class="tela-cheia__fechar" aria-label="Fechar">&times;</button>' +
      '<button type="button" class="tela-cheia__seta tela-cheia__seta--anterior" aria-label="Imagem anterior">&#8249;</button>' +
      '<img class="tela-cheia__imagem" alt="">' +
      '<button type="button" class="tela-cheia__seta tela-cheia__seta--proxima" aria-label="Próxima imagem">&#8250;</button>' +
      '<p class="tela-cheia__contador" aria-live="polite"></p>';
    document.body.appendChild(modal);

    const imagem = modal.querySelector(".tela-cheia__imagem");
    const contador = modal.querySelector(".tela-cheia__contador");
    const varias = gatilhos.length > 1;
    let atual = 0;

    modal.querySelectorAll(".tela-cheia__seta, .tela-cheia__contador").forEach(function (el) {
      el.hidden = !varias;
    });

    function mostrar(indice) {
      atual = (indice + gatilhos.length) % gatilhos.length;
      const origem = gatilhos[atual].querySelector("img");
      imagem.src = origem.currentSrc || origem.src;
      imagem.alt = origem.alt;
      contador.textContent = (atual + 1) + " de " + gatilhos.length;
    }

    gatilhos.forEach(function (gatilho, indice) {
      gatilho.addEventListener("click", function () {
        mostrar(indice);
        modal.showModal();
      });
    });

    modal.querySelector(".tela-cheia__fechar").addEventListener("click", function () { modal.close(); });
    modal.querySelector(".tela-cheia__seta--anterior").addEventListener("click", function () { mostrar(atual - 1); });
    modal.querySelector(".tela-cheia__seta--proxima").addEventListener("click", function () { mostrar(atual + 1); });

    modal.addEventListener("keydown", function (e) {
      if (!varias) return;
      if (e.key === "ArrowLeft") mostrar(atual - 1);
      if (e.key === "ArrowRight") mostrar(atual + 1);
    });

    // clicar no fundo escuro (fora da imagem e dos botões) fecha
    modal.addEventListener("click", function (e) {
      if (e.target === modal) modal.close();
    });
})();
