han = open('file.txt')

for line in han:
    line = line.rstrip()
    #print('Line:', line)
    if line == '' :
        continue
    wds = line.split()
    #print('Words:', wds)
    #Guardian
    if len(wds) < 1 :
        continue
    if wds[0] != 'The' :
        #print("Ignore")
        continue
    print(wds[2])
