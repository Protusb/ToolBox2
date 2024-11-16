import nmap
import re

nm = nmap.PortScanner()

def simple_scan(hosts, file_path=None):
    if isinstance(hosts, str):
        hosts = [hosts]

    for ip in hosts:
        try:
            print(f"Currently scanning {ip}")
            nm.scan(ip)
            nm[ip].all_protocols()
            print_scan_info(ip, file_path)
        except KeyError:
            error_message = f"Could not reach target: {ip}\n"
            print(error_message)
            if file_path:
                with open(file_path, "a") as file:
                    file.write(error_message)

def print_scan_info(host, file_path=None):
    output = ""
    for host in nm.all_hosts():
        output += f"----------------------------------------------------\n"
        output += f"Host : {host} ({nm[host].hostname()})\n"
        output += f"State : {nm[host].state()}\n"
        for proto in nm[host].all_protocols():
            output += f"----------\n"
            output += f"Protocol : {proto}\n"

            lport = nm[host][proto].keys()
            for port in lport:
                output += f"port : {port} | state : {nm[host][proto][port]['state']} | service: {nm[host][proto][port]['name']}\n"

    print(output)

    if file_path:
        with open(file_path, "a") as file:
            file.write(output)

def is_valid_ip(ip: str) -> bool:
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    if re.match(pattern, ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False

def import_ips():
    while True:
        print("----------------------------------------------------")
        import_choice = input("1. Enter single IP manually\n2. Import multiple IPs from a file\nChoose an option: ")
        if import_choice == '1':
            while True:
                ip = input("Enter the IP address: ")
                if is_valid_ip(ip):
                    return ip
                else:
                    print("Invalid IP address. Please try again.")
        elif import_choice == '2':
            try:
                file_name = input("Enter the file name: ")
                with open(file_name, "r") as file:
                    ips = [ip.strip() for ip in file if is_valid_ip(ip.strip())]
                if ips:
                    return ips
                else:
                    print("No valid IPs found in the file.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found. Please try again.")
        else:
            print("Wrong input, please select a valid option.")

def save_to_file():
    while True:
        user_answer = input("Do you want to save the results to a file? (y/n): ").lower()
        if user_answer == 'y':
            return input("Enter the file name to save the results: ")
        elif user_answer == 'n':
            return None
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def run_nmap():
    list_of_ips = import_ips()

    while True:
        print("----------------------------------------------------")
        print("Menu: \n1. Simple port scan\n2. See my current list of IPs\n3. Change IPs\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            file_path = save_to_file()
            simple_scan(list_of_ips, file_path)
        elif choice == '2':
            print(f"Your current list of IPs: {list_of_ips}")
        elif choice == '3':
            list_of_ips = import_ips()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Wrong input, please choose a valid option.")

run_nmap()
