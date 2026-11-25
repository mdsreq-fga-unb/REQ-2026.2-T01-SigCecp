// Impede horário de término igual ou anterior ao de início. O servidor valida de novo ao salvar.
(function () {
  const inicio = document.getElementById('inicio');
  const termino = document.getElementById('termino');
  if (!inicio || !termino) return;

  function conferir() {
    termino.min = inicio.value;
    const invalido = inicio.value && termino.value && termino.value <= inicio.value;
    termino.setCustomValidity(invalido ? 'O horário de término deve ser depois do horário de início.' : '');
    if (invalido) termino.setAttribute('aria-invalid', 'true');
    else termino.removeAttribute('aria-invalid');
  }

  inicio.addEventListener('input', conferir);
  termino.addEventListener('input', conferir);
  conferir();
})();
