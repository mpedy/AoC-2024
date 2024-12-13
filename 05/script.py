import numpy as np
import re
from z3 import *

try:
    with open("05/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()
rules = data.split("\n\n")[0].split("\n")
pages = data.split("\n\n")[1].split("\n")
numbers = list(set(data.split("\n\n")[0].replace("|", ",").replace("\n", ",").split(",")))
myvars = {}

def find_chain(n):
    chain = []
    n = int(n)
    for i in rules:
        ii = i.split("|")
        if n == int(ii[0]) or n==int(ii[1]):
            chain.append(i)
            n = int(ii[0]) if int(ii[1])==n else int(ii[1])
        #if i[:len(n)]==n:
        #    chain.append(i)
        #    n = i[len(n)+1:]
        #    print(n)
    return chain

def find_all_chain_v1(pages):
    result = []
    for p in pages:
        for i in rules:
            ii = i.split("|")
            if ii[0]==p or ii[1]==p:
                result.append(i)
    result = list(set(result))
    return result

def find_all_chain_v2(pages):
    result = []
    for page in range(1,len(pages)):
        for i in rules:
            if i == f"{pages[page-1]}|{pages[page]}" or i == f"{pages[page]}|{pages[page-1]}":
                result.append(i)
    result = list(set(result))
    return result

def load_vars():
    for i in numbers:
        myvars[i] = Int(f"{i}")

s = Solver()
load_vars()
#s.add(Distinct(list(myvars.values())))

# Save clean state
s.push()

corrects = []
incorrects = []
for p in range(len(pages)):
    pags = pages[p].split(",")
    constraints = find_all_chain_v2(pags)
    for c in constraints:
        c = c.split("|")
        s.add(myvars[c[0]]<myvars[c[1]])
    for page in range(1,len(pags)):
        s.add(myvars[pags[page-1]] < myvars[pags[page]])
    print("Pagina ", p, s.check())
    if s.check() == sat:
        corrects.append(p)
    else:
        incorrects.append(p)
    s.pop()
    s.push()

result = 0
for c in corrects:
    page = pages[c].split(",")
    result += int(page[len(page)//2])
    print(page, "Aggiungendo ", int(page[len(page)//2]))
print(result)



# parte due

def myswap(l, n1, n2):
    t = l[n1]
    l[n1] = l[n2]
    l[n2] = t
    return l

sorted_pages = []
for incorrect in incorrects:
    pageline = pages[incorrect].split(",")
    constraints = find_all_chain_v1(pageline)
    sorted = False
    index = 0
    while sorted is False:
        if index == len(pageline)-1:
            sorted = True
            break
        paragone = pageline[index]
        index1 = index
        while index1 < len(pageline)-1:
            index1 = index1 + 1
            paragone_1 = pageline[index1]
            for c in constraints:
                c = c.split("|")
                if c[0]==paragone_1 and c[1]==paragone:
                    pageline = myswap(pageline,index,index1)
                    index = 0
                    paragone = pageline[index]
                    index1 = 0
                    break
        index = index + 1
    print(pageline)
    sorted_pages.append(pageline)

print(sorted_pages)
result = 0
for page in sorted_pages:
    result += int(page[len(page)//2])
    print(page, "Aggiungendo ", int(page[len(page)//2]))
print(result)