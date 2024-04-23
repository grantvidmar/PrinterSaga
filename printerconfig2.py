import pyautogui
import time
import csv

# Function to perform the telnet sequence of actions
def perform_telnet_sequence(ip_address):
    # Type 'admin' into Command Prompt
    pyautogui.write('admin', interval=0.1)
    pyautogui.press('enter')

    time.sleep(1)  # Wait for 1 second

    # Press Enter again
    pyautogui.press('enter')

    time.sleep(1)  # Wait for 1 second

    # Type 'dns' into Command Prompt
    pyautogui.write('dns', interval=0.1)
    pyautogui.press('enter')

    time.sleep(5)  # Wait for 5 seconds

    # Send "dns 1 server 10.144.100.4"
    pyautogui.write('dns 1 server 10.144.100.4', interval=0.1)
    pyautogui.press('enter')

    time.sleep(1)  # Wait for 1 second

    # Send "dns 2 server 10.144.100.5"
    pyautogui.write('dns 2 server 10.144.100.5', interval=0.1)
    pyautogui.press('enter')

    time.sleep(1)  # Wait for 1 second

    # Send "dns 3 server 10.144.100.5"
    pyautogui.write('dns 3 server 10.144.100.5', interval=0.1)
    pyautogui.press('enter')

    time.sleep(1)  # Wait for 1 second

    # Send Ctrl+C
    pyautogui.hotkey('ctrl', 'c')

    # Wait for 1 second to ensure the command is interrupted
    time.sleep(1)

# Function to perform the telnet connection and log commands
def perform_telnet(ip_address):
    # Open Command Prompt
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('cmd', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)  # Wait for 1 second

    # Type the command to redirect output to log file
    log_file = r'C:\temp\PrinterConfig\log.txt'
    command = f'plink -telnet {ip_address} -batch > {log_file}'
    pyautogui.write(command, interval=0.1)
    pyautogui.press('enter')

    # Wait until the "login:" prompt appears
    login_prompt_found = False
    timeout = 30  # Maximum wait time in seconds
    start_time = time.time()
    while not login_prompt_found and time.time() - start_time < timeout:
        time.sleep(1)  # Check every 1 second
        with open(log_file, 'r') as f:
            log_content = f.read()
            if 'login:' in log_content:
                login_prompt_found = True

    if login_prompt_found:
        # Perform the telnet sequence
        perform_telnet_sequence(ip_address)
    else:
        print(f"Login prompt not found for {ip_address}. Check the connection or authentication settings.")

# Read IP addresses from the CSV file
csv_file_path = r'C:\temp\PrinterConfig\hostlist.csv'
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        ip_address = row[0]
        perform_telnet(ip_address)
