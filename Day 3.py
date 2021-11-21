import numpy as np

a = open('day3.txt', 'r')
f = a.readlines()
#part 1
line = f[0].split("\n")
tam = len(line[0])
result = 0
for i in range(1,len(f)):
    line = f[i].split("\n")
    line = line[0]
    pos = np.mod(3*i,tam)
    if "#" in line[pos]:
        result += 1
print(result)


#part 2
list = [1,3,5,7,1]
list2 = [1,1,1,1,2]
result = 1
for j in range(len(list)):
    line = f[0].split("\n")
    tam = len(line[0])
    result2 = 0
    print('---------------')
    for i in range(1,len(f),list2[j]):
        line = f[i].split("\n")
        line = line[0]
        pos = np.mod(list[j]*i,tam)
        print(pos)
        if "#" in line[pos]:
            result2 += 1
    print(result2)
    result = result*result2
print(result)
