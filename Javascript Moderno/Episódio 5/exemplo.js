"use strict";

/*Em alguns momentos, torna-se mais conveniente executarmos
diferentes ações para diferentes condições

Para isso, usamos a instrução if e uma condição que também
pode ser executada com ? para fins de simplicidade

A palavra-chave if avalia uma condição e se essa condição
for verdadeira, então o bloco de código envolvido por chaves
é executado. Se não, então o referido bloco é ignorado.*/

let color = prompt("Qual a cor do cavalo branco de Napoleao?", '')
if(color == 'branco'){
  alert("Parabens, voce eh um genio!");
}

/*Como falei, a instrução if avalia uma expressão e converte
seu resultado para um booleano

Como discutimos no vídeo passado de JS, o número 0, uma string
vazia "", null, undefined e NaN são convertidas para falso

Outros valores são convertidos para verdadeiro
*/

//Assim, a expressão que é avaliada como 0 não é executada*/

if (0)
{
  //nunca entra aqui
}

if (1)
{
  //sempre entra aqui
}

/*uma expressão booleana armazenada em uma variável tb
pode servir como parâmetro de um if*/
let cond = (color == 'branco');
if(cond)
{
  //...
}

/*o if pode conter um bloco else. Esse bloco else
só é executado quando a condição é falsa*/

let color = prompt('Qual a cor do cavalo branco de Napoleao', '');

if (color == 'branco') {
  alert('Parabens, voce eh um genio!');
} else {
  alert('Como voce pode estar tao errado?'); //qualquer coisa diferente de branco
}

/*em alguns momentos queremos testar uma série de variações de uma
condição, para isso usamos else if*/
let bolinhas = prompt('Quantas bolinhas tem aqui? ooo', '');

if (bolinhas > 3) {
  alert('Voce errou para mais!');
} else if (bolinhas < 3){
  alert('Voce errou para menos!');
}else {
  alert('Voce acertou na mosca!');
}


/*no código acima, o javascript primeiramente checa se o número de
bolinhas é maior do que 3. Se essa condição for falsa, então ele
vai checar a condição bolinhas menor do que 3. Se essa também
for falsa, ele irá executar o último bloco else.

Você pode incluir quantos blocos else if quiser, e o último else
é opcional*/

//em alguns casos, queremos que uma variável receba um valor de acordo com a condição
let permissaoDeAcesso;
let idade = prompt('Quantos anos voce tem?', '');

if (idade > 18) {
  permissaoDeAcesso = true;
} else {
  permissaoDeAcesso = false;
}

alert("Acesso: "+permissaoDeAcesso);

/*quando o tipo de condição é semelhante a essa, podemos usar o if ternário. Ele
tem esse nome pois são usados 3 operandos para manuseá-lo. Veja um exemplo*/
let permissaoDeAcesso = (idade > 18) ? true : false;

/*assim, a variável permissaoDeAcesso receberá true se a idade for maior do que 18.
Caso contrário, ela receberá false. Esse if ternário cumpre o mesmo papel de if else
de maneira compacta*/

//inclusive, se vc quiser, vc pode compactar mais ainda
let permissaoDeAcesso = idade > 18;

/*também é possível utilizar uma sequência de operadores if ternário, que
assim podem retornar valores que dependem de várias condições*/

let idade = prompt('Qual sua idade?', 18);
let message;
if (idade < 3) {
  message = 'Voce eh muito jovem para ver isso!';
} else if (idade < 18) {
  message = 'Voce devia ver isso quando for maior de idade!';
} else if (idade < 100) {
  message = 'Voce pode ver isso agora!';
} else {
  message = 'Que idade incomum!';
}
alert(message);

//podemos reescrever o if acima dessa mesma maneira
let idade = prompt('Qual sua idade?', 18);
let message = (idade < 3) ? 'Voce eh muito jovem para ver isso!' :
  (idade < 18) ? 'Voce devia ver isso quando for maior de idade!' :
  (idade < 100) ? 'Voce pode ver isso agora!'; :
  'Que idade incomum!';
}
alert(message);
/*pode parecer difícil entender esse código num primeiro momento, mas
o que ele faz é simples: ele primeiro verifica se a idade é menor do que
3. Se for, a variável message recebe 'Voce eh muito jovem para ver isso!'.
Caso contrário, você realiza um segundo teste: se idade é menor do que 18,
a variável message recebe 'Voce devia ver isso quando for maior de idade!'.
Caso contrário, mais um teste é realizado: se idade for menor do que 100,
message recebe 'Voce pode ver isso agora!'. Caso contrário, acabam-se os
testes e message recebe 'Que idade incomum!'.*/

/*use o operador if ternário com sabedoria, pois ele é menos legível
do que um if convencional. Inclusive, só use ele se um valor for retornado
por uma variável. Quando for executar um código diferente dependendo
da condição testada, use if comum.*/
let so = prompt('Qual sistema operacional eh melhor?', '');

(so == 'Windows') ?
   alert('Parabens!') : alert('Errado.');
   
let so = prompt('Qual sistema operacional eh melhor?', '');

if (so == 'Windows') {
  alert('Parabens!');
} else {
  alert('Errado.');
}

//note que no código acima, dois alerts diferentes podem ser acionados.
//não há variável recebendo valor alí. nesse caso, use if comum.