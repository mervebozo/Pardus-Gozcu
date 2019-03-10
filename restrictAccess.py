import os
from notify import *

def denyApp(userName, path):
    cmd = "sudo setfacl -m u:" + userName + ":--- " + path
    os.system(cmd)

def allowApp(userName, path):
    cmd = "sudo setfacl -m u:" + userName + ":r-x " + path
    os.system(cmd)

def disconnect(userName):
    cmd = "sudo iptables -A OUTPUT -m owner --uid-owner " + userName + " -j DROP"
    os.system(cmd)
	
def reconnect(userName):
    cmd = "sudo iptables -D OUTPUT -m owner --uid-owner " + userName + " -j DROP"
    os.system(cmd)
