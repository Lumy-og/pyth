def parse_cdp_neighbors():
    f=open('sh_cdp_n_sw1.txt', 'r')
    with f as fin:
        dict1 = {}
        dict2 = {}
        marker = False
        for i in fin.readlines():
            if 'show cdp neighbors' in i:
                key1 = i[:i.find('>')]
                dict1[key1] = []
                continue
            if 'Device ID' in i:
                marker = True
                continue
            if marker:
                value1 = ''.join(i.split()[1:3])
                dict1[key1].append(value1)
                key2 = i[:i.find(' ')]
                value2 = ''.join(i.split()[-1:-3:-1])
                dict2[key2] = value2
    return (dict1, dict2)

            

print(*parse_cdp_neighbors(), sep='\n')
