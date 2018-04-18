
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.


def xor_singlekey_singlebyte(input_b, single_key):
    bytes_out = bytearray()
    for x in input_b:
        bytes_out.append(x ^ single_key)
    try:
        return english_character_freq(bytes_out)
    except UnicodeDecodeError:
        pass


# operate on raw bytes, decode string, multiple the value, then rank.
def english_character_freq(decoded_bytes):
    english_map = {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92,
                   'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
                   'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07}
    weight = 0
    for b in decoded_bytes:
        s = chr(b)
        for key, value in english_map.items():
            key = key.lower()
            if key == s.lower():
                weight = weight + (value * .01)
    weight = weight * 100
    return weight

# The xor is against a single byte from 0 to 256, not a literal ascii "character"
def xor_singlekey_allpermuations(input_b):
    x = {}
    for i in range(256):
        returned_weight = xor_singlekey_singlebyte(input_b, i)
        x.update([(i, returned_weight)])
    print(x)
    return x


def test_xor_singlekey():
    input_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytes_input = bytes.fromhex(input_string)
    assert type(bytes_input) is bytes
    xor_return = xor_singlekey_allpermuations(bytes_input)
    assert type(xor_return) is bytes or bytearray


def main():
    test_xor_singlekey()


if __name__ == "__main__":
    main()
