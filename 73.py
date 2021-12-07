f=open('CAM_table.txt', 'r')
lines=f.readlines()
for i in range (len(lines)):
    lines[i]=lines[i].split()
out=""
for i in range(6,len(lines)):
    out+=lines[i][0]+' '*(9-len(lines[i][0]))+lines[i][1]+' '*6+lines[i][3]+'\n'
print(out)
