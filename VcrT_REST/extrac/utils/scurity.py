import hashlib
import time

def safe_md5(user):
    ct = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ct, encoding='utf-8'))
    return m.hexdigest()