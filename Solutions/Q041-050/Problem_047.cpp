// This problem was asked by Facebook.

// Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

// For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

#include <iostream>
using namespace std;

int maxProfit(int arr[], int n) {
    int maxP = 0;
    for(int i=0; i<n; i++) {
        for(int j=i+1; j<n; j++) {
            maxP = max(maxP, arr[j] - arr[i]);
        }
    }
    return maxP;
}

int main() {
    int arr[] = {9, 11, 8, 5, 7, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << maxProfit(arr, n) << endl;
    return 0;
}