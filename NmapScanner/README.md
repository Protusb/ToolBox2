
# Simple Nmap Port Scanner

This script allows users to perform a simple port scan on one or more IP addresses using the `nmap` library. 
The program allows the user to manually enter a single IP address or import multiple IPs from a file, 
and optionally save the scan results to an output file.

## Requirements

- **Required Libraries**:
  - `nmap`: Install using `pip install python-nmap`

## Usage

1. **Run the Program**:
   ```bash
   python NmapScanner.py
   ```

2. **Options in the Program**:
   - **Enter a Single IP**: Manually input a valid IP address.
   - **Import Multiple IPs**: Import multiple IPs from a text file (one IP per line).
   - **Save Results**: Choose whether to save the scan results to a file and specify the file name if desired.

### Menu Options
- **1. Simple port scan**: Performs a scan on the current list of IPs.
- **2. See current list of IPs**: Displays the IPs currently loaded for scanning.
- **3. Change IPs**: Reload IPs by entering a new single IP or by importing from a file.
- **4. Exit**: Exit the program.

### Example Run

Here's an example workflow for running the program:

```plaintext
----------------------------------------------------
1. Enter single IP manually
2. Import multiple IPs from a file
Choose an option: 1
Enter the IP address: 192.168.1.1

----------------------------------------------------
Do you want to save the results to a file? (y/n): y
Enter the file name to save the results: scan_results.txt

----------------------------------------------------
Menu: 
1. Simple port scan
2. See my current list of IPs
3. Change IPs
4. Exit
Choose an option: 1

Currently scanning 192.168.1.1
----------------------------------------------------
Host : 192.168.1.1 (hostname)
State : up
----------
Protocol : tcp
port : 22 | state : open | service: ssh
port : 80 | state : open | service: http
...
```

## Known Limitations
- **Single Threading**: This script is single-threaded, meaning it may be slow when scanning many IP addresses or multiple ports on slower networks.
- **Limited Protocols**: Currently, only basic information for each IP address is scanned and displayed. Additional nmap features (e.g., OS detection, service versioning) could be added for more detailed scans.
