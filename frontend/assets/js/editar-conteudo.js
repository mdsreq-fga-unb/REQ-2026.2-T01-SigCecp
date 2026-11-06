function ligarPrevia(inputId, previaId, nomeRemover) {
    const input = document.getElementById(inputId);
    const previa = document.getElementById(previaId);
    input.addEventListener('change', () => {
      const arq = input.files[0];
      if (!arq) { previa.hidden = true; return; }
      previa.src = URL.createObjectURL(arq);
      previa.hidden = false;
      const rem = document.querySelector(`[name="${nomeRemover}"]`);
      if (rem) rem.checked = false;
    });
  }
  ligarPrevia('imagem', 'previa-imagem', 'remover_imagem');
  ligarPrevia('video', 'previa-video', 'remover_video');
