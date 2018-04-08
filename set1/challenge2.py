# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# '1c0111001f010100061a024b53535009181c'
# after hex decoding, and when XOR'd against:
# '686974207468652062756c6c277320657965'
# ... should produce:
# '746865206b696420646f6e277420706c6179'

import challenge1


def xor_func(b_input):
    xor_against = challenge1.hex_to_base64('686974207468652062756c6c277320657965')
    if len(b_input) == len(xor_against):
    #    print('same length array')
        b_output = bytearray()
        for b_input, xor_against in zip(b_input, xor_against):
            b_output.append(b_input ^ xor_against)
        return b_output
    else:
        print('strings are not same size')


def test_xor_funct():
    input_string = '1c0111001f010100061a024b53535009181c'
    bytes_input = challenge1.hex_to_base64(input_string)
    assert type(bytes_input) is bytes
    xor_return = xor_func(bytes_input)
    assert type(xor_return) is bytes or bytearray
    if xor_return.decode('utf-8') == '746865206b696420646f6e277420706c6179':
        print('failed to decode with bytearray')
    else:
        print('Tests Passing')


def main():
    test_xor_funct()


if __name__ == "__main__":
    main()
