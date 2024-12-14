try:
    with open("14/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

data = data.split("\n")

WIDTH = 101
HEIGHT = 103

WIDTH_HALF = WIDTH//2
HEIGHT_HALF = HEIGHT//2

class Robot:
    def __init__(self, txt):
        txt = txt.split(" ")
        for i in txt:
            i = i.split("=")
            if "p" in i[0]:
                self.x=int(i[1].split(",")[0])
                self.y=int(i[1].split(",")[1])
            if "v" in i[0]:
                self.vx=int(i[1].split(",")[0])
                self.vy=int(i[1].split(",")[1])
    
    def move(self, s=1):
        for i in range(s):
            self.x = (self.x + self.vx) % WIDTH
            self.y = (self.y + self.vy) % HEIGHT
    
    def print(self):
        print(f"{(self.x,self.y)} -> {(self.vx,self.vy)}")

robots = [Robot(i) for i in data]

good_robots = [0,0,0,0] # four quadrants

for robot in robots:
    robot.move(100)
    if robot.x<WIDTH_HALF and robot.y < HEIGHT_HALF:
        good_robots[0] += 1
    elif robot.x<WIDTH_HALF and robot.y > HEIGHT_HALF:
        good_robots[3] += 1
    elif robot.x>WIDTH_HALF and robot.y < HEIGHT_HALF:
        good_robots[1] += 1
    elif robot.x>WIDTH_HALF and robot.y > HEIGHT_HALF:
        good_robots[2] += 1

result = 1
for quadrant in good_robots:
    result = result * quadrant

print(result)
