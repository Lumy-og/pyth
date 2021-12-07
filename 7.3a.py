ignore = [1, 2, 3, 4, 5, 6, 7, 8, 9]
h = []
g = []
o = 0
with open('CAM_table.txt', 'r') as text:   
    ospf = text.readlines()   
    for lines in ospf:  
        for i in range(len(ignore)):
            if 'Gi' not in lines:
                lines = '!'
        if lines[0] != '!':
            h.append((lines.strip()) + '\n')
for i in range(len(h)):
    d = h[i].split()
    g.append(int(d[0]))
g.sort()
for i in range(len(h)):
    d = h[i].split()
    vlan = g[o]   
    mac = d[1]   
    ports = d[3]  
    ospf_route = f""" {vlan:<6}   {mac:<16}   {ports:<} """  
    print(ospf_route, end = '\n')
    o += 1
