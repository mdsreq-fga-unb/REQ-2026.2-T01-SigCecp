(function () {
    const modal = document.getElementById("modal-remover");
    const form = document.getElementById("form-remover");
    const nome = document.getElementById("modal-remover-conteudo");
 
    document.querySelectorAll("[data-remover-conteudo]").forEach(function (botao) {
      botao.addEventListener("click", function () {
        form.action = botao.dataset.action;
        nome.textContent = botao.dataset.titulo;
        modal.showModal();
      });
    });
 
    modal.querySelectorAll("[data-fechar-modal]").forEach(function (botao) {
      botao.addEventListener("click", function () { modal.close(); });
    });
 
    // clicar fora da caixa (no fundo escurecido) também fecha
    modal.addEventListener("click", function (e) {
      if (e.target === modal) modal.close();
    });
  })();
