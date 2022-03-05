import os
import platform, struct
import multiprocessing
import cProfile
import socket

import os.path, time

print(platform.architecture()[0])
print(struct.calcsize("P") * 8)

print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

print(os.system('dir'))

print("Current File Name : ",os.path.realpath(__file__))
print(multiprocessing.cpu_count())

def sum():
    print(1+2)
cProfile.run('sum()')

print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

print("Last modified: %s" % time.ctime(os.path.getmtime("liczby.txt")))
print("Created: %s" % time.ctime(os.path.getctime("liczby.txt")))


import math

help(math)