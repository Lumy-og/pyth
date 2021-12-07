f= open('ospf.txt', 'r')
lines=f.readlines()
for i in range(len(lines)): 
    lines[i]=lines[i].split() 
for i in lines: 
    print('Prefix   ', i[1]) 
    print('AD/Metric    ', i[2]) 
    print('Next Hop ', i[4]) 
    print('Last update  ', i[5]) 
    print('outbound Interface   ',i[0]) 
    print() 

