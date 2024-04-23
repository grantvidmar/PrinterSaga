# Path to the plink executable
$plinkPath = "C:\Program Files\PuTTY\plink.exe"

# Path to the user directory
$userDirectory = "C:\Users\VidmarG"

# Command to execute with plink for telnet
$plinkCommand = "-telnet hostname"

# Start a new Command Prompt window, navigate to the user directory, and run plink
Start-Process -FilePath "cmd.exe" -ArgumentList "/k cd /d $userDirectory && $plinkPath $plinkCommand"
