import requests
import argparse
import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format="%(message)s")

parser = argparse.ArgumentParser(description='Enumeration tool to check for potential subdomains and directories of a domain')
parser.add_argument('domain', type=str, help='Domain to be enumerated (example "google.com")')
parser.add_argument("-m", "--mode", choices=["subdomains", "directories"], required=True, type=str, help="What you want to enumerate")
parser.add_argument("-l", "--list", help="Enter a wordlist file that you would like to check against the domain")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (default is 10)")

args = parser.parse_args()

if args.list:
    try:
        with open(args.list) as file:
            clean_list = file.read().splitlines()
    except FileNotFoundError:
        logging.error(f"Error: file {args.list} not found.")
        sys.exit(1)
else:
    git_url = "https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-1000.txt"
    logging.info("No wordlist provided, using default wordlist from GitHub...")
    try:
        response = requests.get(git_url)
        response.raise_for_status()
        clean_list = response.text.splitlines()
        logging.info("Successfully retrieved the default wordlist.")
    except requests.RequestException:
        logging.error("Failed to retrieve the default wordlist. Please specify a wordlist with the -l flag.")
        sys.exit(1)

found_count = 0

def check_subdomain(sub_dom):
    global found_count
    url = f"https://{sub_dom}.{args.domain}"
    try:
        requests.get(url, timeout=10)
        logging.info(f"Subdomain found: {url}")
        found_count += 1
    except requests.ConnectionError:
        pass
    except requests.exceptions.ReadTimeout:
        logging.warning(f"Read timeout for {url}")

def check_directory(directory):
    global found_count
    url = f"https://{args.domain}/{directory}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        logging.info(f"Valid directory: {url}")
        found_count += 1
    except requests.exceptions.ReadTimeout:
            pass
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404:
            pass
        else:
            logging.error(f"Error checking {url}: {e}")

def enumerate_subdomains():
    print("enumerating subdomains... this may take a while depending on the wordlist and thread-count")
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(check_subdomain, sub_dom) for sub_dom in clean_list]
        for future in as_completed(futures):
            future.result()

def enumerate_directories():
    print("Enumerating directories... this may take a while depending on the wordlist and thread-count")
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(check_directory, directory) for directory in clean_list]
        for future in as_completed(futures):
            future.result()

if args.mode == "subdomains":
    enumerate_subdomains()
elif args.mode == "directories":
    enumerate_directories()

logging.info(f"Enumeration completed. {found_count} valid entries found.")