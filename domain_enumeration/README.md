
# Enumeration Tool

This Python script checks for potential subdomains or directories of a given domain using a wordlist. 
It supports concurrent checks and allows specifying a custom wordlist or using a default wordlist from
an online source.

## Requirements

- **Required Libraries**:
  - `requests`: Install using `pip install requests` (used for making HTTP requests to the target domain).
## Usage

Run the script with the following arguments:

```bash
python your_script_name.py <domain> -m <mode> -l <wordlist_file> -t <threads>
```

### Required Arguments

- **domain**: The target domain to be enumerated (e.g., "example.com").
- **-m / --mode**: Specifies what to enumerate. Choose `subdomains` to check for subdomains or `directories` to check for directories.

### Optional Arguments

- **-l / --list**: Specifies a wordlist file to check against the domain. If not provided, the script fetches a default wordlist.
- **-t / --threads**: Number of concurrent threads to use. Default is 10.

### Example Usage

```bash
# Enumerate subdomains using a custom wordlist file with 5 threads
python your_script_name.py example.com -m subdomains -l wordlist.txt -t 5

# Enumerate directories using the default wordlist from GitHub
python your_script_name.py example.com -m directories
```

### Example Run Output

```plaintext
No wordlist provided, using default wordlist from GitHub...
Successfully retrieved the default wordlist.
enumerating subdomains... this may take a while depending on the wordlist and thread-count
Subdomain found: https://blog.example.com
Subdomain found: https://mail.example.com
...
Enumeration completed. 2 valid entries found.
```

## Known Limitations

- **Network Dependency for Default Wordlist**: If no wordlist file is specified, the script attempts to download a wordlist from GitHub. This may fail if there is no internet connection.
- **Potential Timeout Issues**: Large wordlists or slow connections may lead to timeouts.