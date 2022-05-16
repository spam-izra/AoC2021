infile = "input.txt"

xmin = 10**10
xmax = -10**10
ymin = 10**10
ymax = -10**10

lines = []

with open(infile) as f:
    for line in f:
        x1y1, x2y2 = line.strip().split(" -> ")
        x1, y1 = map(int, x1y1.split(","))
        x2, y2 = map(int, x2y2.split(","))
        
        xmin = min(x1, x2, xmin)
        xmax = max(x1, x2, xmax)
        ymin = min(x1, x2, ymin)
        ymax = max(x1, x2, ymax)
        
        lines.append(((x1, y1), (x2, y2)))
        
        
print(xmin, xmax)
print(ymin, ymax)

W, H = xmax - xmin + 1, ymax - ymin + 1
print(W, H)

grid = [
    [0 for _ in range(W)]
    for _ in range(H)
]

for (x1, y1), (x2, y2) in lines:
    if x1 != x2 and y1 != y2:
        continue
        
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[y-ymin][x-xmin] += 1
            
answer = 0

for row in grid:
    for cell in row:
        if cell > 1:
            answer += 1
            
print(answer)
with open("output1.txt", "w") as f:
    print(answer, file=f)
