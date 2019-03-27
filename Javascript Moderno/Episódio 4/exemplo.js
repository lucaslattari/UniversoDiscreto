"use strict";

/*
Conhecemos alguns operadores matemáticos para comparação:

-"a maior que b": a > b
-"a maior ou igual a b": a >= b
-"a igual a b": a == b (lembre-se que 'a = b' é uma operação de
atribuição)
-"a não é igual a b": a != b

Esses operadores retornam um valor booleano como resultado.
*/

alert(2 > 1); //true
alert(2 == 1); //false
alert(2 != 1); //true

//Mesmo o valor booleano pode ser guardado dentro de uma variável

let result = 5 > 4;
alert(result);

/*é possível fazer comparação envolvendo palavras. Nesse caso,
a ordem alfabética será empregada*/

alert('Z' > 'A'); //true
alert('Gle' < 'Gla'); //false
alert('abc' > 'ab'); //true (maior palavra 'vence')
alert('ab' == 'ab'); //true

/*Se compararmos valores de tipos diferentes, então o JS converterá os valores
para números.*/
alert( '2' > 1 ); // true, pois palavra "2" é convertido pra número, e então comparada com 1
alert( '01' == 1 ); //true, palavra '01' se torna número 1

/*no caso de booleanos, true é equivalente a 1 e false é equivalente a 0*/
alert( true == '01' ); // true
alert( false == 0 ); // true

/*no JS o operador == possui um problema: não diferenciar 0 de false*/
alert(0 == false);//true
alert('' == false); //true

/*isso ocorre pois os operandos são convertidos para número pelo operador ==
uma string vazia se torna zero, assim como false

e se quisermos que 0 e false sejam objetos diferentes?

Usamos === para checar a igualdade sem conversão de tipos

Assim, se a e b forem de tipos diferentes e aplicarmos a === b, então
esse operador retornará falso imediatamente, sem fazer conversões*/

alert(0 === false); //false, pois os tipos são diferentes

//analogamente podemos aplicar !== para "não igualdade restrita"
alert(0 != false); //0 e false são convertidos para 0, são iguais, portanto retorna false
alert(0 !== false); //tipos diferentes, são diferentes, retorna true

/*null e undefined são convertidos para número 0 e NaN, respectivamente*/
alert(null == undefined);//retorna true
alert(null === undefined); //null e undefined são tipos diferentes, retorna falso

//e quanto ao nulo e o 0?
alert( null >= 0 ); // verdadeiro, pois nulo é convertido para 0
alert( null > 0 );  // falso, pois da mesma forma nulo é convertido pra 0

//no entanto:
alert(null == 0); //é falso, pois não ocorre conversão

//em se tratando de undefined, ele é convertido pro número especial Nan
alert( undefined > 0 ); // false
alert( undefined < 0 ); // false
alert( undefined == 0 ); // false

/*assim, compreenda que você não deve usar >= < > <= com variáveis que recebam
valor null ou undefined, a não ser que você tenha absoluta certeza do que é
que está fazendo. prefira ===*/
alert(null == undefined);
alert(null === undefined);

//vamos conhecer agora algumas funções para interface de usuário
//já adotamos muito a alert
alert("Ola!");

/*a função prompt mostra uma janela modal com uma mensagem de texto,
um campo para o visitante e um botão ok/cancelar

o primeiro parâmetro é a mensagem de texto a aparecer na janela
o segundo parâmetro é opcional e é o valor padrão escrito na caixa de texto
*/
let age = prompt('Quantos anos voce possui?', 100);

alert(`Voce tem ${age} anos!`); // You are 100 years old!

/*temos também a função confirm que mostra uma janela modal com uma
pergunta e 2 botões: ok ou cancelar

O resultado é verdadeiro se apertar ok e falso, caso contrário*/
let isBoss = confirm("Voce eh o chefe?");

alert( isBoss ); //true se ok for pressionado
