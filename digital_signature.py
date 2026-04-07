"""
digital_signature.py
Simulates a digital signature workflow using RSA-2048.
- A private key signs the message (proves identity + integrity)
- A public key verifies the signature (anyone can verify)
This mirrors how OpenSSL's rsautl / dgst commands work under the hood.
"""
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature


def generate_key_pair():
    """Generate a 2048 bit RSA key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return private_key, private_key.public_key()


def sign(message: str, private_key) -> bytes:
    """Sign a message with the private key. Returns raw signature bytes."""
    return private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )


def verify(message: str, signature: bytes, public_key) -> bool:
    """Verify a signature against a message using the public key."""
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False


def serialize_public_key(public_key) -> str:
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()


def serialize_private_key(private_key) -> str:
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()


if __name__ == "__main__":
    print("Digital Signature (RSA-2048 + SHA-256) \n")

    private_key, public_key = generate_key_pair()
    message = "Hello, this is a secret message!"

    print(f"Public Key   :\n{serialize_public_key(public_key)}")
    print(f"Private Key  :\n{serialize_private_key(private_key)}")
    print(f"Message      : {message}\n")

    signature = sign(message, private_key)
    print(f"Signature    : {signature.hex()}\n")

    # Verify with correct message
    result = verify(message, signature, public_key)
    print(
        f"Verification (correct message)  : {'VALID' if result else 'INVALID'}")

    # Verify with tampered message
    tampered = "Hello, this is a TAMPERED message!"
    result_tampered = verify(tampered, signature, public_key)
    print(
        f"Verification (tampered message) : {'VALID' if result_tampered else 'INVALID'}")
