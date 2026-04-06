# Encrypt/Decrypt Demo

Demonstrates symmetric and asymmetric encryption/decryption in Python using the `cryptography` library.

## Files

 File Purpose 
 `symmetric_encrypt.py` AES-128 symmetric encryption via Fernet 
 `asymmetric_encrypt.py` RSA-2048 asymmetric encryption with OAEP padding 
 `demo.py` Runs both methods and saves output to `demo_output.txt` 
 `requirements.txt`  Python dependencies 


## How It Works
### Symmetric Encryption: `symmetric_encrypt.py`
- **Algorithm:** AES-128-CBC wrapped in the [Fernet](https://cryptography.io/en/latest/fernet/) scheme
- **Key:** A single randomly generated 32 byte (256 bit) URL safe base64 key
- **Process:**
  1. Generate a Fernet key
  2. Encrypt the plaintext message → produces a base64 encoded ciphertext token
  3. Decrypt the token with the same key → recovers original plaintext
- **Key property:** Same key encrypts *and* decrypts (symmetric)

### Asymmetric Encryption: `asymmetric_encrypt.py`
- **Algorithm:** RSA-2048 with OAEP padding and SHA-256
- **Keys:** A public/private key pair (2048 bit)
- **Process:**
  1. Generate a private key and derive the corresponding public key
  2. Encrypt the plaintext with the **public key** → produces raw ciphertext bytes
  3. Decrypt with the **private key** → recovers original plaintext
- **Key property:** Public key encrypts, private key decrypts (asymmetric)

## Setup & Run
```bash
pip install -r requirements.txt

# Run the full demo (writes demo_output.txt)
python demo.py

# Or run each module independently
python symmetric_encrypt.py
python asymmetric_encrypt.py
```

## Output
`demo.py` prints and saves to `demo_output.txt`:
- The key(s) used
- The input message
- The encrypted ciphertext
- The decrypted output (matching the original input)

## Dependencies

- [`cryptography`](https://pypi.org/project/cryptography/) ≥ 42.0.0
