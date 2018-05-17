#include <stdio.h>

#define BRANCO 0
#define PRETO 1

int main()
{
    int tamanhoLinhaColuna;
    scanf("%d", &tamanhoLinhaColuna);

    int matriz[100][100];

    int x, y;
    for(x = 0 ; x < tamanhoLinhaColuna ; x++)
        for(y = 0 ; y < tamanhoLinhaColuna ; y++)
            scanf("%d", &matriz[x][y]);

    for(x = 1 ; x < tamanhoLinhaColuna ; x++)
        for(y = 1 ; y < tamanhoLinhaColuna ; y++)
            if(matriz[x - 1][y - 1] == BRANCO)
            {
                if(matriz[x - 1][y] == BRANCO)
                {
                    matriz[x][y] = PRETO;
                }else if(matriz[x - 1][y] == PRETO)
                {
                    if(matriz[x][y - 1] == BRANCO)
                        matriz[x][y] = PRETO;
                    else if(matriz[x][y - 1] == PRETO)
                        matriz[x][y] = BRANCO;
                }
            }else if(matriz[x - 1][y - 1] == PRETO)
            {
                if(matriz[x - 1][y] == PRETO)
                {
                    matriz[x][y] = BRANCO;
                }else if(matriz[x - 1][y] == BRANCO)
                {
                    if(matriz[x][y - 1] == BRANCO)
                    {
                        matriz[x][y] = PRETO;
                    }else if(matriz[x][y - 1] == PRETO)
                    {
                        matriz[x][y] = BRANCO;
                    }
                }
            }

    printf("%d", matriz[tamanhoLinhaColuna - 1][tamanhoLinhaColuna - 1]);

    return 0;
}
