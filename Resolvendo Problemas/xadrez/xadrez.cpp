#include <stdio.h>
#include <string.h>

int resolveXadrez(int linhas, int colunas)
{
    //linha par e coluna par? branco!
    if((linhas % 2 == 0) && (colunas % 2 == 0))
        return 1;
    //linha impar e coluna impar? branco!
    else if((linhas % 2 != 0) && (colunas % 2 != 0))
        return 1;
    //qualquer coisa diferente é preto!
    else
        return 0;
}


int main()
{
    int linhas, colunas;

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
            fscanf(ff, "%d", &linhas);
            fscanf(ff, "%d", &colunas);

            int resposta = resolveXadrez(linhas, colunas);

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
