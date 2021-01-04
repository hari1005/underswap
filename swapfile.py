def swapData():
    fileA=input('enter file name here:')
    fileB=input('enter the other file here:')
    with open(fileA,'r') as a:
        data_a=a.read()
    with open(fileB,'r') as a:
        data_b=a.read()
    with open(fileA,'w') as a:
        a.write(data_a)
    with open(fileB,'w') as a:
        a.write(data_b)

swapData()