"use strict";

/*
Na maior parte do tempo, as aplicações
javascript precisam trabalhar com
informações

Temos dois exemplos:
1. Uma loja online, em que as informações
incluídas podem ser os produtos vendidos
e um carrinho de compras online.

2. Uma aplicação de batepapo, em que as
informações podem ser os usuários, as
mensagens trocadas, dentre outros.

Como sabemos, uma variável armazena
um determinado valor e precisa de um
nome.

Para criar uma variável em Javascript
moderno, usamos a palavra-chave let*/

let mensagem;

/*podemos atribuir um valor qualquer
por meio da atribuição = */

mensagem = 'Oi!';

/*no caso, optamos pela string "Oi!".
Dessa forma, a palavra oi! está
guardada na memória e pode ser
acessada pela variável mensagem
que criamos*/

alert(mensagem);

/*podemos declarar múltiplas variáveis
em uma mesma linha*/

let usuario = 'Lucas', idade = 32, profissao = 'youtuber';

/*em códigos antigos costumava-se usar
a palavra-chave var para declarar uma
variável. atualmente, recomenda-se o
uso de let para tal*/

/*também podemos trocar os valores
das variáveis*/

mensagem = 'tudo bom?';

alert(mensagem);

/*e obviamente podemos trocar o
valor de uma variável pela
informação de uma variável diferente*/

var outraMensagem = "beleza?";
mensagem = outraMensagem;

alert(mensagem);

/*para declarar uma constante, ou seja,
uma variável com valor que não pode ser
alterado, você a declara com const*/

const aniversario = '25.03.1986';

/*recomenda-se que você declare constantes
usando caixa alta, como no exemplo*/

const VERMELHO = "#F00";
const VERDE = "#0F0";
const AZUL = "#00F";
const LARANJA = "#FF7F00";

var cor = LARANJA;
alert(cor);

/*uma variável javascript pode conter
diversos tipos de dados. uma mesma
variável pode ser uma string e
receber logo depois um valor numérico*/

let variavel = "olá!";
variavel = 123456;

alert(variavel);

/*linguagens de programação que permitem
isso são chamadas de dinamicamente tipadas,
dando a entender que as variáveis possuem
tipos que não são necessariamente fixos ao
longo de um programa*/

/*existem 7 tipos de dados no Javascript
moderno, vamos ver cada uma delas a seguir.*/

let numero = 123;
numero = 12.345;

/*o tipo número refere-se tanto ao
inteiro quanto aos números reais.
logicamente as quatro operações fundamentais
estão disponíveis para esse tipo*/

/*além dos números regulares, existem os
valores numéricos especiais, que podem
ser Infinity, -Infinity e NaN*/

/*O infinito pode ser conseguido apenas
fazendo uma divisão por zero ou mencionando
diretamente no código*/

alert(1 / 0);
alert(Infinity);

/*O NaN já indica um valor inválido.
ele pode ocorrer ao fazer uma operação
indefinida, como dividir uma palavra por
um número qualquer*/

alert("não é número" / 2);

/*as cadeias de caracteres são strings, que
podem ser representadas de 3 maneiras*/

let string1 = "Lucas";
let string2 = 'Lucas';
let string3 = `${string1}`;

/*não existe diferença tanto em string1
quanto em string2. em string3, quando
usamos as aspas `${}`, podemos incorporar
variáveis dentro da string. operações
matemáticas também são válidas*/

alert(string3);
alert(`${2 + 2}`);

/*outro tipo existente é o booleano.
por meio dele podemos apenas armazenar
verdadeiro e falso*/

let lucasEhYoutuber = true;
let lucasEhPadeiro = false;

/*operações booleanas também podem ser
atribuídas*/
let ehMaior = 4 > 1;
alert(ehMaior);

/*o valor null implica que o valor
da variável difere de todos os
tipos mencionados acima. */

let nulo = null;

/*em javascript o null é um valor
com o sentido de nada, vazio ou
valor desconhecido*/

/*além disso o javascript possui
o tipo indefinido, que significa que
o valor atribuído a variável não foi
assinalado ainda*/

/*uma variável criada sem atribuição
recebe por padrão o valor indefinido*/
let x;
alert(x);

/*podemos fazer uma variável receber
indefinido*/
x = 124;
x = undefined;

alert(x);

/*entretanto, isso não é recomendado.
é preferível que se use null para
deixar a variável vazia ou com
valor desconhecido para um determinado
momento*/

/*O operador typeof retorna o tipo
de uma variável. isso é útil quando
você trabalha com variáveis de diferentes
tipos simultaneamente, ou precisa
checar rapidamente o tipo de determinada
variável*/

typeof undefined // "undefined"
typeof 0 // "number"
typeof true // "boolean"
typeof "foo" // "string"
typeof alert // "function"  (3)
