"""
asymmetric_encrypt.py
Asymmetric encryption/decryption using RSA-2048 with OAEP padding
(cryptography library). The public key encrypts; the private key decrypts.
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization


def generate_key_pair():
    """Generate a 2048-bit RSA private/public key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt(message: str, public_key) -> bytes:
    """Encrypt a plaintext string using the RSA public key."""
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def decrypt(ciphertext: bytes, private_key) -> str:
    """Decrypt ciphertext bytes using the RSA private key."""
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    ).decode()


def serialize_public_key(public_key) -> str:
    """Return PEM encoded public key as a string for display."""
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()


def serialize_private_key(private_key) -> str:
    """Return PEM encoded private key as a string for display."""
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()


if __name__ == "__main__":
    print("=== Asymmetric Encryption (RSA-2048) ===\n")

    private_key, public_key = generate_key_pair()
    message = "Hello, this is a secret message!"

    print("Public Key:\n", serialize_public_key(public_key))
    print("Private Key:\n", serialize_private_key(private_key))
    print(f"Input      : {message}")

    ciphertext = encrypt(message, public_key)
    print(f"Encrypted  : {ciphertext.hex()}")

    plaintext = decrypt(ciphertext, private_key)
    print(f"Decrypted  : {plaintext}")
