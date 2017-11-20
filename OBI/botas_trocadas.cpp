#include <stdio.h>

#define MAXIMO_DE_BOTAS 10000
#define TAMANHOS_DE_PE  61

typedef struct TipoBota
{
    int     tamanho;
    char    lado;
};

int main()
{
    int N;
    TipoBota vetorBotas[MAXIMO_DE_BOTAS];

    //capturando os dados das botas
    scanf("%d", &N);
    for(int i = 0 ; i < N ; i++)
    {
        scanf("%d %c", &vetorBotas[i].tamanho,
              &vetorBotas[i].lado);
    }

    //ordenando as botas
    for(int i = 0 ; i < N ; i++)
    {
        for(int j = i + 1 ; j < N ; j++)
        {
            if(vetorBotas[i].tamanho >
                vetorBotas[j].tamanho)
            {
                TipoBota aux;
                aux.tamanho = vetorBotas[i].tamanho;
                aux.lado    = vetorBotas[i].lado;

                vetorBotas[i].tamanho   = vetorBotas[j].tamanho;
                vetorBotas[i].lado      = vetorBotas[j].lado;

                vetorBotas[j].tamanho   = aux.tamanho;
                vetorBotas[j].lado      = aux.lado;
            }
        }
    }

    //anotando cada bota que temos
    int botasQueTemDoPeEsquerdo[TAMANHOS_DE_PE] = { 0 };
    int botasQueTemDoPeDireito[TAMANHOS_DE_PE] = { 0 };

    for(int i = 0 ; i < N ; i++)
    {
        int tamanhoDoPeAnalisado    = vetorBotas[i].tamanho;
        int ladoDoPeAnalisado       = vetorBotas[i].lado;

        if(ladoDoPeAnalisado == 'e' || ladoDoPeAnalisado == 'E')
        {
            botasQueTemDoPeEsquerdo[tamanhoDoPeAnalisado]++;
        }else if(ladoDoPeAnalisado == 'd' || ladoDoPeAnalisado == 'D')
        {
            botasQueTemDoPeDireito[tamanhoDoPeAnalisado]++;
        }
    }

    //conta os pares de botas
    int totalDePares = 0;
    for(int i = 30 ; i <= 60 ; i++)
    {
        if(botasQueTemDoPeEsquerdo[i] == botasQueTemDoPeDireito[i])
        {
            totalDePares += botasQueTemDoPeEsquerdo[i];
        }else if(botasQueTemDoPeEsquerdo[i] < botasQueTemDoPeDireito[i])
        {
            totalDePares += botasQueTemDoPeEsquerdo[i];
        }else
            totalDePares += botasQueTemDoPeDireito[i];
    }

    printf("%d", totalDePares);

    return 0;
}
