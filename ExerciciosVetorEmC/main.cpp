#include <stdio.h>

void Exercicio1()
{
    int vetor[10];
    int i;

    for(i = 0 ; i < 10 ; i++)
    {
        printf("Informe o valor da posicao %i do vetor: ", i);
        scanf("%i", &vetor[i]);
    }

    for(i = 0 ; i < 10 ; i+=2)
    {
        printf("%d - ", vetor[i]);
    }
}

void Exercicio2(){
    int vetor[15];
    int i;

    for(i = 0 ; i < 15 ; i++)
    {
        vetor[i] = (i + 1) * 3;
    }

    for(i = 0 ; i < 15 ; i++)
    {
        printf("%d %d\n", i, vetor[i]);
    }
}

void Exercicio3()
{
    int vetor[5];
    int i;
    int tamanhoDoVetor = 20;
    for(i = 0 ; i < tamanhoDoVetor ; i++)
    {
        printf("Informe o valor da posicao %i do vetor: ", i);
        scanf("%i", &vetor[i]);
    }

    int indice;
    printf("Informe um indice a ser consultado: ");
    scanf("%i", &indice);

    while((indice >= 0) && (indice < tamanhoDoVetor))
    {
        printf("O valor daquela posicao eh %d.", vetor[indice]);

        printf("Informe um indice a ser consultado: ");
        scanf("%i", &indice);
    }

    int valorBuscado;
    printf("Informe um valor a ser buscado no vetor: ");
    scanf("%i", &valorBuscado);

    int achouValor = 0;
    int contaValores = 0;
    for(i = 0 ; i < tamanhoDoVetor ; i++)
    {
        if(valorBuscado == vetor[i])
        {
            achouValor = 1;
            contaValores = contaValores + 1;
        }
    }

    if(achouValor == 0)
    {
        printf("O valor nao existe no vetor.\n");
    }else if(achouValor == 1)
    {
        printf("O valor existe no vetor.\n");
        printf("O valor aparece %i vezes.\n", contaValores);
    }
}

void ExercicioDesafio1(){
    int vetor[16];
    int i;
    for(i = 0 ; i < 16 ; i++)
    {
        printf("Informe um valor para o indice i do vetor: ", i);
        scanf("%d", &vetor[i]);
    }

    int aux;
    for(i = 0 ; i < 8 ; i++)
    {
        aux = vetor[i];
        vetor[i] = vetor[i + 8];
        vetor[i + 8] = aux;
    }

    for(i = 0 ; i < 16 ; i++)
    {
        printf("%d - ", vetor[i]);
    }
}

void ExercicioDesafio2(){
    float media[3] = {0}, valorLido;
    int i;
    for(i = 0 ; i < 5 ; i++)
    {
        printf("Informe o valor: ");
        scanf("%f", &valorLido);

        media[0] += valorLido;
    }

    for(i = 0 ; i < 5 ; i++)
    {
        printf("Informe o valor: ");
        scanf("%f", &valorLido);

        media[1] += valorLido;
    }

    for(i = 0 ; i < 5 ; i++)
    {
        printf("Informe o valor: ");
        scanf("%f", &valorLido);

        media[2] += valorLido;
    }

    printf("A media 1 eh: %f.", media[0] / 5);
    printf("A media 2 eh: %f.", media[1] / 5);
    printf("A media 3 eh: %f.", media[2] / 5);
}

void ExercicioDesafio3(){
    int original[100]   = {0};
    int pares[100]      = {0};
    int impares[100]    = {0};

    int i;
    for(i = 0 ; i < 100 ; i++)
    {
        original[i] = i;
    }

    int contadorPares = 0;
    int contadorImpares = 0;

    for(i = 0 ; i < 100 ; i++)
    {
        if(original[i] % 2 == 0)
        {
            pares[contadorPares] = original[i];
            contadorPares++;
        }else{
            impares[contadorImpares] = original[i];
            contadorImpares++;
        }
    }
}

void ExercicioDesafio4(){
    int vetor[20];
    int i;
    for(i = 0 ; i < 20 ; i++)
    {
        printf("Informe o valor da posicao %d:", i);
        scanf("%d", &vetor[i]);
    }

    int aux;
    for(i = 0 ; i < 10 ; i++)
    {
        aux = vetor[i];
        vetor[i] = vetor[19 - i];
        vetor[19 - i] = aux;
    }

    for(i = 0 ; i < 20 ; i++)
    {
        printf("%d - ", vetor[i]);
    }

}

int main(){
    ExercicioDesafio4();
    return 0;
}
