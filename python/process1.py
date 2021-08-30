import re
with open('uspolygon.txt') as fp:
    Lines = fp.readlines()
    for line in Lines:
        if line[0:12]=='<state name=':
            print(re.findall(r'"([^"]*)"', line))











