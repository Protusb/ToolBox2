# File Encryption and Decryption Tool

This Python tool allows you to encrypt and decrypt files using the `cryptography` library. 
It includes two programs: one for generating an encryption key and another for using this key to encrypt or 
decrypt files.

## Requirements
- **Required Libraries**:
  - `cryptography`: Install using `pip install cryptography`.

## Usage

### Program 1: Key Generation

The first program generates an encryption key and saves it as `Secret.key` in the current directory. If `Secret.key` already exists, you will be prompted to overwrite it.

Run the program:

```bash
python key_generator.py
```
Output:

- The program will display the generated key and save it as `Secret.key` in the current directory.

### Program 2: Encrypt and Decrypt Files
The second program encrypts or decrypts a file using the `Secret.key` file.

Run the program with the following arguments:
```bash
python file_encrypt_decrypt.py <file_name> -m <mode>
```
### Required Arguments
- **file_name**: The name of the file to encrypt or decrypt.
- **-m / --mode**: Specifies the mode of operation. Use encrypt to encrypt the file and decrypt to decrypt it.
Example Usage
```bash
# Encrypt a file named 'example.txt'
python file_encrypt_decrypt.py example.txt -m encrypt

# Decrypt a file named 'example.txt'
python file_encrypt_decrypt.py example.txt -m decrypt
```
Example Run Output
```plaintext
Successfully Encrypted
Successfully Decrypted
```
## Known Limitations
- **Key Dependency**: The Secret.key file must be generated and available in the same directory as the encryption/decryption script.
- **Overwrite Warning**: Encryption overwrites the original file. It's recommended to back up the original file before encryption.