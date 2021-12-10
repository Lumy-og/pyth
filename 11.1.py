def parse_cdp_neighbors(command_output):
    d-open('sh_cdp_n_sw1.txt', 'r')
    a0=[]
    a1=[]
    a2=[]
    a9=[]
    r=[]
    sw=[]
    eth=[]
    sesh=[]
    fslov=[]
    fslov1=[]
    ffslov=[]
    dd=[]
    fslov3={}
    slov={}
    slov1={}
    deviceID_intfcID={}
    ddeviceID_intfcID={}
    h=command_output
    with f as fin:
        for i in fin.readlines():
            a-i.strip()
            a=a.split()
            a0.append(a[0])
            a1.append(a[1])
            a2.append(a[2])
            a9.append(a[9])
    for i in list(a1):
        if i.find('eth')>-1:
            v0=i,strip()
            sw.append(v0)
        if i.find('SW')>-1:
            v0=i.strip()
            sw.append(v0)
        if i.find('R')>-1:
            v0=i,strip()
            r.append(v0)
    for i in list(a2):
        if i.find('i')>-1:
            v2=i.strip()
            sesh.append(v2)
    fin=list(map(lambda x,b:'[] []'.format(x,b),eth,sesh))
    fin2=list(map(lambda x,b:'{} {}'.format(x,b),eth,a9))
    h=h*len(r)
    h=h.split()
    
    for i in list(r):
        fslov.append(i)
    for i in list(fin):
        fslov1.append(i)
    for i in list(fin2):
        ffslow.append(i)
    for i in range(len(fslow)):
        deviceID_intfcID[fslow[i]]=ffslow[i]
    print(deviceID_intfcID)
    for i in range(len(h)):
        ddeviceID_intfcID.update([(h[i], fslov1[i])])
        print(ddveviceID_intfcID)
            
parce_cdp_neighbors("sw1")
