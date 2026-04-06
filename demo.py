"""
demo.py
Runs both symmetric and asymmetric encryption demos and saves all
keys, inputs, and outputs to demo_output.txt for submission.
"""
import sys
from io import StringIO

import symmetric_encrypt as sym
import asymmetric_encrypt as asym


def run_demo() -> str:
    lines = []
    # Symmetric
    lines.append("")
    lines.append("SYMMETRIC ENCRYPTION  (AES-128 via Fernet)")
    lines.append("")

    sym_key = sym.generate_key()
    message = "Hello, this is a secret message!"
    sym_cipher = sym.encrypt(message, sym_key)
    sym_plain = sym.decrypt(sym_cipher, sym_key)

    lines.append(f"Key        : {sym_key.decode()}")
    lines.append(f"Input      : {message}")
    lines.append(f"Encrypted  : {sym_cipher.decode()}")
    lines.append(f"Decrypted  : {sym_plain}")
    lines.append("")

    # Asymmetric
    lines.append("")
    lines.append("ASYMMETRIC ENCRYPTION  (RSA-2048 with OAEP/SHA-256)")
    lines.append("")

    private_key, public_key = asym.generate_key_pair()
    asym_cipher = asym.encrypt(message, public_key)
    asym_plain = asym.decrypt(asym_cipher, private_key)

    lines.append("Public Key:")
    lines.append(asym.serialize_public_key(public_key))
    lines.append("Private Key:")
    lines.append(asym.serialize_private_key(private_key))
    lines.append(f"Input      : {message}")
    lines.append(f"Encrypted  : {asym_cipher.hex()}")
    lines.append(f"Decrypted  : {asym_plain}")

    return "\n".join(lines)


if __name__ == "__main__":
    output = run_demo()

    print(output)

    with open("demo_output.txt", "w") as f:
        f.write(output)

    print("\n[demo_output.txt written]")
