def getUserData(path, userName):
    f = open(path, "r")
    hosts = f.readlines()
    f.close()
    result = []
    point = 0
    for i in range(len(hosts)):
	point += 1
	if(("$" + userName) == hosts[i][:-1]):
	    break
    for x in range(point,len(hosts)):
	if hosts[x][0] == '$':
	    break
	if len(hosts[x]) > 1:
            if '\n' in hosts[x]:
                hosts[x] = hosts[x][:-1]
	    result.append(hosts[x])	
    return result
