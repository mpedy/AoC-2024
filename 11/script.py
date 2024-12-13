try:
    with open("11/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

data = data.split(" ")


class Stone:
    def __init__(self, n, ntimes = 1):
        self.n = int(n)
        self.ntimes = ntimes

    def evolve(self):
        if self.n == 0:
            self.n = 1
            return [self]
        elif len(str(self.n)) % 2 == 0:
            return [Stone(str(self.n)[:len(str(self.n))//2], self.ntimes), Stone(str(self.n)[len(str(self.n))//2:], self.ntimes)]
        else:
            self.n = self.n*2024
            return [self]

    def __str__(self):
        return "{"+str(self.n)+","+str(self.ntimes)+"}"


stones = []
for i in data:
    stones.append(Stone(i))

blinks = 75
for blink in range(blinks):
    newstones = []
    print("Blink ", blink)
    #print(" ".join([x.__str__() for x in stones]))
    print(len(stones))
    for i in range(len(stones)):
        for stone in stones[i].evolve():
            newstones.append(stone)
    stones = newstones

    if True:
        i = -1
        while i < len(stones)-1:
            i = i+1
            j = i
            while j < len(stones)-1:
                j = j+1
                if stones[i].n == stones[j].n:
                    stones[i].ntimes += stones[j].ntimes
                    del stones[j]
                    j = j-1

print("\n\n", len(stones))

res = 0
for i in stones:
    res += i.ntimes
print(res)
