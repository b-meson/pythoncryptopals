## Fixed XOR
## Write a function that takes two equal-length buffers and produces their XOR combination.
## If your function works properly, then when you feed it the string:
## '1c0111001f010100061a024b53535009181c'
## after hex decoding, and when XOR'd against:
## '686974207468652062756c6c277320657965'
## ... should produce:
## '746865206b696420646f6e277420706c6179'
import pdb
import binascii
import base64
from binascii import unhexlify, b2a_base64

def xorg_func(input_s,xor_a,check):
    h_input = bytearray.fromhex(input_s)
    h_xor = bytearray.fromhex(xor_a)
    cipher_text=bytearray(h_input^h_xor for h_input,h_xor in zip(h_input,h_xor))
    if (len(h_input)==len(h_xor)):
        print('same length array')
    h_input = bytearray(cipher_text).hex()
    if check == h_input:
        print(check)
        print('PASSING')
    else:
        print('wrong_result')

def main():
    input_string='1c0111001f010100061a024b53535009181c'
    xor_against = '686974207468652062756c6c277320657965'
    check='746865206b696420646f6e277420706c6179'
    xorg_func(input_string,xor_against,check)

if __name__ == "__main__":
    main()
