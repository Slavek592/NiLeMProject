$script = New-Object Net.WebClient
$script.DownloadString("https://chocolatey.org/install.ps1")
iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
choco upgrade chocolatey
choco install -y python3
python -m pip install --upgrade pip
python -m pip install tkPDFViewer
