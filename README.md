# Quotekey

Plain old randomness just doesn't cut it sometimes. Personalize your SSH keys.

## Usage
```
santosh@goodgodwhy$ python quotekey.py -h
usage: quotekey.py [-h] [--message [MESSAGE]] [--key_file [KEY_FILE]]
                   [--key_strength_bytes [KEY_STRENGTH_BYTES]]

Generate boutique SSH keys. This script embeds a string of your choice into the modulus of a freshly generated SSH key pair.

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
Nope, trying again ...
Nope, trying again ...
Success! Writing private key to test.id_rsa
Your authorized_keys entry is below:
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQG/X1eTM9IZpSI299fdjiuwvNE/sdg9JUZjnxmNPLju
Jw46wWYWDdIZozD5GgfAMYxuhTQ1jFSWItT1ElipasLvb++BjXo3HNw64fxll73GIAvE3VDp/WsvDcpL
26LSo3WYj++B33VPRn/HgUg8SCaAvqRw0RrB9V0IPS9s9K2WXXpgj+q3BKS9wVluYxSiFy7xD4BnMK0C
OyShTYaxqHQC4M8+2IH6XwWB0Vp7x1e+T8wexGZhrpEcBN5pc<b>DataAtRestEncryptionIsLikeIfSome
oneToldYouTheirCarWasPerfectlySafeBecauseItDidnTHaveWheels</b>/p5wcqDW/gSzur1OyeJpCfV
Fc6QFa953vXIyjKv05H+epvJ/skS+h+eM0PiWO5chUssFC4JD3GsoEAvwwCTm182oC1Brocr+I3Wj8hXJ
56Ad3ev/xwbj1HMdsf7fmzFZrIWLkn65yHhVPeXcrSVmnr3gmFaA8aF3xxNdkoTK7t6U8qRTIyJ8dPgYi
5O1drop7haoV4QL7W0Uqqn1ZN0P10nc8P+y+d30ju1LHe2PcHf/SIsIjWrk6IEi4BRUTEgkF4mERsGXua
6ONeE6BIoJ9v2g3Cssg04lkyFrVLIID3XveQLN/5Bu26vCjU7KeOx6Z7sB3DFrSAajN2Cix2qdYWhw==

```

## Security

These keys are probably not safe for real-use, but I don't know enough cryptography to quantify the impact of reducing entropy this way on the chance of finding either prime.

## Dependencies
* libgmp10
* python-gmpy2


## Credits

The idea is not my own. I remember reading someone who did the same thing for their SSL certificates, but I can't find their page anymore. If you do, please let me know so I can link to them here.



