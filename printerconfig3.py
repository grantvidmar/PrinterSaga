import pyautogui
import time
import csv

# Function to perform the telnet sequence of actions
def perform_telnet_sequence(ip_address):
    # Type 'admin' into Command Prompt
    pyautogui.write('admin', interval=0.1)
    pyautogui.press('enter')

    time.sleep(2)  # Wait for 2 seconds

    # Press Enter again
    pyautogui.press('enter')

    time.sleep(2)  # Wait for 2 seconds

    # Type 'dns' into Command Prompt
    pyautogui.write('dns', interval=0.1)
    pyautogui.press('enter')

    time.sleep(5)  # Wait for 5 seconds

    # Send "dns 1 server 10.144.100.4"
    pyautogui.write('dns 1 server 10.144.100.4', interval=0.1)
    pyautogui.press('enter')

    time.sleep(2)  # Wait for 2 seconds

    # Send "dns 2 server 10.144.100.5"
    pyautogui.write('dns 2 server 10.144.100.5', interval=0.1)
    pyautogui.press('enter')

    time.sleep(2)  # Wait for 2 seconds

    # Send "dns 3 server 10.144.100.5"
    pyautogui.write('dns 3 server 10.144.100.5', interval=0.1)
    pyautogui.press('enter')

    time.sleep(2)  # Wait for 2 seconds

    # Send Ctrl+C
    pyautogui.hotkey('ctrl', 'c')

    # Wait for 2 seconds to ensure the command is interrupted
    time.sleep(2)

# Function to perform the telnet connection and telnet sequence
def perform_telnet(ip_addresses):
    # Open Command Prompt
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('cmd', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)  # Wait for 3 seconds after opening Command Prompt

    # Iterate over IP addresses
    for ip_address in ip_addresses:
        # Type the command to start telnet
        command = f'plink -telnet {ip_address} -batch'
        pyautogui.write(command, interval=0.1)
        pyautogui.press('enter')

        # Wait until the connection is established
        connection_established = False
        timeout = 30  # Maximum wait time in seconds
        start_time = time.time()
        while not connection_established and time.time() - start_time < timeout:
            time.sleep(1)  # Check every 1 second
            # Check if 'login:' prompt is visible
            screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
            if pyautogui.locateOnScreen('login.png', image=screenshot, confidence=0.8):
                connection_established = True

        if connection_established:
            # Perform the telnet sequence
            perform_telnet_sequence(ip_address)
        else:
            print(f"Connection to {ip_address} could not be established.")

# Read IP addresses from the CSV file
csv_file_path = r'C:\temp\PrinterConfig\hostlist.csv'
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    ip_addresses = [row[0] for row in csv_reader]

    # Perform telnet for all IP addresses
    perform_telnet(ip_addresses)
