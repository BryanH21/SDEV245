"""
demo.py
Runs all three modules and saves keys, inputs, and outputs to demo_output.txt.
"""
import sha256_hash as sha
import caesar_cipher as caesar
import digital_signature as ds

lines = []
message = "Hello, this is a secret message!"

# SHA-256
lines.append("SHA-256 HASHING")
lines.append(f"Input          : {message}")
lines.append(f"SHA-256 Hash   : {sha.hash_string(message)}")
lines.append("")
message2 = "Hello, this is a test message?"
lines.append(f"Input          : {message2}")
lines.append(f"SHA-256 Hash   : {sha.hash_string(message2)}")
lines.append("Note: One character difference = completely different hash")
lines.append("")

# Caesar Cipher
lines.append("CAESAR CIPHER")
shift = 13
encrypted = caesar.encrypt(message, shift)
decrypted = caesar.decrypt(encrypted, shift)
lines.append(f"Shift          : {shift}")
lines.append(f"Input          : {message}")
lines.append(f"Encrypted      : {encrypted}")
lines.append(f"Decrypted      : {decrypted}")
lines.append("")

# Digital Signature
lines.append("DIGITAL SIGNATURE (RSA-2048 + SHA-256)")
private_key, public_key = ds.generate_key_pair()
signature = ds.sign(message, private_key)
valid = ds.verify(message, signature, public_key)
tampered = "Hello, this is a TAMPERED message!"
invalid = ds.verify(tampered, signature, public_key)

lines.append(f"Public Key     :\n{ds.serialize_public_key(public_key)}")
lines.append(f"Private Key    :\n{ds.serialize_private_key(private_key)}")
lines.append(f"Message        : {message}")
lines.append(f"Signature      : {signature.hex()}")
lines.append(
    f"Verification (correct message)  : {'VALID' if valid else 'INVALID'}")
lines.append(
    f"Verification (tampered message) : {'VALID' if invalid else 'INVALID'}")

output = "\n".join(lines)
print(output)
with open("demo_output.txt", "w") as f:
    f.write(output)

print("\n[demo_output.txt written]")
