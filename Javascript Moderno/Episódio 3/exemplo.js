"use strict";

/*
Na maior parte do tempo, operadores e funções
convertem automaticamente os valores para um
determinado tipo. Isso é o que chamamos de
conversão de tipos.

Por exemplo, a função alert converte automaticamente
os valores para um tipo string. Operadores matemáticos
convertem valores para números.

Entretanto, existem casos em que precisamos converter
um valor para um determinado tipo. Traremos alguns
exemplos disso ao longo do vídeo.

Podemos converter um valor para string da seguinte maneira:
*/

let value = true;
alert(typeof value); //boolean

value = String(value);
alert(typeof value); //string

/* Conversões numéricas ocorrem automaticamente, mesmo se
operações forem realizadas em strings. */

alert("6" / "2"); //3

/*Podemos usar Number(value) para converter um valor
explicitamente*/

let str = "123";
alert(typeof str); //string

let num = Number(str); //virou o número 123
alert(typeof num); //number

/*se a string não for um número válido, valor
é convertido para NaN (Not a Number), que é de
tipo undefined*/

let nan = Number("oi");
alert(nan); //NaN, conversão inválida

alert(Number("   123   ")); //123
alert(Number("123abc")); //NaN
alert(Number(true)); //1
alert(Number(false)); //0

/*As operações matemáticas convertem valores string
para números, com exceção da adição. Se um dos valores
somados é uma string, daí ocorre uma concatenação e
uma conversão para string.*/
alert(1 + '2');
alert('1' + 2);

/*A conversão para booleano é bem tranquila. Valores como
0, string vazia, null, undefined e NaN se tornam falso.
Qualquer coisa diferente disso é verdadeiro.*/
alert(Boolean(1)); // true
alert(Boolean(0)); // false

alert(Boolean("hello")); // true
alert(Boolean("")); // false

/* é importante frisar que "0" é uma string com algo dentro,
logo, é verdadeiro. Da mesma forma, uma string com algum
espaço também é verdadeiro. */
alert(Boolean("0")); // true
alert(Boolean(" ")); // spaces, also true (any non-empty string is true)

/*vamos falar agora de operadores! Temos os operadores unários, que são
aplicados em um único valor. Um bom exemplo disso é negativo, que inverte
o sinal de um valor numérico*/
let x = 1;
x = -x;
alert(x);

/*Já os operadores binários são os que manipulam dois valores. Um bom
exemplo disso é a subtração*/
let z = 1, y = 3;
alert(y - z);

/*Podemos fazer concatenação de strings por meio do operador de soma*/
let s = "my " + " string";
alert(s);

/*O Javascript faz a conversão de valores em strings automaticamente*/
alert('1' + 2);
alert(2 + '1');
alert(2 + 2 + '1'); //41, pois soma primeiro da esquerda pra direita e depois concatena

/*Outros operadores aritméticos convertem caracteres para números*/
alert(2 - '1'); // 1
alert('6' / '2'); //3

/* sinal de + não tem efeito como operador unário*/
let q = 2;
alert(+q); //-2

/*lembrar da precedência de operador é importante*/
let w = 2 + 3 * 2; //8
alert(w);

/*atribuições em cadeia também são permitidas*/
let a, b, c;
a = b = c = 2 + 2;
alert(a); //4
alert(b); //4
alert(c); //4

/*resto da divisão*/
alert(5 % 2);//1

/*exponencial*/
alert(2 ** 4); //8
alert(8 ** (1/2)) //2

/*incremento*/
let counter = 1;
a = ++counter; //2
alert(a);

counter = 1;
a = counter++; //1
alert(a);

counter = 0;
counter++;
++counter;
alert(counter); //2

/*operador vírgula computa várias operações, mas retorna apenas
a última*/
counter = (a = 1, b = 2, a + b);
alert(counter);
