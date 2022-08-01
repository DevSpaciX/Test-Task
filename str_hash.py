import hashlib
s = "Python Bootcamp"
hashvariable = hashlib.sha1(s.encode())
print(hashvariable.hexdigest())