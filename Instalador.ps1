$F = Get-Service -Name "wuauserv"
if ($F.status -eq "Running") {
Install-Windowsupdate -AcceptAll
} else {
Start-service -name "wuauserv"
Install-windowsupdate -AcceptAll
}
