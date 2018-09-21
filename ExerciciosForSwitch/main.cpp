#include <stdio.h>
#include <stdlib.h>

void Exercicio1()
{
    int i;
    for(i = 99 ; i >= 49 ; i--)
    {
        printf("%d ", i);
    }
}

void Exercicio2()
{
    int i, valor;
    for(i = 0 ; i < 100 ; i++)
    {
        printf("Informe um valor: ");
        scanf("%d", &valor);

        printf("O quadrado desse numero eh: %d.\n", valor * valor);
    }
}

void Exercicio3()
{
    int i;
    for(i = 190 ; i >= 160 ; i--)
    {
        printf("%d ", i);
    }
}

void Exercicio4()
{
    int i, j, naoEhPrimo;
    for(i = 190 ; i >= 160 ; i--)
    {
        //tudo aqui verifica se "i" é primo
        naoEhPrimo = 0;
        for(j = 2 ; j < i ; j++)
        {
            if((i % j) == 0)
            {
                naoEhPrimo = 1;
            }
        }

        //"i" é primo? se for, imprime ele, caso contrário
        //não imprime
        if(naoEhPrimo == 0)
            printf("%d ", i);
    }
}

void Exercicio5()
{
    int i, valorUsuario, maiorValor;
    for(i = 0 ; i < 10 ; i++)
    {
        printf("Informe um numero: ");
        scanf("%d", &valorUsuario);

        if(i == 0)
        {
            maiorValor = valorUsuario;
        }else if(valorUsuario > maiorValor)
        {
            maiorValor = valorUsuario;
        }
    }

    printf("O maior valor eh: %d\n", maiorValor);
}

void Exercicio1Switch()
{
    int dia;
    printf("Informe o dia: ");
    scanf("%d", &dia);

    switch(dia)
    {
    case 1: //domingo
        printf("fim de semana.\n");
        break;
    case 2: //segunda
        printf("dia de semana.\n");
        break;
    case 3: //terça
        printf("dia de semana.\n");
        break;
    case 4: //quarta
        printf("dia de semana. \n");
        break;
    case 5: //quinta
        printf("dia de semana.\n");
        break;
    case 6: //sexta
        printf("dia de semana.\n");
        break;
    case 7: //sabado
        printf("final de semana.\n");
        break;
    default:
        printf("dia invalido.\n");
        break;
    }

    int mes;
    printf("Informe o mes: ");
    scanf("%d", &mes);

    switch(mes)
    {
    case 1: //janeiro
        printf("alta temporada.\n");
        break;
    case 2: //fevereiro
        printf("alta temporada.\n");
        break;
    case 3: //marco
    case 4: //abril
    case 5: //maio
        printf("baixa temporada.\n");
        break;
    case 6: //junho
    case 7: //julho
        printf("alta temporada.\n");
        break;
    case 8: //agosto
    case 9: //setembro
    case 10: //outubro
    case 11: //novembro
        printf("baixa temporada.\n");
        break;
    case 12: //dezembro
        printf("alta temporada.\n");
        break;
    }
}

void Exercicio2Switch()
{
    int mes;
    printf("Informe o mes: ");
    scanf("%d", &mes);

    switch(mes)
    {
    case 1: //janeiro
        printf("31 dias.\n");
        break;
    case 2: //fevereiro
        printf("28 dias.\n");
        break;
    case 3: //marco
        printf("30 dias.\n");
        break;
    case 4: //abril
        printf("31 dias.\n");
        break;
    case 5: //maio
        printf("30 dias.\n");
        break;
    case 6: //junho
        printf("31 dias.\n");
        break;
    case 7: //julho
        printf("30 dias.\n");
        break;
    case 8: //agosto
        printf("31 dias.\n");
        break;
    case 9: //setembro
        printf("30 dias.\n");
        break;
    case 10: //outubro
        printf("31 dias.\n");
        break;
    case 11: //novembro
        printf("30 dias.\n");
        break;
    case 12: //dezembro
        printf("31 dias.\n");
        break;
    }
}

void Exercicio3Switch()
{
    int numero1, numero2;
    char operador;

    printf("Informe o primeiro numero: ");
    scanf("%d", &numero1);
    printf("Informe o segundo numero: ");
    scanf("%d", &numero2);
    fflush(stdin);
    printf("Informe a operacao: ");
    scanf("%c", &operador);

    switch(operador)
    {
    case '+':
        printf("A operacao eh soma.\n");
        printf("%d %c %d => os inteiros: %d e %d; a operacao: %c", numero1, operador, numero2, numero1, numero2, operador);
        break;
    case '-':
        printf("A operacao eh subtracao.\n");
        printf("%d %c %d => os inteiros: %d e %d; a operacao: %c", numero1, operador, numero2, numero1, numero2, operador);
        break;
    case '*':
    case 'x':
    case 'X':
        printf("A operacao eh multiplicacao.\n");
        printf("%d %c %d => os inteiros: %d e %d; a operacao: %c", numero1, operador, numero2, numero1, numero2, operador);
        break;
    case '/':
    case '\\':
    case ':':
        printf("A operacao eh divisao.\n");
        printf("%d %c %d => os inteiros: %d e %d; a operacao: %c", numero1, operador, numero2, numero1, numero2, operador);
        break;
    }
}

void ExercicioExtra()
{
    int x, y, valor;
    printf("Informe o valor: ");
    scanf("%d", &valor);

    for(y = 0 ; y <= valor ; y++) //numero de linhas do triangulo
    {
        for(x = 0 ; x < y ; x++) //controla as colunas
        {
            printf("* ");
        }
        //completou a linha
        printf("\n");
    }
}

void ExercicioExtra2()
{
    int i, valor;
    printf("Informe um valor (para interromper, digite -1): ");
    scanf("%d", &valor);

    while(valor != -1)
    {
        printf("O quadrado desse numero eh: %d.\n", valor * valor);

        printf("Informe um valor: ");
        scanf("%d", &valor);
    }
}

int main()
{
    //Exercicio1();
    //Exercicio2();
    //Exercicio3();
    //Exercicio4();
    //Exercicio5();
    //Exercicio1Switch();
    //Exercicio2Switch();
    //Exercicio3Switch();
    //ExercicioExtra();
    ExercicioExtra2();
}
