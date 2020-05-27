"""Understanding the Request / Response Cycle."""
import socket
import re

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#website = input('What is the website?\n')
website = 'http://data.pr4e.org/intro-short.txt'
search = re.search(r'//(.+?)/', website)
host = search[1]
mysocket.connect((host, 80))
cmd = ('GET ' + website + ' HTTP/1.0\r\n\r\n').encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysocket.close()
