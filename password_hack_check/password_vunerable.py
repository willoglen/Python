'''
Check password for vunerability
using https://pwnedpasswords.com
'''
import hashlib
import requests


def check_password(password):
    ''' checks if the password is in the database of hacked passwords'''   
    res_value = [True,0]
    hash_object = hashlib.new("sha1", password[1].encode())
    token = hash_object.hexdigest().upper()
    key = token[:5]
    print(key)
    tail = token[5:]
    # note this is now a subscription service which requires an API license  and subscription
    url = 'https://api.pwnedpasswords.com/range/' + key
    res = requests.get(url, timeout=2.50)
    if res.status_code == 200:
        hashes = (line.split(':') for line in res.text.splitlines())
        for one_hash, count in hashes:
            if one_hash == tail:
                res_value[0] = False
                res_value[1] =  f'Found {count} instances of hacked password '
                break
    else:
        res_value[0] = False
        res_value[1] = f'url request faile with status {res.status_code}' 
        
    return res_value
