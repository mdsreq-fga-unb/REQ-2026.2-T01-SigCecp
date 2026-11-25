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

  // Máscaras de telefone, CPF e CEP. O servidor valida de novo ao salvar.
  // Texto com letras (como "não aplicável") não é mascarado.
  const mascaras = {
    telefone(digitos) {
      const d = digitos.replace(/^0/, '').slice(0, 11);
      if (d.length <= 2) return d.length ? `(${d}` : '';
      const numero = d.slice(2);
      const corte = numero.length > 8 ? 5 : 4;
      return `(${d.slice(0, 2)}) ${numero.slice(0, corte)}${numero.length > corte ? '-' + numero.slice(corte) : ''}`;
    },
    cpf(digitos) {
      const d = digitos.slice(0, 11);
      return d.replace(/^(\d{3})(\d)/, '$1.$2')
        .replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3')
        .replace(/\.(\d{3})(\d{1,2})$/, '.$1-$2');
    },
    cep(digitos) {
      const d = digitos.slice(0, 8);
      return d.length > 5 ? `${d.slice(0, 5)}-${d.slice(5)}` : d;
    },
  };

  document.querySelectorAll('[data-mascara]').forEach((campo) => {
    const formatar = mascaras[campo.dataset.mascara];
    campo.addEventListener('input', () => {
      if (/[a-zA-ZÀ-ÿ]/.test(campo.value)) return;
      campo.value = formatar(campo.value.replace(/\D/g, ''));
    });
  });

  document.querySelectorAll('[data-imprimir]').forEach((botao) => {
    botao.addEventListener('click', () => window.print());
  });
})();
