#!/usr/bin/python3
from http.server import HTTPServer
from Definitions import Main

hostName = "localhost"
serverPort = 8080

try:
    webServer = HTTPServer((hostName, serverPort), Main.NiLeMServer)
except OSError:
    exit(0)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("\nServer stopped.")
