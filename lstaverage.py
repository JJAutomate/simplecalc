numL=list()
while (True):
    ipm=input('enter number: ')
    if ipm=='done': break
    value= float(ipm)
    numL.append(value)
average=sum(numL)/len(numL)
print('Average is, ', average)
