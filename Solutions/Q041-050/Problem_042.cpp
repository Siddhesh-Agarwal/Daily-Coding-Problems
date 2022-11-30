// Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
// If such a subset cannot be made, then return null.

// Integers can appear more than once in the list. You may assume all numbers in the list are positive.

// For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
#include <iostream>
using namespace std;

void solution(int arr[], int n, int k)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
    }
    if (sum < k)
    {
        cout << "No solution" << endl;
        return;
    }
    int temp = 0;
    for (int i = 0; i < n; i++)
    {
        temp += arr[i];
        if (temp == k)
        {
            for (int j = 0; j <= i; j++)
            {
                cout << arr[j] << " ";
            }
            cout << endl;
            return;
        }
        if (temp > k)
        {
            temp = 0;
            i--;
        }
    }
}

int main()
{
    int n, k;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    cin >> k;
    solution(arr, n, k);
    return 0;
};
