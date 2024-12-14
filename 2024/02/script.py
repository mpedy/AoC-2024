import numpy as np

try:
    with open("02/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

#data = """48 46 47 49 51 54 56
#1 1 2 3 4 5
#1 2 3 4 5 5
#5 1 2 3 4 5
#1 4 3 2 1
#1 6 7 8 9
#1 2 3 4 3
#9 8 7 6 7
#7 10 8 10 11
#29 28 27 25 26 25 22 20"""

data = data.split("\n")

result = []


def control(arr, times=0):
    i = [int(j) for j in arr.split(" ")]
    print(i)
    ok = True
    sign = False
    for j in range(1, len(i)):
        if i[j] == i[j-1]:
            ok = False
            if times == 0:
                times = 1
                return control(" ".join([str(x) for x in [*i[:j], *i[j+1:]]]), times=times) or control(" ".join([str(x) for x in [*i[:j-1], *i[j:]]]), times=times)
            else:
                break
        if sign is False:
            if i[j] == i[j-1]:
                a = 123
            sign = (i[j]-i[j-1])/abs(i[j]-i[j-1])
        if not (abs(i[j]-i[j-1]) >= 1 and abs(i[j]-i[j-1]) <= 3):
            ok = False
            if times == 0:
                times = 1
                return control(" ".join([str(x) for x in [*i[:j], *i[j+1:]]]), times=times) or control(" ".join([str(x) for x in [*i[:j-1], *i[j:]]]), times=times)
            else:
                break
        elif ok:
            if (i[j]-i[j-1])*sign < 0:
                ok = False
                if times == 0:
                    times = 1
                    return control(" ".join([str(x) for x in [*i[:j], *i[j+1:]]]), times=times) or control(" ".join([str(x) for x in [*i[:j-1], *i[j:]]]), times=times) or control(" ".join([str(x) for x in [*i[:j-2], *i[j-1:]]]), times=times)
        if not ok:
            if times == 0:
                times = 1
                return control(" ".join([str(x) for x in [*i[:j], *i[j+1:]]]), times=times) or control(" ".join([str(x) for x in [*i[:j-1], *i[j:]]]), times=times)
            else:
                break
    if ok:
        result.append(i)
        return True
    # else:
    #    print(i)
    return False


for i in data:
    if i == "72 72 73 76 78":
        a = 123
    control(i)

print(len(result))
