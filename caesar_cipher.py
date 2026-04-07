"""
caesar_cipher.py
Encrypts and decrypts text using a Caesar cipher (substitution cipher).
Each letter is shifted by a fixed number of positions in the alphabet.
"""


def encrypt(text: str, shift: int) -> str:
    """Encrypt text by shifting each letter forward by 'shift' positions."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text by shifting each letter backward by 'shift' positions."""
    return encrypt(text, -shift)


if __name__ == "__main__":
    print("=== Caesar Cipher ===\n")

    message = "Hello, this is a secret message!"
    shift = 13  # ROT13

    print(f"Shift        : {shift}")
    print(f"Input        : {message}")

    encrypted = encrypt(message, shift)
    print(f"Encrypted    : {encrypted}")

    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted    : {decrypted}")
