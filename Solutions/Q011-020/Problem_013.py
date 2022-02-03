"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def CountCheck(temp: str, k: int):
    return True if len(set(temp)) == k else False


def LongestSubstring(s: str, k: int):
    sub = ""
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            temp = s[i:j]
            if CountCheck(temp, k):
                if len(temp) > len(sub):
                    sub = temp
    return sub


if __name__ == "__main__":
    S = input("Enter the main string: ")
    K = int(input("Enter length of substring: "))
    print(LongestSubstring(S, K))
