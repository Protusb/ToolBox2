from cryptography.fernet import Fernet, InvalidToken
import argparse
import os

parser = argparse.ArgumentParser(description='Encrypts and decrypts files')

parser.add_argument("name", type=str, help="Enter the name of the file you want to encrypt/decrypt")
parser.add_argument("-m", "--mode", choices=["encrypt","decrypt"], required=True, type=str, help="Enter if you want to encrypt or decrypt a file")

args = parser.parse_args()

try:
    with open("Secret.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    print("Key was not found, please generate one before using this tool or make sure that it is in the right folder")
    exit()

cipher_suite = Fernet(key)


def encrypt():
    if os.path.exists(args.name):
        with open(args.name, "rb") as file:
            original = file.read()

        cipher_text = cipher_suite.encrypt(original)

        with open(args.name, "wb") as enc_file:
            enc_file.write(cipher_text)
        print("Successfully Encrypted")
    else: print(f"A file with the name {args.name} does not exist")

def decrypt():
    if os.path.exists(args.name):
        with open(args.name, "rb") as enc_file:
            enc_text = enc_file.read()
        try:
            plain_text = cipher_suite.decrypt(enc_text)

            with open(args.name, "wb") as enc_file:
                enc_file.write(plain_text)
            print("Successfully Decrypted")
        except InvalidToken: print(f"The file {args.name} is already decrypted")
    else: print(f"A file with the name {args.name} does not exist")

if args.mode == "encrypt":
    encrypt()
elif args.mode == "decrypt":
    decrypt()