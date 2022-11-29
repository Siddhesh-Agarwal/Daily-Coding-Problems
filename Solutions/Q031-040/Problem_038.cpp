// You have an N by N board. Write a function that, given N, returns the number 
// of possible arrangements of the board where N queens can be placed on the 
// board without threatening each other, i.e. no two queens share the same row, 
// column, or diagonal.

#include <bits/stdc++.h>
using namespace std;

bool isSafe(int board[][10], int i, int j, int n)
{
    // You can check for col
    for (int row = 0; row < i; row++)
    {
        if (board[row][j] == 1)
            return false;
    }
    // Check for left diagonal
    int x = i;
    int y = j;
    while (x >= 0 && y >= 0)
    {
        if (board[x][y] == 1)
            return false;
        x--;
        y--;
    }
    // Check for right diagonal
    x = i;
    y = j;
    while (x >= 0 && y < n)
    {
        if (board[x][y] == 1)
            return false;
        x--;
        y++;
    }
    // The position is now safe, return true
    return true;
}

bool solveNQueen(int board[][10], int i, int n)
{
    // Base case
    if (i == n)
    {
        // You have successfully placed queens in n rows (0...n-1)
        // Print the board
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == 1)
                    cout << "Q ";
                else
                    cout << "_ ";
            }
            cout << endl;
        }
        cout << endl;
        return false;
    }
    // Recursive case
    // Try to place the queen in the current row and call on the remaining part which will be solved by recursion
    for (int j = 0; j < n; j++)
    {
        // I have to check if i,j th position is safe to place the queen or not
        if (isSafe(board, i, j, n))
        {
            // Place the queen - assuming i,j is the right position
            board[i][j] = 1;
            bool nextQueen = solveNQueen(board, i + 1, n);
            if (nextQueen)
                return true;
            // Means i,j is not the right position - Assumption is wrong
            board[i][j] = 0; // Backtrack
        }
    }
    // You have tried for all positions in the current row but could not place a queen
    return false;
}

int main()
{
    int n;
    cin >> n;
    int board[10][10] = {0};
    solveNQueen(board, 0, n);
    return 0;
}
