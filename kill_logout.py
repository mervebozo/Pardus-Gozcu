import os
from threading import Timer

def stopUser(userName):
    os.system("pkill -STOP -u %s" %(userName))

def resumeUser(userName):
    os.system("pkill -CONT -u %s" %(userName))

def killLogOut(userName):
    os.system("pkill -KILL -u %s" %(userName))

def killLogOutAll():
    os.system("skill -KILL -v /dev/pts/")	

def killProcessOfUser(userName, processName):
    os.system("pkill -KILL -u %s %i" %(userName, processName))

def executer(time, func, param):
    task = Timer(time, func, args=(param,))
    task.start()
