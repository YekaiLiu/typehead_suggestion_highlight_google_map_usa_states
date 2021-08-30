import re
with open('uspolygon.txt') as fp:
    Lines = fp.readlines()
    for line in Lines:
        if line[0:12]=='<state name=':
            state=['dict.', re.findall(r'"([^"]*)"', line)[0], '=[']

            print(''.join(state))
        if line[0:11]=='<point lat=':
            coordinate=['{lat:', re.findall(r'"([^"]*)"', line)[0], ', lng:',re.findall(r'"([^"]*)"', line)[1],'},']
            print(''.join(coordinate))

        if (line[0:7]=='</state') and (line[7]!='s'):
            print('];')


