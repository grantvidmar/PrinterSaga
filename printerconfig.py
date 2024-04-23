import pyautogui
import time

# Open Command Prompt
pyautogui.press('win')
time.sleep(1)
pyautogui.write('cmd', interval=0.1)
pyautogui.press('enter')
time.sleep(3)  # Wait for 3 seconds

# Type the command into Command Prompt
command = 'plink -telnet 172.27.42.205 -batch'
pyautogui.write(command, interval=0.1)
pyautogui.press('enter')

time.sleep(10)  # Wait for 10 seconds

# Type 'admin' into Command Prompt
pyautogui.write('admin', interval=0.1)
pyautogui.press('enter')

time.sleep(3)  # Wait for 3 seconds

# Press Enter again
pyautogui.press('enter')

time.sleep(3)  # Wait for 3 seconds

# Type 'dns' into Command Prompt
pyautogui.write('dns', interval=0.1)
pyautogui.press('enter')

time.sleep(5)  # Wait for 5 seconds

# Send "dns 1 server 10.144.100.4"
pyautogui.write('dns 1 server 10.144.100.4', interval=0.1)
pyautogui.press('enter')

time.sleep(3)  # Wait for 3 seconds

# Send "dns 2 server 10.144.100.5"
pyautogui.write('dns 2 server 10.144.100.5', interval=0.1)
pyautogui.press('enter')

time.sleep(3)  # Wait for 3 seconds

# Send "dns 3 server 10.144.100.5"
pyautogui.write('dns 3 server 10.144.100.5', interval=0.1)
pyautogui.press('enter')

time.sleep(2)  # Wait for 2 seconds

# Send Ctrl+C
pyautogui.hotkey('ctrl', 'c')
