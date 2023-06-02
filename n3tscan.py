#!/usr/bin/python
# Fast ping sweep of a /24 network
# Usage example: python n3tscan.py 192.168.0
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping_ip(ip):
    # Construct the ping command
    command = ['ping', '-c', '1', '-W', '1', ip]
    
    # Execute the ping command
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return ip, True
    except subprocess.CalledProcessError:
        return ip, False

def ping_subnet(network):
    # Define the range of IP addresses to scan
    start_ip = 1
    end_ip = 254

    # Create a thread pool with a maximum of 255 threads
    with ThreadPoolExecutor(max_workers=255) as executor:
        # Create a list to store the submitted tasks
        tasks = []

        # Loop through the IP addresses and submit the ping tasks
        for ip in range(start_ip, end_ip + 1):
            address = f'{network}.{ip}'
            tasks.append(executor.submit(ping_ip, address))
        
        # Process the completed tasks
        for task in tasks:
            ip, result = task.result()
            if result:
                print(f'Alive IP: {ip}')

# Check if the network argument is provided
if len(sys.argv) < 2:
    print('Please provide the network as an argument.eg. 192.168.0')
    print('Usage: python n3tscan.py <network>')
    sys.exit(1)

# Get the network from the command-line argument
network = sys.argv[1]

# Usage example: python n3tscan.py 192.168.0
ping_subnet(network)

