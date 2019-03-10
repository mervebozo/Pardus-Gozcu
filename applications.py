#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from tasks import getUserTasks
import os
import time
from datetime import datetime

def getApps():
    res = []
    cmd = "find /usr/share/applications -name '*.desktop'"
    lines = subprocess.check_output(cmd, shell=True).split('\n')[:-1]
    for line in lines:
	res.append(line[line.rfind('/')+1 : line.index(".desktop")])
    lo = False
    for r in res[:]:
        if "libreoffice" in r: 
            lo = True 
            res.remove(r)
    if lo:
        res.append("libreoffice")
    return sorted(res)

def getProcess(userName, word):
    result = []
    cmd = "sudo ps aux | grep " + userName + " | grep " + word
    out = subprocess.check_output(cmd, shell=True).split('\n')[:-1]
    for o in out:
        if "grep" not in o:
            line = o.split(' ')
            line = [l for l in line if l != ''][1]
            result.append(line)
    return result

def getAppProcessID(userName, app):
    ID = []
    secondName = app[app.find('-')+1:]
    search = [app]
    if secondName != app:
        search.append(secondName)
    bins = getAll(app)
    search += bins
    for s in search:
        ID += getProcess(userName, s)
    return list(set(ID))

def getAppBin(app):
    bins = []
    try:
	path = "/usr/share/applications/" + app + ".desktop"
	f = open(path, 'r')
	lines = f.readlines()
	f.close()
	for l in lines:
	    if "Exec=" in l:
		command = l[l.find('=')+1:]
		index = 0
		while command[index] == ' ':
		    index += 1
		command = command[index:]
	        bins.append(command)
    except:
	pass
    cmd = "which " + app
    try:
	w = subprocess.check_output(cmd, shell=True)
	bins.append(w)
    except:
	pass
    path = ["/bin", "/usr/bin", "/usr/games", "/usr/lib", "/usr/local", "/opt"]
    for p in path:
	cmd = "find " + p + " -name " + app
	out = None
	try:
	    out = subprocess.check_output(cmd, shell=True)
	except:
	    pass
	if out:
            out = out.split('\n')
            for o in out:
                bins.append(o)
    bins = list(set(bins))
    return bins

def getAll(app):
    bins = getAppBin(app)
    extra = []
    for b in bins:
	if '/' not in b:
            if b.split(' ')[0] != '':
	        extra += getAppBin(b.split(' ')[0])
    bins += extra
    bins = [b for b in bins if '/' in b]
    for i in range(len(bins)):
	lst = bins[i].split(' ')
	if len(lst) > 1:
	    for l in lst:
		if '/' in l:
		    bins[i] = l
		    break
    for i in range(len(bins)):
        if '\n' in bins[i]:
            bins[i] = bins[i][:-1]
    return list(set(bins))

def getUsedApps():
    apps = getApps()
    f = open("appSettings/log/kullanilan.txt", 'w')
    for app in apps:
	tmp = []
	f.write("Uygulama Adı: " + app + "\n")
	bins = getAll(app)
	for b in bins:
	    try:
		tmp.append(time.ctime(os.stat(b).st_atime))
	    except:
		pass
	if len(tmp) == 0:
	    f.write("   Kullanım bilgisi bulunamadı." + "\n")
	    continue
	f.write("   " + max(tmp) + "\n\n")
    f.close()
