#include <stdio.h>

int main()
{
    /****CAPTURANDO AS INFORMAÇÕES DO PROBLEMA*****/
    int numberOfTestCases;
    scanf("%d", &numberOfTestCases);

    int i, maxIndex[100];
    for(i = 0 ; i < numberOfTestCases ; i++)
    {
        int sizeOfArray;
        scanf("%d", &sizeOfArray);

        int arrayOfProblem[1001] = {0}; //1 a 1000
        int j;
        for(j = 1 ; j <= sizeOfArray ; j++)
            scanf("%d", &arrayOfProblem[j]);

        /**********RESOLVENDO O PROBLEMA*********/
        int k;
        maxIndex[i] = 0;

        //percorrendo da direita para a esquerda
        for(j = 1 ; j <= sizeOfArray ; j++)
            for(k = sizeOfArray ; k > 0 ; k--)
            {
                if(arrayOfProblem[k] >= arrayOfProblem[j])
                    if(maxIndex[i] <= (k - j))
                    {
                        maxIndex[i] = k - j;
                    }else
                        break;
            }
    }

    for(i = 0 ; i < numberOfTestCases ; i++)
    {
        printf("%d\n", maxIndex[i]);
    }

    return 0;
}
