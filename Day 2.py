import numpy as np


a = open('day2.txt', 'r')
f = a.readlines()
### part 1
result = 0
for i in range(len(f)):
    line = f[i]
    x = line.split(" ")
    x1 = x[0].split("-")
    n1 = int(x1[0])
    n2 = int(x1[1])
    x1 = x[1].split(":")
    let = x1[0]
    x1 = x[2].split("\n")
    passw = x1[0]
    n = passw.count(let)
    if n <= n2 and n >= n1:
        result += 1
print(result)

### part 2
result = 0
for i in range(len(f)):
    line = f[i]
    x = line.split(" ")
    x1 = x[0].split("-")
    n1 = int(x1[0])
    n2 = int(x1[1])
    x1 = x[1].split(":")
    let = x1[0]
    x1 = x[2].split("\n")
    passw = x1[0]
    count = 0
    if let in passw[n1-1]:
        count += 1
    if let in passw[n2-1]:
        count += 1
    if count == 1:
        result += 1
print(result)