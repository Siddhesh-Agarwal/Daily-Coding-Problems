/*
The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other. For example, the
edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute
the “e” for “i”, and append a “g”.
*/

#include <iostream>
#include <vector>
using namespace std;

int minEditDist(string A, string B, int m, int n, vector<vector<int>> &T)
{
    if (m == 0 || n == 0)
        return max(m, n);
    if (T[m][n] != -1)
        return T[m][n];
    if (A[m - 1] == B[n - 1])
        return T[m][n] = minEditDist(A, B, m - 1, n - 1, T);
    return T[m][n] = 1 + min(minEditDist(A, B, m - 1, n, T), min(minEditDist(A, B, m, n - 1, T), minEditDist(A, B, m - 1, n - 1, T)));
}

int main()
{
    string A = "kitten", B = "sitting";
    vector<vector<int>> T(A.length() + 1, vector<int>(B.length() + 1, -1));
    cout << minEditDist(A, B, A.length(), B.length(), T) << endl;
    return 0;
}