#include <stdio.h>
#include <ctime>
#include <iostream>
#include <string.h>
#include <cstdlib>
#include <algorithm>

using namespace std;

void swapElementsInArray(int* arrayOfData, int indexOfFirstElement, int indexOfSecondElement)
{
    int temporary                       = arrayOfData[indexOfFirstElement];
    arrayOfData[indexOfFirstElement]    = arrayOfData[indexOfSecondElement];
    arrayOfData[indexOfSecondElement]   = temporary;
}

void selectionSort(int* arrayOfData, int sizeOfArray, int& totalOfIterations, int& totalOfSwaps)
{
    totalOfIterations  = 0;
    totalOfSwaps       = 0;

    for(int i = 0 ; i < sizeOfArray ; i++)
    {
        int minimumElementIndex = i;
        for(int j = i + 1 ; j < sizeOfArray ; j++)
            if(arrayOfData[j] < arrayOfData[minimumElementIndex])
                minimumElementIndex = j;
        swapElementsInArray(arrayOfData, i, minimumElementIndex);

        if(totalOfSwaps <= UINT_MAX)
            totalOfSwaps++;
        if(totalOfIterations <= UINT_MAX)
            totalOfIterations++;
    }
}

void mergeTwoArrays(int* arrayOfData, int lowerIndex, int midPointArrayIndex, int higherIndex, int* temporaryArray)
{
    //merge array[lowerIndex ... midpointArray] with array[midpointArrayIndex + 1 ... higherIndex]
    int indexForFirstPartOfArray    = lowerIndex;
    int indexForSecondPartOfArray   = midPointArrayIndex + 1;

    memset(temporaryArray, 0, sizeof(int) * (higherIndex - lowerIndex));
    for(int k = lowerIndex ; k <= higherIndex ; k++)
        temporaryArray[k - lowerIndex] = arrayOfData[k];

    for(int k = lowerIndex ; k <= higherIndex ; k++)
    {
        if(indexForFirstPartOfArray > midPointArrayIndex)
        {
            arrayOfData[k] = temporaryArray[indexForSecondPartOfArray - lowerIndex];
            indexForSecondPartOfArray++;
        }else if(indexForSecondPartOfArray > higherIndex)
        {
            arrayOfData[k] = temporaryArray[indexForFirstPartOfArray - lowerIndex];
            indexForFirstPartOfArray++;
        }else if(temporaryArray[indexForFirstPartOfArray - lowerIndex] < temporaryArray[indexForSecondPartOfArray - lowerIndex])
        {
            arrayOfData[k] = temporaryArray[indexForFirstPartOfArray - lowerIndex];
            indexForFirstPartOfArray++;
        }else
        {
            arrayOfData[k] = temporaryArray[indexForSecondPartOfArray - lowerIndex];
            indexForSecondPartOfArray++;
        }
    }
}

void mergeSort(int* arrayOfData, int lowerIndex, int higherIndex, int& totalOfMerges, int* temporaryArray)
{
    if(higherIndex <= lowerIndex)
        return;
    int midPointIndex = lowerIndex + (higherIndex - lowerIndex) / 2;
    mergeSort(arrayOfData, lowerIndex, midPointIndex, totalOfMerges, temporaryArray);
    mergeTwoArrays(arrayOfData, lowerIndex, midPointIndex, higherIndex, temporaryArray);
    mergeSort(arrayOfData, midPointIndex + 1, higherIndex, totalOfMerges, temporaryArray);

    if(totalOfMerges <= UINT_MAX)
        totalOfMerges++;
    if(totalOfMerges <= UINT_MAX)
        totalOfMerges++;
}

void fillArrayWithRandomNumbers(int* arrayOfData, int sizeOfArray, int maximumValueOfArray)
{
    srand((unsigned)time(nullptr));

    for(int i = 0 ; i < sizeOfArray ; i++)
    {
        int randomNumber = rand() % maximumValueOfArray;
        arrayOfData[i] = randomNumber;
    }
}

void analysisOfMergeSort(int* arrayOfData, int sizeOfArray, int& totalOfMerges)
{
    int* temporaryArray = new int[sizeOfArray];

    const clock_t beginClockTime    = clock();                     //contador de tempo inicial
    mergeSort(arrayOfData, 0, sizeOfArray - 1, totalOfMerges, temporaryArray);     //executa algoritmo mergesort
    const clock_t endClockTime      = clock();                     //contador de tempo final

    float totalTimeInSeconds        = float( endClockTime - beginClockTime ) /  CLOCKS_PER_SEC;

    cout << "Total of merges in MergeSort: " << totalOfMerges << endl;
    cout << "Total time in seconds: " << totalTimeInSeconds << endl;

    delete(temporaryArray);
}

void analysisOfSelectionSort(int* arrayOfData, int sizeOfArray, int& totalOfIterations, int& totalOfSwaps)
{
    const clock_t beginClockTime    = clock();                                 //contador de tempo inicial
    selectionSort(arrayOfData, sizeOfArray, totalOfIterations, totalOfSwaps);     //executa algoritmo selectionsort
    const clock_t endClockTime      = clock();                                 //contador de tempo final

    float totalTimeInSeconds        = float(endClockTime - beginClockTime) /  CLOCKS_PER_SEC;

    cout << "Total of iterations in SelectionSort: " << totalOfIterations << endl;
    cout << "Total of swaps in SelectionSort: " << totalOfSwaps << endl;
    cout << "Total time in seconds: " << totalTimeInSeconds << endl;
}

int main()
{
    int sizeOfArray                              = 100000;
    int totalOfIterations = 0;
    int totalOfSwaps = 0;
    int totalOfMerges = 0;
    int* arrayOfDataForSelectionSort                = new int[sizeOfArray];
    int* arrayOfDataForMergeSort                    = new int[sizeOfArray];

    fillArrayWithRandomNumbers(arrayOfDataForSelectionSort, sizeOfArray, 1000000);
    memcpy(arrayOfDataForMergeSort, arrayOfDataForSelectionSort, sizeof(int) * sizeOfArray);

    analysisOfSelectionSort(arrayOfDataForSelectionSort, sizeOfArray, totalOfIterations, totalOfSwaps);
    delete(arrayOfDataForSelectionSort);

    totalOfIterations = 0; totalOfSwaps = 0;
    analysisOfMergeSort(arrayOfDataForMergeSort, sizeOfArray, totalOfMerges);
    delete(arrayOfDataForMergeSort);
}
