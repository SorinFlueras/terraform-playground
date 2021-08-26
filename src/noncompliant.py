######################
# Positional Arguments
######################

param_args = [1, 2, 3]
param_kwargs = {'x': 1, 'y': 2}

def func(a, b=1):
    print(a, b)

def positional_unlimited(a, b=1, *args):
    print(a, b, *args)

func(1)
func(1, 42)
func(1, 2, 3)  # Noncompliant. Too many positional arguments
func()  # Noncompliant. Missing positional argument for "a"

positional_unlimited(1, 2, 3, 4, 5)

def positional_limited(a, *, b=2):
    print(a, b)

positional_limited(1, 2)  # Noncompliant. Too many positional arguments


#############################
# Unexpected Keyword argument
#############################

def keywords(a=1, b=2, *, c=3):
    print(a, b, c)

keywords(1)
keywords(1, z=42)  # Noncompliant. Unexpected keyword argument "z"

def keywords_unlimited(a=1, b=2, *, c=3, **kwargs):
    print(a, b, kwargs)

keywords_unlimited(a=1, b=2, z=42)

#################################
# Mandatory Keyword argument only
#################################

def mandatory_keyword(a, *, b):
    print(a, b)

mandatory_keyword(1, b=2)
mandatory_keyword(1)  # Noncompliant. Missing keyword argument "b"



####################################################
from Cryptodome.Cipher import DES, DES3, ARC2, ARC4, Blowfish, AES
from Cryptodome.Random import get_random_bytes

key = b'-8B key-'
DES.new(key, DES.MODE_OFB) # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search

key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_CFB) # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack

key = b'Sixteen byte key'
cipher = ARC2.new(key, ARC2.MODE_CFB) # Noncompliant: RC2 is vulnerable to a related-key attack

key = b'Very long and confidential key'
cipher = ARC4.new(key) # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security)

key = b'An arbitrarily long key'
cipher = Blowfish.new(key, Blowfish.MODE_CBC) # Noncompliant: Blowfish use a 64-bit block size makes it vulnerable to birthday attacks

######################################################
def foo(a):  # NonCompliant
    b = 12
    if a == 1:
        return b
    return b

#######################################################
username = 'admin'
password = 'admin' # Sensitive
usernamePassword = 'user=admin&password=admin' # Sensitive
