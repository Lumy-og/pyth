with open('config_sw1.txt') as f, open('result.txt', 'w') as g:
    ignore=["duplex", "alias", "configuration", "!"]
    for line in f:
        flag=True
        for i in ignore:
            if i in line:
                flag=False
        if flag:
            print(line,end="")
            g.write(line)
