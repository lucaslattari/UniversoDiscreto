#include <stdio.h>

int main()
{
    int carta1, carta2, carta3;

    scanf("%d %d %d", &carta1, &carta2, &carta3);

    if(carta1 == carta2)
    {
        printf("%d", carta3);
    }else if(carta1 == carta3)
    {
        printf("%d", carta2);
    }else if(carta2 == carta3)
    {
        printf("%d", carta1);
    }

    return 0;
}
