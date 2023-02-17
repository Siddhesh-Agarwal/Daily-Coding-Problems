// This problem was asked by Amazon.

// Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

// For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

#include <iostream>
using namespace std;

string largestPalindromicSubstring(string s)
{
    string lps = "";
    int n = s.length();
    int start = 0;
    int maxLength = 1;
    bool table[n][n];
    for (int i = 0; i < n; i++)
    {
        table[i][i] = true;
    }
    for (int i = 0; i < n - 1; i++)
    {
        if (s[i] == s[i + 1])
        {
            table[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }
    }
    for (int k = 3; k <= n; k++)
    {
        for (int i = 0; i < n - k + 1; i++)
        {
            int j = i + k - 1;
            if (table[i + 1][j - 1] && s[i] == s[j])
            {
                table[i][j] = true;
                if (k > maxLength)
                {
                    start = i;
                    maxLength = k;
                }
            }
        }
    }
    for (int i = start; i <= start + maxLength - 1; i++)
    {
        lps += s[i];
    }
    return lps;
}

int main()
{
    string s1 = "aabcdcb";
    string s2 = "bananas";

    cout << largestPalindromicSubstring(s1) << endl;
    cout << largestPalindromicSubstring(s2) << endl;
}