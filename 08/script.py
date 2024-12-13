try:
    with open("08/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

class Antenna:
    def __init__(self, x, y, symb):
        self.x = x
        self.y = y
        self.symb = symb

    @classmethod
    def sub(self, a, b):
        return (abs(a.x-b.x), abs(a.y-b.y)), (a.x-b.x)>=0, (a.y-b.y)>=0

    def __str__(self):
        return str(self.x) + "," + str(self.y) + " = " + str(self.symb)


matrix = data.split("\n")
dimx = len(matrix[0])
dimy = len(matrix)

antennas = []

for x in range(dimx):
    for y in range(dimy):
        if matrix[y][x] != ".":
            a = Antenna(x, y, matrix[y][x])
            antennas.append(a)

locations = []

for i in antennas:
    for j in antennas:
        if (i.x!=j.x or i.y!=j.y) and i.symb == j.symb:
            ok = True
            pos, signx, signy = Antenna.sub(i,j)
            newloc = [i.x, i.y]
            while ok:
                #newloc = [newloc[0]-pos[0],newloc[1]-pos[1]]
                if signx:
                    newloc[0] = newloc[0]+pos[0]
                else:
                    newloc[0] = newloc[0]-pos[0]
                if signy:
                    newloc[1] = newloc[1]+pos[1]
                else:
                    newloc[1] = newloc[1]-pos[1]
                if newloc[0]>=0 and newloc[0]<dimx and newloc[1]>=0 and newloc[1]<dimy:
                    locations.append((newloc[0],newloc[1]))
                    print(newloc, " from ", i, j, pos, signx, signy)
                else:
                    ok = False

print(list(set(locations)))
print(len(list(set(locations))))

for i in locations:
    t = list(matrix[i[1]])
    t[i[0]] = "#"
    matrix[i[1]] = ("".join(t))

for i in matrix:
    print(i)

symbols = {}
for i in antennas:
    if i.symb in symbols.keys():
        symbols[i.symb][0] = symbols[i.symb][0]+1
        symbols[i.symb][1].append((i.x,i.y))
    else:
        symbols[i.symb] = [1,[(i.x,i.y)]]

for i in symbols.keys():
    if symbols[i][0]>1:
        for pos in symbols[i][1]:
            if not pos in locations:
                locations.append(pos)
print(list(set(locations)))
print(len(list(set(locations))))