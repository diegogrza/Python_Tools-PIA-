$g = Get-Service -Name "wuauserv"
if ($g.status -eq "Running") {
Stop-service -name "wuauserv"
}