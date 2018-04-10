
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

import string
import challenge1
import challenge2


def xor_singlekey(input_b):
    char_set = string.printable
    b_array = bytearray(char_set, 'utf-8')
    bytes_output = bytearray()
    for b in b_array:
        bytes_output = bytearray()
        for x in input_b:
            bytes_output.append(x ^ b)
        s_plaintext = bytes_output.decode('utf-8')
        print(bytes_output)


def test_xor_singlekey():
    input_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytes_input = challenge1.hex_to_base64(input_string)
    assert type(bytes_input) is bytes
    xor_return = xor_singlekey(bytes_input)
    assert type(xor_return) is bytes or bytearray


def main():
    test_xor_singlekey()

if __name__ == "__main__":
    main()
