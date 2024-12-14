import numpy as np
import re

try:
    with open("03/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

#data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
finds = re.findall("mul\(\d{1,3},\d{1,3}\)", data)

result = 0
for f in finds:
    a = int(f[f.index("mul")+4:f.index(",")])
    b = int(f[f.index(",")+1:-1])
    result += (a*b)

print(result)

## seconda parte
result = 0

#data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
finds = re.findall("(mul\(\d{1,3},\d{1,3}\))|(don't\(\))|(do\(\))",data)

enabled = True
for fi in finds:
    if len(fi[1])>0:
        enabled = False
    if len(fi[2])>0:
        enabled = True
    if enabled:
        if(len(fi[0]))>0:
            f = fi[0]
            a = int(f[f.index("mul")+4:f.index(",")])
            b = int(f[f.index(",")+1:-1])
            result += (a*b)
print(result)
