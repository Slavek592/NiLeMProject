#!/usr/bin/python3
from http.server import HTTPServer
from Definitions import Main

serverPort = 8000

try:
    webServer = HTTPServer(("", serverPort), Main.NiLeMServer)
except OSError:
    exit(0)
print("Server started.")

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("\nServer stopped.")
