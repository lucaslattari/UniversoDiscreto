#include <stdio.h>

int main()
{
    int totalAlunos, totalMonitores;

    scanf("%d %d", &totalAlunos, &totalMonitores);

    if(totalAlunos + totalMonitores <= 50)
    {
        printf("S");
    }else
    {
        printf("N");
    }

    return 0;
}
