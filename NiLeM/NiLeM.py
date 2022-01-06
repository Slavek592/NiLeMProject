#!/usr/bin/python3
from http.server import HTTPServer
from Definitions import Main

hostName = "localhost"
serverPort = 8080

webServer = HTTPServer((hostName, serverPort), Main.NiLeMServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.\n")
