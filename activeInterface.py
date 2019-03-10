import subprocess

def interface():
    output = subprocess.check_output("ip link show", shell=True).split('\n')
    for i in range(len(output)):
	if "state UP" in output[i]:
	    line = output[i]
	    pos = []
	    for i in range(len(line)):
		if line[i] == ':':
		    pos.append(i)
    return line[pos[0]+2:pos[1]]
