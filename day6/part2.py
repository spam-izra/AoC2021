fishes = [0 for _ in range(8+1)]

with open("input.txt") as f:
    tmp = [*map(int, f.read().split(","))]
    for fish in tmp:
        fishes[fish] += 1
        
print(f'{fishes=}')

for day in range(256):
    new = fishes.pop(0)
    fishes[6] += new
    fishes.append(new)
    
answer = sum(fishes)
print(answer)