const inputImagens = document.getElementById("adicionar-imagens");
const containerPreview = document.querySelector(".imagem-preview");
const previewImagem = document.getElementById("preview-imagem");

let urlImagemAtual = null;

inputImagens.addEventListener("change", () => {
    const arquivo = inputImagens.files[0];

    if (urlImagemAtual) {
        URL.revokeObjectURL(urlImagemAtual);
        urlImagemAtual = null;
    }

    if (!arquivo) {
        containerPreview.hidden = true;
        return;
    }

    if (!arquivo.type.startsWith("image/")) {
        alert("Selecione uma imagem válida.");
        inputImagens.value = "";
        containerPreview.hidden = true;
        return;
    }

    urlImagemAtual = URL.createObjectURL(arquivo);

    previewImagem.src = urlImagemAtual;
    containerPreview.hidden = false;
});

const inputVideo = document.getElementById("adicionar-video");
const previewVideo = document.getElementById("preview-video");

let urlVideoAtual = null;

inputVideo.addEventListener("change", () => {
    previewVideo.innerHTML = "";

    // Libera a URL anterior
    if (urlVideoAtual) {
        URL.revokeObjectURL(urlVideoAtual);
        urlVideoAtual = null;
    }

    const arquivo = inputVideo.files[0];

    if (!arquivo) return;

    if (!arquivo.type.startsWith("video/")) {
        alert("Selecione um arquivo de vídeo válido.");
        inputVideo.value = "";
        return;
    }

    urlVideoAtual = URL.createObjectURL(arquivo);

    const video = document.createElement("video");

    video.src = urlVideoAtual;
    video.controls = true;
    video.preload = "metadata";

    previewVideo.appendChild(video);
});