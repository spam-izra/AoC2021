from collections import Counter

infile = "input.txt"

with open(infile) as f:
    pos = [*map(int, f.read().split(","))]

    
N, vMin, vMax = len(pos), min(pos), max(pos)
print(N, vMin, vMax)

answer = 10**10

for p in range(vMin, vMax + 1):
    fuel = 0
    for sub in pos:
        n = abs(sub - p)
        fuel += (n*(n+1))//2
    answer = min(fuel, answer)
    
print(answer)
with open("output2.txt", "w") as f:
    print(answer, file=f)
    