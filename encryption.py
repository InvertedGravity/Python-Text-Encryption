# Library pycryptodome used for this encryption script
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# Static salt for encryption
salt = b'\xfbj@\xdc\x9aoT8\xa4\x08\x05\xffZ\xa4\xe0\xe5\xb4\x0f\x12\x99D\xd4z\xac\xee)\x92\x15$\x96\x8f\r'
# Password for encryption
password = "password" # The most secure password known to man
# Generates key for encryption
key = PBKDF2(password, salt, dkLen=32)
# Message to be encrypted
msg = b"Hello World!"
# Creates cipher to actually encrypt our data to a form that cannot be read
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(msg, AES.block_size))
# Exports encrypted text into a binary file
with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
# Decrypt encrypted text
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
