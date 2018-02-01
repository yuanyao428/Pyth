strin = input("");
list1 = []
for i in range(0, len(strin)):
    list1.append(strin[i])
countstart = 0
countend = 0
length = len(list1)
for i in range(0, length):
if list1[i] == '0':
    countstart += 1
else:
    break
j = length - 1
while j >= 0:
    if list1[j] == '0':
        countend += 1
    else:
        break
    j -= 1
if countstart >= countend:
    m = length - countend - 1
    countend1 = 0
    while length >= 0:
        if list1[m] == '1':
            countend1 += 1
        else:
            break
        m -= 1
    for i in range(countstart + 1, length - countend - countend1):
        if list(countstart + 1) == '0':

            
    

