with open('config_sw1.txt') as f:
    for line in f:
        if '!' not in line:
            print(line,end="")
