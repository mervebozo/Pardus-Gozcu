#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def getFROM(userName):
    FROM = None
    out = subprocess.check_output("w", shell=True).split('\n')
    for o in out:
        if userName in o:
            line = [i for i in o.split(' ') if i != '']
            for l in line:
                if ':' in l:
                    FROM = l[1:]
                    break
    return FROM

def showNotification(userName, text):
    FROM = getFROM(userName)
    if FROM:
        cmd = "sudo cat /home/" + userName + "/.Xauthority | xauth merge -"
        subprocess.call(cmd, shell=True)
        cmd = "sudo DISPLAY=:" + FROM + " kdialog --title 'Pardus Gözcü' --sorry '" + text + "'&"
        subprocess.call(cmd, shell=True)
