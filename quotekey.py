#!/usr/local/bin/python

import argparse
import gmpy2
import os
import random
import re
import subprocess

from Crypto.PublicKey import RSA

# https://twitter.com/SwiftOnSecurity/status/717575221759205376
DEFAULT_MESSAGE = """
Data at rest encryption is like if someone told you their car was perfectly safe because it didn't have wheels.
"""

def highlight_print(message, payload):
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    GREEN = '\033[92m'
    CLEAR = '\033[0m'

    start_hl = message.find(payload)
    end_hl = start_hl + len(payload)
    print message[:start_hl] + GREEN + payload + CLEAR + message[end_hl:]

def clean_payload(message):
    """
    Remove invalid base 64 characters
    """
    return re.sub('[^a-zA-Z0-9+/]', '', message.title())

def splice(source, index, payload):
    """
    Splices payload into a string at a given location
    """
    return source[:index] + payload + source[index+len(payload):]

def mpz_to_base64(n):
    # This dance packs an mpz into a variable length byte array and encodes it to base64
    encoded_modulus = '00' + hex(long(n))[2:-1]
    if len(encoded_modulus) % 2:
        encoded_modulus = '0' + encoded_modulus
    encoded_modulus = encoded_modulus.decode('hex').encode('base64')
    return encoded_modulus.replace('\n', '')

def base64_to_long(encoded_message):
    return long(encoded_message.decode('base64').encode('hex'), 16)

def build_keys(N, p, q, key_file):
    e = 65537L
    d = long(gmpy2.invert(e,(p-1)*(q-1)))
    key = RSA.construct((long(N), e, d))

    with open(key_file, 'w') as w:
        w.write(key.exportKey())
    os.chmod(key_file, 0o600)

    return subprocess.check_output(['ssh-keygen', '-y', '-f', key_file])

def parse_args():
    parser = argparse.ArgumentParser(description='Generate boutique SSH keys.\n\n This script embeds a string of your choice into the modulus of a freshly generated SSH key pair.')
    parser.add_argument('--message', nargs='?', default=DEFAULT_MESSAGE,
                       help='Statement you would like your authorized_keys to make')
    parser.add_argument('--key_file', nargs='?', default='test.id_rsa',
                       help='Location to write SSH private key file')
    parser.add_argument('--key_strength_bytes', nargs='?', type=int, default=512,
                       help='Desired length of modulus in bytes')
    return parser.parse_args()

def main():
    args = parse_args()

    prime_length_bits = args.key_strength_bytes * 4
    p = gmpy2.next_prime((1<<prime_length_bits) + random.getrandbits(prime_length_bits))
    q = gmpy2.mpz((1<<prime_length_bits) + random.getrandbits(prime_length_bits))

    N = p*q

    # Now try to find qs that give us a modulus with the payload somewhere in the middle
    encoded_modulus = mpz_to_base64(N)
    payload = clean_payload(args.message)
    start_index = len(encoded_modulus)//2 - len(payload) + 10 # Magic number. Reduce if having a bad day.
    success = False

    while not success:
        # Splice payload into the initial modulus
        approx_modulus = base64_to_long(splice(encoded_modulus, start_index, payload))

        # Find the next value of q that is prime
        start_q = gmpy2.mpz(approx_modulus)/p
        next_q = gmpy2.next_prime(start_q)
        candidate_modulus = next_q * p

        # Check if the payload is preserved
        if payload in mpz_to_base64(candidate_modulus):
            print 'Success! Writing private key to {}'.format(args.key_file)
            print 'Your authorized_keys entry is below:'
            authorized_key = build_keys(candidate_modulus, p, next_q, args.key_file)
            highlight_print(authorized_key, payload)

            break

        # If not, shift the payload to the left and try again
        if start_index < 20:
            print 'No cookie for you, sorry!'
            break

        start_index -= 1

if __name__=="__main__":
    main()
