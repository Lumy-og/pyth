import sys
f=sys.argv[1]
a=open(config_sw1.txt,'r')
for i in a:
    if "i" !=i[0]:
        print(i,end="")
