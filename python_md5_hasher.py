import hashlib
from sys import argv

def hashString(arg):
    s_hash = hashlib.md5(s.encode())
    s_hex = s_hash.hexdigest()
    return s_hex

script, s = argv
print(hashString(s))
