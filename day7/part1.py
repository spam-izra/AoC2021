from collections import Counter

infile = "input.txt"

with open(infile) as f:
    pos = [*map(int, f.read().split(","))]
    
N, vMin, vMax = len(pos), min(pos), max(pos)

answer = 10**10

for p in range(vMin, vMax + 1):
    fuel = 0
    for sub in pos:
        fuel += abs(sub - p)
        
    answer = min(fuel, answer)
    
with open("output1.txt", "w") as f:
    print(anwer, file=f)
    