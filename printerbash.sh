#cd /cygdrive/c/temp/PrinterConfig

#!/usr/bin/expect -f

# Set variables
set HOSTNAME "172.27.42.205"
set LOGIN "admin"
set PASSWORD ""

# Execute Telnet
spawn -noecho telnet $HOSTNAME

# Handle connection and login
expect "login:"
send "$LOGIN\r"
expect "Password:"
send "$PASSWORD\r"

# Wait for the prompt
expect "msh>"

# Send commands
send "dns\r"

# Wait for the prompt again
expect "msh>"

# Exit Telnet session
send "exit\r"

# Wait for process to finish
expect eof
