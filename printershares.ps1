# Define an array of network shares where printers are located
$networkShares = @(
    "Printer server addresses"

)

# Define the path where you want to save the CSV file
$csvFilePath = "C:\temp\printers.csv"

# Initialize an array to store printer information
$printerInfo = @()

# Loop through each network share
foreach ($networkShare in $networkShares) {
    # Get the list of printers from the network share
    $printers = Get-Printer -ComputerName $networkShare
    
    # If there are printers, add their information to the array
    if ($printers) {
        foreach ($printer in $printers) {
            $printerInfo += [PSCustomObject]@{
                "NetworkShare" = $networkShare
                "Name" = $printer.Name
                "PortName" = $printer.PortName
                "DriverName" = $printer.DriverName
            }
        }
    }
}

# Export the printer information to a CSV file
$printerInfo | Export-Csv -Path $csvFilePath -NoTypeInformation

Write-Host "Printer information saved to: $csvFilePath"
