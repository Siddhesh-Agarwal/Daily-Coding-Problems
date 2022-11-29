// Given a string, find the palindrome that can be made by inserting the fewest
// number of characters as possible anywhere in the word. If there is more than one
// palindrome of minimum length that can be made, return the lexicographically
// earliest one (the first one alphabetically).

// For example, given the string "race", you should return "ecarace", since we can
// add three letters to it (which is the smallest amount to make a palindrome).
// There are seven other palindromes that can be made from "race" by adding three
// letters, but "ecarace" comes first alphabetically.

#include <bits/stdc++.h>
using namespace std;

int findMinInsertions(char str[], int l, int h)
{
    if (l > h)
        return INT_MAX;
    if (l == h)
        return 0;
    if (l == h - 1)
        return (str[l] == str[h]) ? 0 : 1;
    return (str[l] == str[h]) ? findMinInsertions(str, l + 1, h - 1) : (min(findMinInsertions(str, l, h - 1), findMinInsertions(str, l + 1, h)) + 1);
}

int main()

{
    string s;
    cin >> s;
    cout << findMinInsertions((char *)s.c_str(), 0, s.length() - 1);
    return 0;
}