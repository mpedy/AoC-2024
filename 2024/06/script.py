try:
    with open("06/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()


class Guardian:
    def __init__(self, data):
        self.data = data
        self.matrix = data.split("\n")
        self.dim = (len(self.matrix), len(self.matrix[0]))
        self.dimx = self.dim[1]
        self.dimy = self.dim[0]
        self.pos = (0, 0)
        self.moving_direction = "up"
        self.moving_directions = ["up", "right", "down", "left"]
        self.moving_direction_symbol = "^"
        self.moving_direction_symbols = ["^", ">", "v", "<"]
        self.steps = 0
        self.assigned = None
        self.get_initial_point()
        self.starting_point = self.pos
        self.all_steps = [self.pos]
        self.all_steps_1 = [f"{self.pos}_up"]
        self.corner_steps = [{"starting_up": self.pos}]
        self.convert_matrix()
        self.is_converted = True
    
    def convert_matrix(self):
        def convert(symbol):
            return True if symbol != "#" else False
        for i in range(len(self.matrix)):
            self.matrix[i] = [convert(s) for s in self.matrix[i]]

    
    def reset(self):
        self.pos = self.starting_point
        self.steps = 0
        self.all_steps = [self.pos]
        self.all_steps_1 = [f"{self.pos}_up"]
        self.corner_steps = [{"starting_up": self.pos}]
        self.matrix = data.split("\n")
        self.moving_direction = "up"
        self.moving_direction_symbol = "^"
        if self.is_converted:
            self.convert_matrix()


    def get_initial_point(self):
        for i in range(self.dimx):
            for j in range(self.dimy):
                if self.get((i, j)) in self.moving_direction_symbols:
                    self.pos = (i, j)
                    self.moving_direction_symbol = self.get((i, j))
                    self.get_moving_direction()
                    return

    def get_moving_direction(self):
        self.moving_direction = self.moving_directions[self.moving_direction_symbols.index(
            self.moving_direction_symbol)]

    def get(self, pos=None):
        if pos == None:
            return self.matrix[self.pos[1]][self.pos[0]]
        else:
            #self.set(pos[0], pos[1])
            return self.matrix[pos[1]][pos[0]]
    
    def set(self,pos):
        self.steps = self.steps + 1
        self.all_steps.append(pos)
        self.pos = (pos[0],pos[1])
        if f"{self.pos}_{self.moving_direction}" in self.all_steps_1:
            raise Exception("Too many steps!", self.assigned, self.steps >= self.dimx*self.dimy*2, f"{self.pos}_{self.moving_direction}" in self.all_steps_1)
        self.all_steps_1.append(f"{pos}_{self.moving_direction}")
    
    def assign(self, pos, elem):
        t = list(self.matrix[pos[1]])
        t[pos[0]] = elem
        self.matrix[pos[1]] = ("".join(t) if not self.is_converted else t)
        self.assigned = pos

    def move(self):
        def cond_up(pos):
            return pos[1]==0 or self.get((pos[0],pos[1]-1))==("#" if not self.is_converted else False)
        def cond_down(pos):
            return pos[1]==self.dim[0]-1 or self.get((pos[0],pos[1]+1))==("#" if not self.is_converted else False)
        def cond_right(pos):
            return pos[0]==self.dim[1]-1 or self.get((pos[0]+1,pos[1]))==("#" if not self.is_converted else False)
        def cond_left(pos):
             return pos[0]==0 or self.get((pos[0]-1,pos[1]))==("#" if not self.is_converted else False)
        
        oldstep = -1
        while self.pos[0]!=self.dimx-1 and self.pos[1]!=self.dimy-1 and self.pos[0]!=0 and self.pos[1] != 0:
            #if self.steps == oldstep:
            #    print("Nessun passo fatto!")
            oldstep = self.steps
            if self.moving_direction == "up":
                while not cond_up(self.pos):
                    self.set((self.pos[0],self.pos[1]-1))
                self.corner_steps.append({"up": self.pos})
                self.moving_direction = "right"
            elif self.moving_direction == "right":
                while not cond_right(self.pos):
                    self.set((self.pos[0]+1,self.pos[1]))
                self.corner_steps.append({"right" : self.pos})
                self.moving_direction = "down"
            elif self.moving_direction == "down":
                while not cond_down(self.pos):
                    self.set((self.pos[0],self.pos[1]+1))
                self.corner_steps.append({"down" : self.pos})
                self.moving_direction = "left"
            elif self.moving_direction == "left":
                while not cond_left(self.pos):
                    self.set((self.pos[0]-1,self.pos[1]))
                self.corner_steps.append({"left" : self.pos})
                self.moving_direction = "up"
        #print("Finito in ", len(self.all_steps), " di cui unici ", len(list(set(self.all_steps))))
            
g = Guardian(data)
initial_point = g.pos
g.move()
print("Finito in ", len(g.all_steps), " di cui unici ", len(list(set(g.all_steps))))

# parte due

g1 = Guardian(data)
loops_created = 0

for step in list(set(g.all_steps)):
    x = step[0]
    y = step[1]
    if (x,y)!= initial_point:
        if (x,y) == (3,6):
            asdasd=  1
        g1.reset()
        if g1.get((x,y))==("." if not g1.is_converted else True):
            g1.assign((x,y),("#" if not g1.is_converted else False ))
            try:
                g1.move()
                #print(g.assigned, "Finito in ", len(g.all_steps), " di cui unici ", len(list(set(g.all_steps))))
            except Exception as e:
                print(e)
                loops_created = loops_created+1
            #finally:
            #    g1.reset()
print("Loop creati: ",loops_created)
