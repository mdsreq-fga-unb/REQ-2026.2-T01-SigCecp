// Ficha do aluno: mostra campos que dependem de uma resposta (RN38) e imprime a ficha (RN45).
(function () {
  const dependentes = document.querySelectorAll('[data-mostrar-se]');

  function atualizar() {
    dependentes.forEach((bloco) => {
      const [nome, valor] = bloco.dataset.mostrarSe.split('=');
      const marcado = document.querySelector(`input[name="${nome}"]:checked`);
      bloco.hidden = !marcado || marcado.value !== valor;
    });
  }

  if (dependentes.length) {
    document.addEventListener('change', (evento) => {
      if (evento.target.matches('input[type="radio"]')) atualizar();
    });
    atualizar();
  }

  document.querySelectorAll('[data-imprimir]').forEach((botao) => {
    botao.addEventListener('click', () => window.print());
  });
})();
