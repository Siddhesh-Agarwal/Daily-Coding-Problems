"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

    ["the  quick brown", # 1 extra space on the left
    "fox  jumps  over", # 2 extra spaces distributed evenly
    "the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def justify_text(words, max_line_length):
    lines = []
    cum_len = -1
    curr_words = []
    line_lengths = []

    for word in words:
        if cum_len + (len(word) + 1) > max_line_length:
            lines.append(curr_words)
            line_lengths.append(cum_len)
            cum_len = -1
            curr_words = list()
        cum_len += len(word) + 1
        curr_words.append(word)

    if curr_words:
        lines.append(curr_words)
        line_lengths.append(cum_len)

    justified_lines = list()
    for words, length in zip(lines, line_lengths):
        spaces_to_add = max_line_length - length
        guaranteed_spaces = 1 + (spaces_to_add // (len(words) - 1))
        bonus_space_recipients = spaces_to_add % (len(words) - 1)
        line = ""

        for (index, word) in enumerate(words[:-1]):
            line += word
            line += " " * guaranteed_spaces
            if index < bonus_space_recipients:
                line += " "

        line += words[-1]
        justified_lines.append(line)

    return justified_lines
