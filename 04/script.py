import numpy as np
import re

try:
    with open("04/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

class WordSearch:
    def __init__(self,data, word):
        self.data = data
        self.matrix = data.split("\n")
        self.dim = (len(self.matrix),len(self.matrix[0]))
        self.pos = (0,0)
        self.word = word
        self.index = 0
        self.founds = []
    def set(self,x,y):
        if x>=0 and x<self.dim[1] and y>=0 and y<self.dim[0]:
            self.pos = (x,y)
        else:
            raise Exception("Fuori range")
    def get(self, pos = None):
        if pos == None:
            return self.matrix[self.pos[1]][self.pos[0]]
        else:
            self.set(pos[0],pos[1])
            return self.matrix[self.pos[1]][self.pos[0]]
    def search(self,word):
        for y in range(0,self.dim[0]):
            for x in range(0,self.dim[1]):
                if self.get((x,y))==word[0]:
                    # prima lettera trovata
                    #self.search_word("up", (x,y),1)
                    #self.search_word("down", (x,y),1)
                    #self.search_word("left", (x,y),1)
                    #self.search_word("right", (x,y),1)
                    self.search_word("up right", (x,y),1, [(x,y)])
                    self.search_word("up left", (x,y),1, [(x,y)])
                    self.search_word("down right", (x,y),1, [(x,y)])
                    self.search_word("down left", (x,y),1, [(x,y)])
    def search_word(self,mode,pos,index=0,history=None):
        def cond_up(w,pos):
            return pos[1]==0
        def cond_down(w,pos):
            return pos[1]==self.dim[0]-1
        def cond_right(w,pos):
            return pos[0]==self.dim[1]-1
        def cond_left(w,pos):
             return pos[0]==0
        if index == len(self.word):
            self.founds.append({"direction": mode, "pos": pos, "history": history})
            return
        if mode == "up":
            if cond_up(self.word[index:],pos):
                return
            else:
                if self.get((pos[0],pos[1]-1))==self.word[index]:
                    history.append((pos[0],pos[1]-1))
                    return self.search_word("up",(pos[0],pos[1]-1),index+1,history)
        if mode == "down":
            if cond_down(self.word[index:],pos):
                return
            else:
                if self.get((pos[0],pos[1]+1))==self.word[index]:
                    history.append((pos[0],pos[1]+1))
                    return self.search_word("down",(pos[0],pos[1]+1),index+1,history)
        if mode == "right":
            if cond_right(self.word[index:],pos):
                return
            else:
                if self.get((pos[0]+1,pos[1]))==self.word[index]:
                    history.append((pos[0]+1,pos[1]))
                    return self.search_word("right",(pos[0]+1,pos[1]),index+1,history)
        if mode == "left":
            if cond_left(self.word[index:],pos):
                return
            else:
                if self.get((pos[0]-1,pos[1]))==self.word[index]:
                    history.append((pos[0]-1,pos[1]))
                    return self.search_word("left",(pos[0]-1,pos[1]),index+1,history)
        if mode == "up right":
            if cond_up(self.word[index:],pos) or cond_right(self.word[index:],pos):
                return
            else:
                if self.get((pos[0]+1,pos[1]-1))==self.word[index]:
                    history.append((pos[0]+1,pos[1]-1))
                    return self.search_word("up right", (pos[0]+1,pos[1]-1),index+1,history)
        if mode == "up left":
            if cond_up(self.word[index:],pos) or cond_left(self.word[index:],pos):
                return
            else:
                if self.get((pos[0]-1,pos[1]-1))==self.word[index]:
                    history.append((pos[0]-1,pos[1]-1))
                    return self.search_word("up left", (pos[0]-1,pos[1]-1),index+1,history)
        if mode == "down left":
            if cond_down(self.word[index:],pos) or cond_left(self.word[index:],pos):
                return
            else:
                if self.get((pos[0]-1,pos[1]+1))==self.word[index]:
                    history.append((pos[0]-1,pos[1]+1))
                    return self.search_word("down left", (pos[0]-1,pos[1]+1),index+1,history)
        if mode == "down right":
            if cond_down(self.word[index:],pos) or cond_right(self.word[index:],pos):
                return
            else:
                if self.get((pos[0]+1,pos[1]+1))==self.word[index]:
                    history.append((pos[0]+1,pos[1]+1))
                    return self.search_word("down right", (pos[0]+1,pos[1]+1),index+1,history)

                

wordSearch = WordSearch(data,"MAS")
wordSearch.search("MAS")

for i in wordSearch.founds:
    assert "".join([wordSearch.get(j) for j in i["history"]]) == "MAS"

foundXs = 0
foundXs_list = []
for found in wordSearch.founds:
    if not found in foundXs_list or True:
        for j in wordSearch.founds:
            if found["direction"] == "down right" and (
                (j["direction"]=="up right" and j["history"][0][1]==found["history"][0][1]+2 and j["history"][0][0]==found["history"][0][0]) or 
                (j["direction"]=="down left" and j["history"][0][0]==found["history"][0][0]+2 and j["history"][0][1]==found["history"][0][1])
            ):
                foundXs += 1
                foundXs_list.append((found,j))
            elif found["direction"] == "down left" and (
                (j["direction"]=="up left" and j["history"][0][1]==found["history"][0][1]+2) and j["history"][0][0]==found["history"][0][0]):
                foundXs += 1
                foundXs_list.append((found,j))
            elif found["direction"] == "up left" and (
                (j["direction"]=="up right" and j["history"][0][0]==found["history"][0][0]-2 and j["history"][0][1]==found["history"][0][1])):
                foundXs += 1
                foundXs_list.append((found,j))