'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

# This function will decode an encoded string
def RunLengthDecode(encoded):
    decoded = ""
    stored = 0
    for index, i in enumerate(encoded):
        if i.isalpha():
            num = encoded[stored:index]
            stored = index + 1
            decoded += i * int(num)
    return decoded

# This function will encode a decoded string
def RunLengthEncode(decoded):
    char = decoded[0]
    counter = 0
    encoded = ""
    for i in decoded:
        if i == char:
            counter += 1
        else:
            encoded = encoded + str(counter) + char
            char = i
            counter = 1
    encoded = encoded + str(counter) + char
    return encoded
