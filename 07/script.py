try:
    with open("07/input.txt", "r") as file:
        data = file.read()
except Exception:
    with open("input.txt", "r") as file:
        data = file.read()

data = data.split("\n")

operators = ["+","*","|"]


correct = []
correct_sum = 0

from itertools import product

for line in data:
    total = int(line.split(":")[0])
    numbers = [int(x) for x in line.split(": ")[1].split(" ")]
    all_combinations = list(product(operators,repeat=len(numbers)-1))
    
    for comb in all_combinations:
        result = numbers[0]
        for i in range(1,len(numbers)):
            if comb[i-1]=="+":
                result = result + numbers[i]
            elif comb[i-1]=="*":
                result = result *numbers[i]
            elif comb[i-1]=="|":
                result = int(str(result)+str(numbers[i]))
        if result == total:
            correct.append(line)
            correct_sum = correct_sum + total
            break
print(correct)
print(len(correct))
print("\n\n", correct_sum)