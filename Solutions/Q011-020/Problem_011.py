"""
Implement an autocomplete system. That is, given a query string s
and a set of all possible query strings, return all strings in the set that
have s as a prefix.

For example, given the query string de and the set of strings [dog,
deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries.
"""


def autocomplete(query_string: str, query_list: list):
    n = len(query_string)
    return [i for i in query_list if i[:n] == query_string]


if __name__ == "__main__":
    query_string = input("Enter the query string: ")
    query_list = eval(input("Enter the list of strings: "))
    print(autocomplete(query_string, query_list))
