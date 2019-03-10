import datetime
import subprocess

def getTimes(userName, path):
    f = open(path, "r")
    dt = f.readlines()
    f.close()
    times = []
    for i in range(len(dt)):
        if ('$' + userName) in dt[i]:
            i += 1
            while (len(dt) > i) and not ('$' in dt[i]):
                times.append(dt[i].split(' '))
                i += 1
    return times

def getBannedHours(day, path):
    f = open(path, "r")
    rules = f.readlines()
    f.close()
    ban = []
    userName = None
    current = []
    for i in range(len(rules)):
        if '$' in rules[i]:
            ban.append((userName, current))
            current = []
            userName = rules[i][1:-1]
        else:
            rule = rules[i].split(' ')
            row = int(rule[0])
            if row == day:
                current.append(int(rule[1]))
            if (i + 1) == len(rules):
                ban.append((userName, current))
    ban = ban[1:]
    return ban
    
def getBannedHoursUser(day, path, userName):
    data = getBannedHours(day, path)
    hours = []
    for d in data:
	if userName == d[0]:
	    hours = d[1]
	    break
    return hours

def getBannedHoursToday(path):
    day = datetime.datetime.today().weekday()
    return getBannedHours(day, path)

def getBannedHoursTodayUser(userName, path):
    ban = getBannedHoursToday(path)
    hours = []
    for x in ban:
        if userName == x[0]:
            hours = x[1]
            break
    return hours

def remainingSeconds(userName, path):
    hours = getBannedHoursTodayUser(userName, path)
    hour = datetime.datetime.now().hour
    limit = False
    for i in hours:
        if hour < int(i):
            rt = (i * 3600) - (datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second)
            limit = True
            break
    if limit == False:
        return -1
    return rt

def timeToEndBan(userName, path):
    hours = getBannedHoursTodayUser(userName, path)
    hour = datetime.datetime.now().hour
    end = -9
    flag = False
    for i in hours:
        if flag == False and hour <= i:
            flag = True
            end = i
        if i == (end + 1):
            end = i
    return ((end + 1) * 3600) - (datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second)

def isLegal(userName, path):
    ban = getBannedHoursToday(path)
    hour = datetime.datetime.now().hour
    result = True
    for x in ban:
        if (hour in x[1]) and userName == x[0]:
            result = False
    return result
