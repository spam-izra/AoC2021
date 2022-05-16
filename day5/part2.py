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
    if x1 == x2:
        dx, dy = 0, 1 if y2 >= y1 else -1
        length = abs(y2 - y1) + 1
    elif y1 == y2:
        dx, dy = 1 if x2 >= x1 else -1, 0
        length = abs(x2 - x1) + 1
    elif abs(x2 - x1) == abs(y2 - y1):
        dx = 1 if x2 >= x1 else -1
        dy = 1 if y2 >= y1 else -1
        length = abs(x2 - x1) + 1
    else:
        continue
    
    x, y = x1, y1
    for _ in range(length):
        grid[y-ymin][x-xmin] += 1
        x += dx
        y += dy
            
answer = 0

for row in grid:
    for cell in row:
        if cell > 1:
            answer += 1
            
print(answer)
with open("output2.txt", "w") as f:
    print(answer, file=f)