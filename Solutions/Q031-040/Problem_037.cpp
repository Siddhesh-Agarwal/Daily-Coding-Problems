// The power set of a set is the set of all its subsets. Write a function that, 
// given a set, generates its power set.

// For example, given the set {1, 2, 3}, 
// it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

// You may also use a list or array to represent a set.

#include <bits/stdc++.h>
using namespace std;

void printPowerSet(int arr[], int n)
{
    unsigned int powSize = pow(2, n);
    int counter, j;
    for (counter = 0; counter < powSize; counter++)
    {
        for (j = 0; j < n; j++)
        {
            if (counter & (1 << j))
                cout << arr[j] << " ";
        }
        cout << "\n";
    }
    return;
}

int main()
{
    int arr[] = {1, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    printPowerSet(arr, n);
    return 0;
}