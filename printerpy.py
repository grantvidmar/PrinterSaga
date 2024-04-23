# Define the path to the CSV file
$csvFilePath = "C:\temp\printers.csv"

# Import the CSV file
$data = Import-Csv $csvFilePath

# Function to get MAC address from IP address
function Get-MacAddress {
    param (
        [string]$ipAddress
    )
    $mac = Get-WmiObject Win32_NetworkAdapterConfiguration | Where-Object { $_.IPAddress -contains $ipAddress }
    if ($mac) {
        return $mac.MACAddress
    } else {
        return $null
    }
}

# Iterate over each row in the CSV data
foreach ($row in $data) {
    $ipAddress = $row.PortName
    $macAddress = Get-MacAddress -ipAddress $ipAddress
    if ($macAddress) {
        $row | Add-Member -MemberType NoteProperty -Name "MACAddress" -Value $macAddress
    }
}

# Export the updated data back to the CSV file
$data | Export-Csv -Path $csvFilePath -NoTypeInformation
