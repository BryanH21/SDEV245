"""
symmetric_encrypt.py
Symmetric encryption/decryption using AES-128 via the Fernet scheme
(cryptography library). The same key is used to both encrypt and decrypt.
"""
from cryptography.fernet import Fernet


def generate_key() -> bytes:
    """Generate a new random Fernet (AES-128) key."""
    return Fernet.generate_key()


def encrypt(message: str, key: bytes) -> bytes:
    """Encrypt a plaintext string and return ciphertext bytes."""
    f = Fernet(key)
    return f.encrypt(message.encode())


def decrypt(ciphertext: bytes, key: bytes) -> str:
    """Decrypt ciphertext bytes and return the original plaintext string."""
    f = Fernet(key)
    return f.decrypt(ciphertext).decode()


if __name__ == "__main__":
    print("=== Symmetric Encryption (AES via Fernet) ===\n")

    key = generate_key()
    message = "Hello, this is a secret message!"

    print(f"Key        : {key.decode()}")
    print(f"Input      : {message}")

    ciphertext = encrypt(message, key)
    print(f"Encrypted  : {ciphertext.decode()}")

    plaintext = decrypt(ciphertext, key)
    print(f"Decrypted  : {plaintext}")
