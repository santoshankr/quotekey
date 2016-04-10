# Quotekey

Bumper stickers and yard signs are so 2000s. SSH authorized_keys file statements is the next big thing.

## Usage
```
santosh@goodgodwhy$ python quotekey.py -h
usage: quotekey.py [-h] [--message [MESSAGE]] [--key_file [KEY_FILE]]
                   [--key_strength_bytes [KEY_STRENGTH_BYTES]]

Generate boutique SSH keys. This script embeds a string of your choice into
the modulus of a freshly generated SSH key pair.

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
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQG/X1eTM9IZpSI299fdjiuwvNE/sdg9JUZjnxmNPLjuJw46wWYWDdIZozD5GgfAMYxuhTQ1jFSWItT1ElpasLvb++BjXo3HNw64fxll73GIAvE3VDp/WsvDcpL26LSo3WYj++B33VPRn/HgUg8SCaAvqRw0RrB9V0IPS9s9K2WXXpgj+q3BKS9wVluYxSiFy7xD4BnMK0COyShTYaxqHQC4M8+2IH6XwWB0Vp7x1e+T8wexGZhrpEcBN5pcDataAtRestEncryptionIsLikeIfSomeoneToldYouTheirCarWasPerfectlySafeBecauseItDidnTHaveWheels/p5wcqDW/gSzur1OyeJpCfVFc6QFa953vXIyjKv05H+epvJ/skS+h+eM0PiWO5chUssFC4JD3GsoEAvwwCTm182oC1Brocr+I3Wj8hXJ56Ad3ev/xwbj1HMdsf7fmzFZrIWLkn65yHhVPeXcrSVmnr3gmFaA8aF3xxNdkoTK7t6U8qRTIyJ8dPgYi5O1drop7haoV4QL7W0Uqqn1ZN0P10nc8P+y+d30ju1LHe2PcHf/SIsIjWrk6IEi4BRUTEgkF4mERsGXua6ONeE6BIoJ9v2g3Cssg04lkyFrVLIID3XveQLN/5Bu26vCjU7KeOx6Z7sB3DFrSAajN2Cix2qdYWhw==

```

## Dependencies
* libgmp10
* python-gmpy2
