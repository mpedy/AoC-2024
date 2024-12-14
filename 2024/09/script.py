try:
    with open("09/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

data = [int(d) for d in data]
ids = -1
is_a_file = True


space = []

for n in data:
    if is_a_file:
        ids = ids + 1
        for _ in range(n):
            space.append(str(ids))
    else:
        for _ in range(n):
            space.append(str("."))
    is_a_file = not is_a_file

old_space = space.copy()

print("".join(space))
last_pos = -1
for i in range(len(space)-1,-1,-1):
    if i<=last_pos:
        break
    if space[i] != ".":
        for j in range(0,i):
            if space[j]==".":
                space[j]=space[i]
                space[i]="."
                last_pos = j
                break

print("".join(space))

#calculate checksum
checksum = 0

for i in range(len(space)):
    if space[i] != ".":
        checksum += int(space[i])*i
    else:
        break

print(checksum)


# seconda parte

space = old_space.copy()

print("".join(space))

last_pos = 0
i = ids+1
while i >0:
    i = i-1
    len_space = 0
    len_blocco = len(list(filter(lambda x : x==str(i),space)))
    last_pos = space.index(str(i))
    found = False
    j=0
    while j < len(space)-1:
        if found:
            break
        j = j+1
        if j > last_pos:
            break
        if space[j]==".":
            for j1 in range(j+1,len(space)):
                if space[j1]!=".":
                    len_space = j1-j
                    break
            if len_space > 0 and len_space >= len_blocco:
                found = True
                for j2 in range(j,j+len_blocco):
                    space[j2]=str(i)
                for j2 in range(j+len_space,len(space)):
                    if space[j2]==str(i):
                        space[j2]="."

print("".join(space))

# calculate checksum
#calculate checksum
checksum = 0

for i in range(len(space)):
    if space[i] != ".":
        checksum += int(space[i])*i

print(checksum)