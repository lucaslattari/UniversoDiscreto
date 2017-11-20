#include <stdio.h>

void computaGame10(int posicoesJogo, int posDisco, int posNave)
{
    if(posNave > posDisco)
    {
        printf("%d", posicoesJogo - posNave + posDisco);
    }else
    {
        printf("%d", posDisco - posNave);
    }
}

int main()
{
    int n, d, a;

    scanf("%d %d %d", &n, &d, &a);
    computaGame10(n, d, a);
    return 0;
}
