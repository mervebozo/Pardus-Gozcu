#!/usr/bin/env python

import subprocess
import re

def fnd(passwdLine):
    return passwdLine[:passwdLine.find(':')]

def user():
    f = open('/etc/login.defs')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        if re.match("^UID_MIN", lines[i]):
            UID_MIN = re.findall(r'\d+', lines[i])[0]
        if re.match("^UID_MAX", lines[i]):
            UID_MAX = re.findall(r'\d+', lines[i])[0]
    UID_MIN = int(UID_MIN)
    UID_MAX = int(UID_MAX)
    users = []
    lines = subprocess.check_output("cat /etc/passwd", shell=True).split()  
    for i in range(len(lines)):
        row = lines[i]
        occur = []
        for j in range(len(row)):	
            if row[j] == ':':			
                occur.append(j)	
        try:
            id_ = int(row[occur[1]+1:occur[2]])
        except:
            continue
        if (id_ >= UID_MIN and id_ <= UID_MAX):
            users.append(fnd(row))
    return users

def activeUser():
    cmd = "users"
    out = list(set(subprocess.check_output(cmd, shell=True)[:-1].split(' ')))
    return out
