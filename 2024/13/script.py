from z3 import *

try:
    with open("13/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

data = data.split("\n\n")


class Button:
    def __init__(self, _type, x=None, y=None):
        self.type = _type
        self.x = x
        self.y = y
        self.cost = 3 if _type == "A" else 1


class Prize:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


na = Int("N_a")
nb = Int("N_b")

s = Optimize()

# s.add(na <= 100, nb <= 100) seconda parte

used_tokens = 0

for problem in data:
    s.push()
    problem = problem.split("\n")
    btns = []
    for i in problem:
        if "Button" in i:
            btn_type, ops = i[7:7+1], i[9:].split(",")
            b1 = Button(btn_type)
            for op in ops:
                if "X" in op:
                    op = op.replace("X", "")
                    b1.x = int(op)
                if "Y" in op:
                    op = op.replace("Y", "")
                    b1.y = int(op)
            btns.append(b1)
        if "Prize" in i:
            p = Prize()
            i = i.split(": ")[1].split(", ")
            for coord in i:
                if "X" in coord:
                    p.x = int(coord[2:]) + 10000000000000 # seconda parte
                if "Y" in coord:
                    p.y = int(coord[2:]) + 10000000000000 # seconda parte
    if btns[0].type == "A":
        s.add(na*btns[0].x + nb*btns[1].x == p.x,
              na*btns[0].y + nb*btns[1].y == p.y)
    else:
        s.add(na*btns[1].x+nb*btns[0].x == p.x,
              na*btns[1].y+nb*btns[0].y == p.y)
    s.minimize(3*na+nb)
    status = s.check()
    m = s.model()
    print(m)
    if status == sat:
        used_tokens = used_tokens + 3*m[na].as_long() + m[nb].as_long()
    s.pop()

print(used_tokens)