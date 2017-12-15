fname=open('mboxshort.txt')
for line in fname:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    print(words[3]) #at [2] will print the day where line
    #starts with FROM
