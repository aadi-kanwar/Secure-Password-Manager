from Crypto.Cipher import AES
import base64
import os

SECRET_KEY = os.getenv("ENCRYPTION_KEY", os.urandom(32))

def encrypt_password(password):
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(password.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt_password(encrypted_password):
    encrypted_password = base64.b64decode(encrypted_password)
    nonce = encrypted_password[:16]
    ciphertext = encrypted_password[16:]
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')
