import numpy as np


a = open('day1.txt', 'r')
f = a.readlines()
## part 1
for i in range(len(f)):
    for j in range(i,len(f)):
        sum = int(f[i]) + int(f[j])
        if sum == 2020:
            result = int(f[i]) * int(f[j])
            print(result)

## part 2
for i in range(len(f)):
    for j in range(i,len(f)):
        for k in range(j, len(f)):
            sum = int(f[i]) + int(f[j]) + int(f[k])
            if sum == 2020:
                result = int(f[i]) * int(f[j]) * int(f[k])
                print(result)
