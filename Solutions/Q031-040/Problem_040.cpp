// Given an array of integers where every integer occurs three times except for 
// one integer, which only occurs once, find and return the non-duplicated integer.

// For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], 
// return 19.

// Do this in O(N) time and O(1) space.
#include <iostream>
using namespace std;

int oddOneOut(int arr[], int size)
{
    int ones = 0, twos = 0;
    int common_bit_mask;

    for (int i = 0; i < size; i++)
    {
        twos = twos | (ones & arr[i]);
        ones = ones ^ arr[i];
        common_bit_mask = ~(ones & twos);
        ones &= common_bit_mask;
        twos &= common_bit_mask;
    }
    return ones;
}

int main() {
    // int n = sizeof(arr) / sizeof(arr[0]);
    // int arr[] = {6, 1, 3, 3, 3, 6, 6};
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    cout << oddOneOut(arr, n) << endl;
    return 0;
}