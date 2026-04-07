# Secure Hashing and Encryption
Python implementations of SHA-256 hashing, Caesar cipher encryption, and RSA digital signatures.

## Files
File Purpose 
`sha256_hash.py`  SHA-256 hashing for strings and files 
 `caesar_cipher.py`  Caesar cipher encrypt/decrypt 
 `digital_signature.py`  RSA-2048 digital signature sign/verify 
 `demo.py`  Runs all three and writes output to `demo_output.txt` 
 `requirements.txt`  Python dependencies 

## How It Works

### SHA-256 Hashing `sha256_hash.py`
Generates a SHA-256 hash for any input string or file. SHA-256 is a one way cryptographic hash, the same input always produces the same hash, but changing even one character produces a completely different result. Used to verify file and message integrity.

### Caesar Cipher `caesar_cipher.py`
Encrypts and decrypts text using a simple substitution cipher. Each letter is shifted forward (encrypt) or backward (decrypt) by a fixed number of positions in the alphabet. Non letter characters are left unchanged. Default shift is 13 (ROT13).

### Digital Signature — `digital_signature.py`
Simulates the digital signature process using RSA-2048 with PSS padding and SHA-256. A private key signs the message; the public key verifies it. Also demonstrates tamper detection, a modified message fails verification, proving the signature is tied to the exact original content.

## Setup & Run
```bash
pip install -r requirements.txt

# Run full demo (writes demo_output.txt)
python demo.py

# Or run individually
python sha256_hash.py
python caesar_cipher.py
python digital_signature.py

# Hash a specific file
python sha256_hash.py path/to/yourfile.txt
```

## Dependencies

- [`cryptography`](https://pypi.org/project/cryptography/) >= 42.0.0
