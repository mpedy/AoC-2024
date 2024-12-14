from colorama import *

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

def createMatrix(char="."):
    matrix = []
    for i in range(0,HEIGHT):
        res = []
        for j in range(0,WIDTH):
            res.append(char)
        matrix.append(res)
    return matrix

def printMatrix(matrix):
    res = []
    for j in range(len(matrix)):
        res.append(" ".join([str(i) for i in matrix[j]]))
    for row in res:
        row = row.split(" ")
        print(" ".join(f"{str(' '):<{1}}" if str(item) == '0' else Back.RED+Fore.WHITE+f"{str(item):<{1}}"+Style.RESET_ALL for item in row))

def search_continuos_h(matrix, block_len):
    for i in range(len(matrix)):
        l = 0
        for j in range(len(matrix[i])):
            if matrix[i][j]!=0:
                l+=1
                if l>=block_len:
                    return True, (i,j)
            else:
                l=0
        if l>=block_len:
            return True, (i,j)
    return False, (-1,-1)

def search_continuos_v(matrix, block_len):
    for i in range(len(matrix[0])):
        l = 0
        for j in range(len(matrix)):
            if matrix[i][j]!=0:
                l+=1
                if l>=block_len:
                    return True, (i,j)
            else:
                l = 0
    return False, (-1,-1)


import os

seconds = WIDTH*HEIGHT
for robot in robots:
    robot.move(7568)
matrix = createMatrix(0)
for robot in robots:
    robot.move(1)
    matrix[robot.y][robot.x] = matrix[robot.y][robot.x] + 1
#for sec in range(7560,seconds):
#    matrix = createMatrix(0)
#    for robot in robots:
#        robot.move(1)
#        matrix[robot.y][robot.x] = matrix[robot.y][robot.x] + 1
    #found, coords = search_continuos_h(matrix,5)
#    if sec >= 7560:
        #print(chr(27) + "[2J")
os.system("cls")
#print("secondo ", sec,"\n\n")
printMatrix(matrix)

matrix = createMatrix(1)
printMatrix(matrix)