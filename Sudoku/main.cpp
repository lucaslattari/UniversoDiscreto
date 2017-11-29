#include <stdio.h>
#include <stdlib.h>
#include <time.h>

bool naoHaViolacao(int valorInserido, int posicao, int* vetor)
{
    //0 a gente ignora
    if(valorInserido == 0)
        return true;

    //printf("Tentativa a ser inserida: %d\n", valorInserido);
    //getchar();

    //checa linha
    int linha = posicao / 9;
    for(int i = linha * 9 ; i < linha * 9 + 9 ; i++)
    {
        if(vetor[i] == valorInserido)
        {
            //printf("VIOLACAO DE LINHA: posicao %d.\n", i);
            //getchar();
            return false;
        }
    }

    //checa coluna
    int coluna = posicao % 9;
    for(int i = coluna % 9 ; i <= 8 * 9 + coluna % 9 ; i+=9)
    {
        if(vetor[i] == valorInserido)
        {
            //printf("VIOLACAO DE COLUNA: posicao %d.\n", i);
            //getchar();
            return false;
        }
    }

    //checa submatriz
    int submatrizX, submatrizY;
    if(linha < 3)
        submatrizY = 0;
    else if(linha >= 3 && linha < 6)
        submatrizY = 1;
    else if(linha >= 6)
        submatrizY = 2;

    if(coluna < 3)
        submatrizX = 0;
    else if(coluna >= 3 && coluna < 6)
        submatrizX = 1;
    else if(coluna >= 6)
        submatrizX = 2;

    for(int y = 0 ; y < 3 ; y++)
        for(int x = 0 ; x < 3 ; x++)
        {
            int pos = (x + submatrizX * 3) + ((y * 9) + (submatrizY * 9 * 3));
            if(vetor[pos] == valorInserido)
            {
                //printf("VIOLACAO DE SUBMATRIZ: posicao %d.\n", pos);
                //getchar();
                return false;
            }
        }
    return true;
}

bool verificaSeTerminou(int* vetor)
{
    for(int i = 0 ; i < 81 ; i++)
        if(vetor[i] == 0)
            return false;
    return true;
}

void imprimeVetor(int* vetor)
{
    for(int linha = 0 ; linha < 9 ; linha++)
    {
        for(int coluna = 0 ; coluna < 9 ; coluna++)
            printf("%d ", vetor[linha * 9 + coluna]);
        printf("\n");
    }
}

void realizaBackTracking(int* vetorSudoku, bool* posicaoPreenchida, int posicao);

void computaSudoku(int* vetorSudoku, bool* posicaoPreenchida, int posicao)
{
    //printf("Agora estou na posicao: %d\n", posicao);
    //getchar();

    while(posicaoPreenchida[posicao] == true)
        posicao++;

    //printf("Agora estou na posicao: %d\n", posicao);
    //getchar();

    int tentativa = vetorSudoku[posicao] + 1;
    if(tentativa > 9)
    {
        realizaBackTracking(vetorSudoku, posicaoPreenchida, posicao);
        tentativa = 1;
    }

    while(!naoHaViolacao(tentativa, posicao, vetorSudoku))
    {
        tentativa++;
        if(tentativa > 9)
        {
            realizaBackTracking(vetorSudoku, posicaoPreenchida, posicao);
            tentativa = 1;
        }
    }

    vetorSudoku[posicao] = tentativa;

    //printf("Beleza, inseri.\n");
    //getchar();
    if(verificaSeTerminou(vetorSudoku))
    {
        printf("Resolucao Final: \n");
        imprimeVetor(vetorSudoku);
        exit(0);
    }
    //imprimeVetor(vetorSudoku);
    //getchar();
    computaSudoku(vetorSudoku, posicaoPreenchida, posicao + 1);
}

void realizaBackTracking(int* vetorSudoku, bool* posicaoPreenchida, int posicao)
{
    vetorSudoku[posicao] = 0;
    posicao--;
    while(posicaoPreenchida[posicao] == true)
        posicao--;
    //printf("Precisei fazer backtracking pra posicao %d\n", posicao);
    //getchar();
    computaSudoku(vetorSudoku, posicaoPreenchida, posicao);
}

int main()
{
    int vetorSudoku[81]         = {0};
    bool posicaoPreenchida[81]  = {false};

    //posicoes preenchidas conforme o enade
    vetorSudoku[0] = 5; posicaoPreenchida[0] = true;
    vetorSudoku[1] = 3; posicaoPreenchida[1] = true;
    vetorSudoku[4] = 7; posicaoPreenchida[4] = true;

    vetorSudoku[9] = 6; posicaoPreenchida[9] = true;
    vetorSudoku[12] = 1; posicaoPreenchida[12] = true;
    vetorSudoku[13] = 9; posicaoPreenchida[13] = true;
    vetorSudoku[14] = 5; posicaoPreenchida[14] = true;

    vetorSudoku[19] = 9; posicaoPreenchida[19] = true;
    vetorSudoku[20] = 8; posicaoPreenchida[20] = true;
    vetorSudoku[25] = 6; posicaoPreenchida[25] = true;

    vetorSudoku[27] = 8; posicaoPreenchida[27] = true;
    vetorSudoku[31] = 6; posicaoPreenchida[31] = true;
    vetorSudoku[35] = 3; posicaoPreenchida[35] = true;

    vetorSudoku[36] = 4; posicaoPreenchida[36] = true;
    vetorSudoku[39] = 8; posicaoPreenchida[39] = true;
    vetorSudoku[41] = 3; posicaoPreenchida[41] = true;
    vetorSudoku[44] = 1; posicaoPreenchida[44] = true;

    vetorSudoku[45] = 7; posicaoPreenchida[45] = true;
    vetorSudoku[49] = 2; posicaoPreenchida[49] = true;
    vetorSudoku[53] = 6; posicaoPreenchida[53] = true;

    vetorSudoku[55] = 6; posicaoPreenchida[55] = true;
    vetorSudoku[60] = 2; posicaoPreenchida[60] = true;
    vetorSudoku[61] = 8; posicaoPreenchida[61] = true;

    vetorSudoku[66] = 4; posicaoPreenchida[66] = true;
    vetorSudoku[67] = 1; posicaoPreenchida[67] = true;
    vetorSudoku[68] = 9; posicaoPreenchida[68] = true;
    vetorSudoku[71] = 5; posicaoPreenchida[71] = true;

    vetorSudoku[76] = 8; posicaoPreenchida[76] = true;
    vetorSudoku[79] = 7; posicaoPreenchida[79] = true;
    vetorSudoku[80] = 9; posicaoPreenchida[80] = true;

    printf("Tabuleiro inicial: \n");
    imprimeVetor(vetorSudoku);
    printf("\n\n");
    computaSudoku(vetorSudoku, posicaoPreenchida, 0);

    return 0;
}
