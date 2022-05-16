with open("input.txt") as f:
    fishes = [*map(int, f.read().split(","))]
    
print(f'{fishes=}')


for day in range(80):
    for i in range(len(fishes)):
        fishes[i] -= 1
        if fishes[i] < 0:
            fishes[i] = 6
            fishes.append(8)
            
answer = len(fishes)
print(answer)
with open("output1.txt", "w") as f:
    print(answer, file=f)