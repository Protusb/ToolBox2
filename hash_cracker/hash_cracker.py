import hashlib
import argparse
import requests
import sys

parser = argparse.ArgumentParser(description='Hash cracker, use a wordlist and returns the word that matches the hash')
parser.add_argument("password", type=str, help="Enter the password hash")
parser.add_argument("-l", "--list", help="Enter a wordlist file that you would like to check against the domain")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (default is 10)")
parser.add_argument("-th", "--typehash", choices=["md5", "sha1","sha224","sha384", "sha256", "sha512"],required=True ,help="Hash type")

args = parser.parse_args()

if args.list:
    try:
        with open(args.list) as file:
            wordlist = file.read().splitlines()
    except FileNotFoundError:
        print(f"The file {args.list} could not be found")
        sys.exit(1)
else:
    git_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10k-most-common.txt"
    try:
        response = requests.get(git_url)
        response.raise_for_status()
        wordlist = response.text.splitlines()
    except requests.RequestException:
        print("Failed to retrieve the default wordlist. Please specify a wordlist file with the -l flag.")
        sys.exit(1)

def hash_type():
    if "md5" in args.typehash:
        return hashlib.md5
    elif "sha1" in args.typehash:
        return hashlib.sha1
    elif "sha224" in args.typehash:
        return hashlib.sha224
    elif "sha256" in args.typehash:
        return hashlib.sha256
    elif "sha384" in args.typehash:
        return hashlib.sha384
    elif "sha512" in args.typehash:
        return hashlib.sha512

def crack_hash():
    h = hash_type()
    for password in wordlist:
        hash_ob = h(password.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == args.password:
            print('Found cleartext password! ' + password.strip())
            exit(0)

crack_hash()