import numpy as np

with open("input.txt","r") as file:
    data = file.read()

data = data.split("\n")
list1 = []
list2 = []
for i in data:
    d = i.split(" ")
    list1.append(int(d[0]))
    list2.append(int(d[-1]))



#list1 = [3,4,2,1,3,3]
#list2 = [4,3,5,3,9,3]

assert len(list1) == len(list2)


result = []

for i in range(0,len(list1)):
    a = np.min(list1)
    b = np.min(list2)
    result.append(abs(a-b))
    list1.remove(a)
    list2.remove(b)

print(np.sum(result))