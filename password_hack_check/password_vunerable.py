'''
Check password for vunerability
using https://pwnedpasswords.com
'''
import hashlib
import sys
import requests


def main(password):
    result = check_password(password)
    print(result)
    
def check_password(password):
    hash_object = hashlib.new("sha1", password[1].encode())
    token = hash_object.hexdigest().upper()
    key = token[:5]
    tail = token[5:]
    url = 'https://api.pwnedpasswords.com/range/' + key
    res = requests.get(url, timeout=2.50)
    if res.status_code == 200:
        hashes = (line.split(':') for line in res.text.splitlines())
        for one_hash, count in hashes:
            if one_hash == tail:
                print(f'Found {count} instances of hacked password')
                return True
    else:
        return False


if __name__ == '__main__':
    password = sys.argv[:2]
    sys.exit(main(password))
