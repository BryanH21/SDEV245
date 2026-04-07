"""
sha256_hash.py
Generates SHA-256 hashes for input strings and files.
Demonstrates how SHA-256 is used to verify data integrity.
"""
import hashlib
import sys
import os


def hash_string(text: str) -> str:
    """Return the SHA-256 hash of a string."""
    return hashlib.sha256(text.encode()).hexdigest()


def hash_file(filepath: str) -> str:
    """Return the SHA-256 hash of a file's contents."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


if __name__ == "__main__":
    print("SHA-256 Hashing \n")

    # Hash a string
    message = "Hello, this is a test message!"
    print(f"Input String : {message}")
    print(f"SHA-256 Hash : {hash_string(message)}\n")

    # Show that changing one character completely changes the hash
    message2 = "Hello, this is a test message?"
    print(f"Input String : {message2}")
    print(f"SHA-256 Hash : {hash_string(message2)}\n")

    print("Notice: changing one character produces a completely different hash.\n")

    # Hash a file if provided as argument
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            print(f"File         : {filepath}")
            print(f"SHA-256 Hash : {hash_file(filepath)}")
        except FileNotFoundError as e:
            print(e)
