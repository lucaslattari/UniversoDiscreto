#include <stdio.h>

int main()
{
    /******* CAPTURAR OS ELEMENTOS DO PROBLEMA********/
    int numberOfTestCases;
    scanf("%d", &numberOfTestCases);

    int i;
    int beginInterval[100] = {0}, endInterval[100] = {0};
    int sumNotFound[100] = {0};
    for (i = 0 ; i < numberOfTestCases ; i++)
    {
        int sizeOfArray, sum;
        scanf("%d %d", &sizeOfArray, &sum);

        int j;
        int arrayOfProblem[101] = {0}; //0 a 100
        for(j = 1 ; j <= sizeOfArray ; j++)
        {
            scanf("%d", &arrayOfProblem[j]);
        }

        int auxSum = arrayOfProblem[1];
        beginInterval[i] = 1;
        endInterval[i] = 1;
        sumNotFound[i] = 0;
        for(j = 1 ; j <= sizeOfArray ; j++)
        {
            if(auxSum < sum)
            {
                endInterval[i]++;
                auxSum += arrayOfProblem[endInterval[i]];
            }else if(auxSum > sum)
            {
                auxSum -= arrayOfProblem[beginInterval[i]];
                beginInterval[i]++;
                j--;
            }else if(auxSum == sum)
            {
                //note que nesse instante, tanto o beginInterval quanto
                //o endInterval já recebeu os valores finais!
                break;
            }

            if(endInterval[i] > sizeOfArray)
            {
                //não existe soma naquele vetor
                sumNotFound[i] = 1;
                break;
            }
        }
    }

    for(i = 0 ; i < numberOfTestCases ; i++)
    {
        if(sumNotFound[i] == 1)
        {
            printf("-1\n");
        }else
        {
            printf("%d %d\n", beginInterval[i], endInterval[i]);
        }
    }

    return 0;
}
