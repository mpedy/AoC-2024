#from numpy import sum

try:
    with open("12/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

DEBUG = False

def _print(*args ,**kwargs):
    if DEBUG:
        return print(args, kwargs)
    return None

print = _print

class Field:
    def __init__(self, data):
        self.data = data
        self.matrix = data.split("\n")
        self.dim = (len(self.matrix), len(self.matrix[0]))
        self.dimx = self.dim[1]
        self.dimy = self.dim[0]
        self.pos = (0, 0)
        self.steps = 0
        self.convert_matrix()
        self._matrix = self.matrix.copy()
        self.areas = {}
        self.ps = {}

    def reset(self):
        self.matrix = self._matrix.copy()

    def popolate(self, l, n):
        for pos in l:
            self.assign((pos[0],pos[1]), n)

    def clean(self, n=0):
        for x in range(self.dimx):
            for y in range(self.dimy):
                self.assign((x, y), n)

    def expand(self, offset, symb=" "):
        for i in range(len(self.matrix)):
            self.matrix[i] = [ord(symb) for _ in range(
                offset)] + self.matrix[i] + [ord(symb) for _ in range(offset)]
        self.matrix.insert(0, [ord(symb) for _ in range(self.dimx + offset*2)])
        self.matrix.append([ord(symb) for _ in range(self.dimx + offset*2)])
        self.dimx = self.dimx+offset*2
        self.dimy = self.dimy+offset*2
        self.dim = [self.dimy, self.dimx]
        self.expanded_offset = offset

    def print(self, literal=True):
        print("\n\n")
        res = []

        def convert(c):
            if c == -1:
                return "."
            elif c == -2:
                return "#"
            else:
                return chr(c)
        for j in range(len(self.matrix)):
            res.append(" ".join([convert(i) if literal else str(i)
                       for i in self.matrix[j]]))
        # print("\n".join(res))
        for row in res:
            row = row.split(" ")
            print(" ".join(f"{str(item):<{2}}" for item in row))

    def convert_matrix(self):
        for i in range(len(self.matrix)):
            self.matrix[i] = [ord(s) for s in self.matrix[i]]

    def get(self, pos=None):
        if pos == None:
            return self.matrix[self.pos[1]][self.pos[0]]
        else:
            # self.set(pos[0], pos[1])
            return self.matrix[pos[1]][pos[0]]

    def cond_up(self, pos):
        # or self.get((pos[0],pos[1]-1))==("#" if not self.is_converted else False)
        return pos[1] == 0

    def cond_down(self, pos):
        # or self.get((pos[0],pos[1]+1))==("#" if not self.is_converted else False)
        return pos[1] == self.dim[0]-1

    def cond_right(self, pos):
        # or self.get((pos[0]+1,pos[1]))==("#" if not self.is_converted else False)
        return pos[0] == self.dim[1]-1

    def cond_left(self, pos):
        # or self.get((pos[0]-1,pos[1]))==("#" if not self.is_converted else False)
        return pos[0] == 0

    def check_pos(self, pos, n):
        return self._check_pos(pos, n)

    def start(self, part1=True, lst = None):
        def check_pos_1(pos, n): return self.get(pos) == n
        def check_pos_2(pos, n): return self.get(pos) != 0
        self._check_pos = check_pos_1 if part1 else check_pos_2
        if not part1:
            for x in range(self.dimx):
                for y in range(self.dimy):
                    if (self.get((x, y)) != 0 and self.get((x,y))!=-2 and (x,y) not in lst):
                        key = f"{(x,y)}_{(self.get((x,y)))}"
                        self.areas[key] = [(x, y)]
                        self.ps[key] = self.calculate_fence_part2(x, y, self.get((x, y)), key, lst)
                        #for pos in self.areas[key]:
                        #    self.assign(pos, -2)
        else:
            for x in range(self.dimx):
                for y in range(self.dimy):
                    if (self.get((x, y)) != -1 and self.get((x, y)) != -2):
                        key = f"{(x,y)}_{chr(self.get((x,y)))}"
                        self.areas[key] = [(x, y)]
                        self.ps[key] = self.calculate_fence(x, y, self.get((x, y)), key)
                        for pos in self.areas[key]:
                            self.assign(pos, -2)

    def assign(self, pos, elem):
        t = list(self.matrix[pos[1]])
        t[pos[0]] = elem
        self.matrix[pos[1]] = t
        self.assigned = pos

    def calculate_fence_part2(self, x, y, n, key,lst, a=1, p=0):
        self.assign((x, y), 0)
        if not self.cond_up((x,y)) and self.get((x, y-1))!=0 and (x,y-1) not in lst:
            a += 1
            self.areas[key].append((x, y-1))
            p = self.calculate_fence_part2(x, y-1, n, key,lst, a, p)
        if not self.cond_down((x,y)) and self.get((x, y+1))!=0 and (x,y+1) not in lst:
            a += 1
            self.areas[key].append((x, y+1))
            p = self.calculate_fence_part2(x, y+1, n, key,lst, a, p)
        if not self.cond_left((x,y)) and self.get((x-1, y))!=0 and (x-1,y) not in lst:
            a += 1
            self.areas[key].append((x-1, y))
            p = self.calculate_fence_part2(x-1, y, n, key,lst, a, p)
        if not self.cond_right((x,y)) and self.get((x+1, y))!=0 and (x+1,y) not in lst:
            a += 1
            self.areas[key].append((x+1, y))
            p = self.calculate_fence_part2(x+1, y, n, key,lst, a, p)
        return p

    def calculate_fence(self, x, y, n, key, a=1, p=0):
        self.assign((x, y), -1)
        if not self.cond_up((x, y)):
            if self.check_pos((x, y-1), n):
                a += 1
                self.areas[key].append((x, y-1))
                p = self.calculate_fence(x, y-1, n, key, a, p)
            elif self.get((x, y-1)) != -1:
                print("fence up ", x, y, chr(n))
                p += 1
        else:
            print("Non più su", x, y, chr(n))
            p += 1
        if not self.cond_down((x, y)):
            if self.check_pos((x, y+1), n):
                a += 1
                self.areas[key].append((x, y+1))
                p = self.calculate_fence(x, y+1, n, key, a, p)
            elif self.get((x, y+1)) != -1:
                print("fence down", x, y, chr(n))
                p += 1
        else:
            print("non più giù", x, y, chr(n))
            p += 1
        if not self.cond_left((x, y)):
            if self.check_pos((x-1, y), n):
                a += 1
                self.areas[key].append((x-1, y))
                p = self.calculate_fence(x-1, y, n, key, a, p)
            elif self.get((x-1, y)) != -1:
                print("fence left", x, y, chr(n))
                p += 1
        else:
            print("non più left", x, y, chr(n))
            p += 1
        if not self.cond_right((x, y)):
            if self.check_pos((x+1, y), n):
                a += 1
                self.areas[key].append((x+1, y))
                p = self.calculate_fence(x+1, y, n, key, a, p)
            elif self.get((x+1, y)) != -1:
                print("fence right", x, y, chr(n))
                p += 1
        else:
            print("non più right", x, y, chr(n))
            p += 1
        return p


f = Field(data)
f.start()

print(f.areas)
print(f.ps)

# calculate price

price = 0

for key in f.ps.keys():
    price = price + (f.ps[key]*len(f.areas[key]))
print(price)


# seconda parte - calcolo dei lati

f.reset()
expand = 1
f.expand(expand, chr(0))

all_areas = f.areas.copy()
all_ps = f.ps.copy()
keys_areas = all_areas.keys()
sides = {}
for k in keys_areas:
    points, elem = all_areas[k], ord(k.split("_")[1])
    points = [(x+expand,y+expand) for x,y in points]
    #f.print(False)
    # cleaning matrix
    f.clean()
    # popolating matrix
    f.popolate(points, elem)
    print(k.split("_")[1])
    for p in points:
        x, y = p[0], p[1]
        # Up
        if f.get((x, y-1)) != elem:
            f.assign((x, y-1), f.get((x, y-1))+1)
        # Down
        if f.get((x, y+1)) != elem:
            f.assign((x, y+1), f.get((x, y+1))+1)
        # Right
        if f.get((x+1, y)) != elem:
            f.assign((x+1, y), f.get((x+1, y))+1)
        # Left
        if f.get((x-1, y)) != elem:
            f.assign((x-1, y), f.get((x-1, y))+1)
    f.areas = {}
    f.ps = {}
    oldmatrix = f.matrix.copy()
    f.start(part1=False,lst=points)
    f.matrix = oldmatrix
    f.print(False)
    sides[k] = 0


    # second method
    for y in range(f.dimy):
        all_up, all_down = 0,0
        s_up, s_down = 0,0
        for x in range(f.dimx):
            if (x,y) in points:
                up_elem = f.get((x,y-1))
                down_elem = f.get((x,y+1))
                if up_elem!=elem:
                    s_up = 1
                if up_elem==elem and s_up == 1:
                    sides[k] += 1
                    all_up += 1
                    s_up = 0
                
                if down_elem != elem:
                    s_down = 1
                if down_elem == elem and s_down == 1:
                    sides[k] += 1
                    all_down += 1
                    s_down = 0
            if (x,y) not in points:
                if s_up==1:
                    sides[k] += 1
                    s_up = 0
                    all_up += 1
                if s_down==1:
                    sides[k]+=1
                    s_down = 0
                    all_down+=1
        print(sides[k],all_up,all_down,0,0)
        sides[k] = sides[k]+s_up + s_down
    
    f.print(False)

    for x in range(f.dimx):
        all_left, all_right = 0,0
        s_left, s_right = 0,0
        for y in range(f.dimy):
            if (x,y) in points:
                left_elem = f.get((x-1,y))
                right_elem = f.get((x+1,y))
                if left_elem!=elem:
                    s_left = 1
                if left_elem==elem and s_left == 1:
                    sides[k] += 1
                    all_left += 1
                    s_left = 0
                
                if right_elem != elem:
                    s_right = 1
                if right_elem == elem and s_right == 1:
                    sides[k] += 1
                    all_right += 1
                    s_right = 0
            if (x,y) not in points:
                if s_left==1:
                    sides[k] += 1
                    s_left = 0
                    all_left += 1
                if s_right==1:
                    sides[k]+=1
                    s_right = 0
                    all_right+=1
        print(sides[k],0,0,all_left,all_right)
        sides[k] = sides[k]+s_left + s_right

print(sides)

# calculate price

price = 0
for key in sides.keys():
    price = price + (sides[key]*len(all_areas[key]))

print(price)