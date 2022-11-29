// Suppose you are given a table of currency exchange rates, represented as a 2D
// array Determine whether there is a possible arbitrage: that is, whether there
// is some sequence of trades you can make, starting with some amount A of any 
// currency, so that you can end up with some amount greater than A of that currency.

#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(n^3)
// Space complexity: O(n^2)
int main() {
    int n;
    cin >> n;
    vector<vector<double>> rates(n, vector<double>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> rates[i][j];

    vector<vector<double>> dp(n, vector<double>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dp[i][j] = rates[i][j];

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dp[i][j] = max(dp[i][j], dp[i][k] * dp[k][j]);

    for (int i = 0; i < n; i++)
        if (dp[i][i] > 1.0) {
            cout << "Arbitrage is possible" << endl;
            return 0;
        }

    cout << "Arbitrage is not possible" << endl;
    return 0;
}
