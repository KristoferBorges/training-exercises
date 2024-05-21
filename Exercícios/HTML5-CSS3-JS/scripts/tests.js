// Função para animar a imagem do botão e iniciar o jogo
document.addEventListener("DOMContentLoaded", function() {
    let botao = document.getElementById("buttonStart");
    let imagem = document.getElementById("buttonStart_img");

    botao.addEventListener("click", function() {
        imagem.src = "/Exercícios/HTML5-CSS3-JS/image/buttonStartPress.png"

        setTimeout(function() {
            imagem.src = "/Exercícios/HTML5-CSS3-JS/image/buttonStart.png";
        }, 100);
    });
});