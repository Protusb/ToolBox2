
# Hash Cracker

This Python script attempts to crack a given hash by comparing it to the hashes of words in a wordlist. The program supports multiple hash algorithms and allows users to specify a custom wordlist or use a default wordlist..

## Requirements

- **Required Libraries**:
  - `requests`: Install using `pip install requests` (used for fetching the default wordlist from an online source).

## Usage

Run the script with the following arguments:

```bash
python hash_cracker.py <password_hash> -th <hash_type> -l <wordlist_file> -t <threads>
```

### Required Arguments

- **password_hash**: The hash you want to crack.
- **-th / --typehash**: Specifies the hash type. Accepted values are `md5`, `sha1`, `sha224`, `sha256`, `sha384`, and `sha512`.

### Optional Arguments

- **-l / --list**: Specifies a wordlist file to check against the hash. If not provided, the script fetches a default wordlist.
- **-t / --threads**: Number of concurrent threads to use. Default is 10.

### Example Usage

```bash
# Using a custom wordlist file
python hash_cracker.py e10adc3949ba59abbe56e057f20f883e -th md5 -l wordlist.txt -t 5

# Using the default wordlist from GitHub
python hash_cracker.py e10adc3949ba59abbe56e057f20f883e -th md5
```

### Example Run Output

```plaintext
Found cleartext password! 123456
```

## Known Limitations

- **Limited Hashing Algorithms**: The script supports only MD5, SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 algorithms.
- **Network Dependency for Default Wordlist**: If no wordlist file is specified, the script attempts to download a wordlist from GitHub. This may fail if there is no internet connection.

