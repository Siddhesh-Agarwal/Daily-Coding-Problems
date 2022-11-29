// Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

// Do this in linear time and in-place.

// For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

#include <bits/stdc++.h>
using namespace std;

void swap(char *a, char *b)
{
    char temp = *a;
    *a = *b;
    *b = temp;
}

void sortRGB(char arr[], int n)
{
    int low = 0, mid = 0, high = n - 1;
    while (mid <= high)
    {
        switch (arr[mid])
        {
        case 'R':
            swap(&arr[low++], &arr[mid++]);
            break;
        case 'G':
            mid++;
            break;
        case 'B':
            swap(&arr[mid], &arr[high--]);
            break;
        }
    }
}

int main()
{
    char arr[] = {'G', 'B', 'R', 'R', 'B', 'R', 'G'};
    int n = sizeof(arr) / sizeof(arr[0]);
    sortRGB(arr, n);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}