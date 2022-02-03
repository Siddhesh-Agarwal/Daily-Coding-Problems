"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def transform(close_bracket):
    transformed = []
    for i in close_bracket:
        if i == ")":
            transformed.append("(")
        if i == "}":
            transformed.append("{")
        if i == "]":
            transformed.append("")
    return transformed


def balanced(string: str):
    open_bracket = []
    close_bracket = []
    for i in string:
        if i in "{[(":
            open_bracket.append(i)
        else:
            close_bracket.append(i)
    if open_bracket[::-1] == transform(close_bracket):
        return True
    return False


if __name__ == "__main__":
    string = input()
    print(balanced(string))
