//lê arquivo de texto local
function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest(); //construtor de funcionalidade que transfere dados entre cliente e servidor
    rawFile.overrideMimeType("application/json"); //especifica tipo do stream tratado a ser json
    rawFile.open("GET", file); //requisição de abertura de arquivo usando método GET
    rawFile.onreadystatechange = function() { //quando o evento readystatechange é disparado (por exemplo, quando documento é carregado)
        if (rawFile.readyState === 4 && rawFile.status == "200") { //readyState == 4 (DONE, operação concluída pelo user agent, browser) e status == 200 (OK, requisição correta de acordo com o servidor)
            callback(rawFile.responseText); //chama a função que programamos no index.html
        }
    }
    rawFile.send(null); //envia requisição ao servidor
}
