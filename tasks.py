import os
import subprocess

def getUserTasks(userName):
    tasks = []
    cmd = "pgrep -u " + userName + " | grep -Fvx \"$(pgrep -u " + userName + " -P 1)\""
    result = subprocess.check_output(cmd, shell=True)
    lst = result.split()
    for line in lst:
	com = "ps " + line
	try:
	    t = subprocess.check_output(com, shell=True).split()
	    if len(t) > 5:
		tasks.append(t[9])
	except:
	    pass
    for i in range(len(tasks)):
	t = tasks[i]
	if '/' in t:
	    t = t[t.rfind('/')+1:]
	    tasks[i] = t
    return sorted(list(set(tasks)))

def getUserTasksPS(userName):
    cmd = "last | fgrep \"still logged in\" | cut -d\" \" -f1"
    users = list(set((subprocess.check_output(cmd, shell=True).split('\n'))[:-1]))
    if userName not in users:
	return []
    cmd = "ps -ef | grep " + userName
    ts = subprocess.check_output(cmd, shell=True).split('\n')
    tasks = []
    for t in ts:
        x = t.split(' ')
        try:
            tasks.append([i for i in x if i != ''][7])
        except:
            pass
    for i in range(len(tasks)):
        t = tasks[i]
        if '/' in t:
            t = t[t.rfind('/')+1:]
            tasks[i] = t
    return sorted(list(set(tasks)))

def getUserTasksIDSource(userName, taskName):
    IDs = []
    Sources = []
    cmd = "ps -ef | grep " + userName
    tasks = subprocess.check_output(cmd, shell=True).split('\n')
    for task in tasks:
        if getTaskName(task) == taskName:
            t = task.split(' ')
            t = [i for i in t if i != '']
            IDs.append(t[1])
            Sources.append(t[7])
    return (list(set(IDs)), list(set(Sources)))

def getTaskName(task):
    task = task.split(' ')
    try:
    	task = [t for t in task if t != ''][7]
    except:
	return ''
    if '/' in task:
        return task[task.rfind('/')+1:]
    return task
