document.addEventListener('DOMContentLoaded', function () {
    var botaoExibir = document.getElementById('botaoExibir');
    botaoExibir.addEventListener('click', exibirConteudo);
});
function exibirConteudo() {
    var caixaDeTexto = document.getElementById('caixaDeTexto');
    var conteudo = caixaDeTexto.value;
    var display = document.getElementById('conteudo');

    if(conteudo == '') {
        caixaDeTexto.style.border = '1px solid red'
       display.innerHTML = 'Digite algo!'
       display.style.color = 'red'
    }
}