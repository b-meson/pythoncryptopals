# Convert hex to base64
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

from binascii import unhexlify, b2a_base64
import base64


def main():
    test_hex_to_b64()


def hex_to_base64(i_s):
    encoded = base64.b64encode(unhexlify(i_s))
    return encoded


def test_hex_to_b64():
    input_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    returned_bytes = hex_to_base64(input_string)
    assert type(returned_bytes) is bytes
    passing_bytes = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert returned_bytes == passing_bytes


if __name__ == "__main__":
    main()




