#include <stdio.h>
#include <string.h>

int resolveEscadinha(int tamanhoVetor, int* vetor)
{
    int totalDeEscadinhas = 0;
    int i, j;

    if(tamanhoVetor == 1)
        return 1;
    else if(tamanhoVetor > 1)
    {
        for(i = 0 ; i < tamanhoVetor - 1 ; i++)
        {
            int diferenca = vetor[i + 1] - vetor[i];
            for(j = i + 1 ; j < tamanhoVetor ; j++)
            {
                if(diferenca != (vetor[j + 1] - vetor[j]))
                    break;
            }
            totalDeEscadinhas++;
            i = j - 1;
        }

        return totalDeEscadinhas;
    }
}

int main()
{
    int vetor[1000];
    int tamanhoVetor;

    FILE* f = fopen("gabarito.txt", "r+");
    char nomeDoArquivoEntrada[100] = {0};
    char nomeDoArquivoSaida[100] = {0};
    while(fgetc(f) != EOF)
    {
        fscanf(f, "%s", nomeDoArquivoEntrada);
        printf("Abrindo arquivo: %s.....", nomeDoArquivoEntrada);
        if((unsigned)strlen(nomeDoArquivoEntrada) > 0)
        {
            fscanf(f, "%s", nomeDoArquivoSaida);

            FILE* ff = fopen(nomeDoArquivoEntrada, "r+");
            fscanf(ff, "%d", &tamanhoVetor);
            for(int i = 0 ; i < tamanhoVetor ; i++)
                fscanf(ff, "%d", &vetor[i]);
            fclose(ff);

            int resposta = resolveEscadinha(tamanhoVetor, vetor);

            ff = fopen(nomeDoArquivoSaida, "r+");
            int gabarito;
            fscanf(ff, "%d", &gabarito);

            if(gabarito == resposta)
                printf("OK!\n");
            else
                printf("ERROR!\n");

            fclose(ff);
        }
    }
    fclose(f);

    return 0;
}
