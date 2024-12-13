from numpy import sum

try:
    with open("10/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()


class Hiking:
    def __init__(self, data):
        self.data = data
        self.matrix = data.split("\n")
        self.dim = (len(self.matrix), len(self.matrix[0]))
        self.dimx = self.dim[1]
        self.dimy = self.dim[0]
        self.pos = (0, 0)
        self.steps = 0
        self.convert_matrix()
        self.founds = {}

    def convert_matrix(self):
        for i in range(len(self.matrix)):
            self.matrix[i] = [int(s) if s in ["0","1","2","3","4","5","6","7","8","9"] else -1 for s in self.matrix[i]]

    def get(self, pos=None):
        if pos == None:
            return self.matrix[self.pos[1]][self.pos[0]]
        else:
            # self.set(pos[0], pos[1])
            return self.matrix[pos[1]][pos[0]]

    def start(self):
        for x in range(self.dimx):
            for y in range(self.dimy):
                if self.get((x, y)) == 0:
                    self.move(x, y, 0, (x, y))

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

    def move(self, x, y, n, orig):
        if self.get((x, y)) == 9:
            key = f"{orig}-{(x,y)}"
            if key in self.founds.keys():
                self.founds[key] = self.founds[key]+1
            else:
                self.founds[key] = 1
            return
        if not self.cond_right((x, y)) and self.get((x+1, y)) == n+1:
            self.move(x+1, y, n+1, orig)
        if not self.cond_left((x, y)) and self.get((x-1, y)) == n+1:
            self.move(x-1, y, n+1, orig)
        if not self.cond_up((x, y)) and self.get((x, y-1)) == n+1:
            self.move(x, y-1, n+1, orig)
        if not self.cond_down((x, y)) and self.get((x, y+1)) == n+1:
            self.move(x, y+1, n+1, orig)


h = Hiking(data)

h.start()

print(len(h.founds.keys()))
print(sum(list(h.founds.values())))