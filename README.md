# Quotekey

Plain old randomness just doesn't cut it sometimes. Personalize your SSH keys.

## Usage
```
santosh@goodgodwhy$ python quotekey.py -h
usage: quotekey.py [-h] [--message [MESSAGE]] [--key_file [KEY_FILE]]
                   [--key_strength_bytes [KEY_STRENGTH_BYTES]]

Generate boutique SSH keys. This script embeds a string of your choice into the
modulus of a freshly generated SSH key pair.

optional arguments:
  -h, --help            show this help message and exit
  --message [MESSAGE]   Statement you would like your authorized_keys to make
  --key_file [KEY_FILE]
                        Location to write SSH private key file
  --key_strength_bytes [KEY_STRENGTH_BYTES]
                        Desired length of modulus in bytes
```
## Example Run

```
santosh@goodgodwhy:~/src/quotekey$ python quotekey.py
```
![Alt text](/quotekey.png?raw=true "Quotekey")

## Security

These keys are probably not safe for real-use, but I don't know enough cryptography to quantify the impact of reducing entropy this way on the chance of finding either prime.

## Dependencies
* libgmp10
* python-gmpy2


## Credits

The idea is not my own. I remember reading someone who did the same thing for their SSL certificates, but I can't find their page anymore. If you do, please let me know so I can link to them here.



