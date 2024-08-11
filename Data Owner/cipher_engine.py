import os
# crypto_utils.py
from cryptography.fernet import Fernet
# hash_utils.py
import hashlib

def generate_key():
    return Fernet.generate_key()

def encrypt(key, plaintext):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(plaintext.encode())
    return encrypted_text.decode()

def decrypt(key, encrypted_text):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text.encode())
    return decrypted_text.decode()


def hash_message(message):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode())
    return sha256_hash.hexdigest()

def verify_hash(message, hash_value):
    return hash_message(message) == hash_value

if __name__ == "__main__":
    message = "Hello, World!"
    hash_value = hash_message(message)
    print(f"Message: {message}")
    print(f"SHA-256 Hash: {hash_value}")

    is_valid = verify_hash(message, hash_value)
    print(f"Hash is valid: {is_valid}")
    
    
    key = generate_key()
    print(f"Generated Key: {key.decode()}")

    plaintext = "Hello, World! one two three four five"
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
