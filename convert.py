filename = 'Lep.txt'
f = open(filename)
lines=f.readlines()
f.close()
lines = lines[129:len(lines)]
filename = 'LepShort.txt'
with open(filename, 'w') as f:
    for i in range(0,len(lines)):
        f.write(lines[i])
f.close()


