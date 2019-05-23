import hashlib
password = 'pa$$w0rd'

h = hashlib.sha256(password.encode())

print(h.hexdigest())