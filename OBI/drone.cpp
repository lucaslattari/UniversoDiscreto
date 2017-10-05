#include <stdio.h>

int main()
{
    int larguraDrone, alturaDrone, profDrone;
    int larguraJanela, alturaJanela;

    scanf("%d %d %d", &larguraDrone, &alturaDrone, &profDrone);
    scanf("%d %d", &larguraJanela, &alturaJanela);

    if(larguraDrone <= larguraJanela &&
       alturaDrone <= alturaJanela)
        printf("S");
    else
    if (larguraDrone <= alturaJanela &&
        alturaDrone <= larguraJanela)
        printf("S");
    else
    if (alturaDrone <= alturaJanela &&
        profDrone <= larguraJanela)
        printf("S");
    else
    if(profDrone <= alturaJanela &&
       alturaDrone <= larguraJanela)
        printf("S");
    else
    if(larguraDrone <= larguraJanela &&
       profDrone <= alturaJanela)
        printf("S");
    else
    if(profDrone <= larguraJanela &&
       larguraDrone <= alturaJanela)
        printf("S");
    else
        printf("N");

    return 0;
}
