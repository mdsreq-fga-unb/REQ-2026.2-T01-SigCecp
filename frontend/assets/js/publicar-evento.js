
// ---------- Painel de pagamento ----------

const painel = document.getElementById("painel-pagamento");
const radios = document.querySelectorAll('input[name="cobrado"]');

if (painel) {
    const camposPagamento = painel.querySelectorAll("input, select");

    function atualizarPainel() {
        const escolhido = document.querySelector(
            'input[name="cobrado"]:checked'
        );

        const cobrado = escolhido !== null && escolhido.value === "true";

        painel.hidden = !cobrado;

        camposPagamento.forEach(campo => {
            campo.disabled = !cobrado;
            campo.required = cobrado;
        });
    }

    radios.forEach(radio => {
        radio.addEventListener("change", atualizarPainel);
    });

    atualizarPainel();
}


// ---------- Pré-visualização da imagem ----------

const inputImagem = document.getElementById("adicionar-imagens");
const previewImagem = document.getElementById("preview-imagem");
const containerPreview = document.getElementById("container-preview");

if (inputImagem && previewImagem && containerPreview) {
    let imagemAnterior = null;

    inputImagem.addEventListener("change", () => {
        const arquivo = inputImagem.files[0];

        if (imagemAnterior) {
            URL.revokeObjectURL(imagemAnterior);
            imagemAnterior = null;
        }

        containerPreview.hidden = true;
        previewImagem.removeAttribute("src");

        if (!arquivo) return;

        if (!arquivo.type.startsWith("image/")) {
            console.error("Selecione um arquivo de imagem válido.");
            return;
        }

        imagemAnterior = URL.createObjectURL(arquivo);

        previewImagem.onload = () => {
            containerPreview.hidden = false;
        };

        previewImagem.onerror = () => {
            containerPreview.hidden = true;
            console.error("Erro ao carregar a pré-visualização.");
        };

        previewImagem.src = imagemAnterior;
    });
} else {
    console.error("Elementos da pré-visualização não encontrados.");
}

// ---------- Pré-visualização de vídeo ----------

const inputVideo = document.getElementById("adicionar-video");
const previewVideo = document.getElementById("preview-video");
const containerPreviewVideo = document.getElementById(
    "container-preview-video"
);

if (inputVideo && previewVideo && containerPreviewVideo) {
    let videoAnterior = null;

    inputVideo.addEventListener("change", () => {
        const arquivo = inputVideo.files[0];

        if (videoAnterior) {
            URL.revokeObjectURL(videoAnterior);
            videoAnterior = null;
        }

        previewVideo.pause();
        previewVideo.removeAttribute("src");
        previewVideo.load();

        containerPreviewVideo.hidden = true;

        if (!arquivo) return;

        if (!arquivo.type.startsWith("video/")) {
            console.error("Selecione um arquivo de vídeo válido.");
            return;
        }

        videoAnterior = URL.createObjectURL(arquivo);

        previewVideo.onloadedmetadata = () => {
            containerPreviewVideo.hidden = false;
        };

        previewVideo.onerror = () => {
            containerPreviewVideo.hidden = true;
            console.error("Erro ao carregar a pré-visualização do vídeo.");
        };

        previewVideo.src = videoAnterior;
        previewVideo.load();
    });
}