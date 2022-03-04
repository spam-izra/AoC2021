commands = []

with open("input.txt") as f:
    for line in f:
        op, X = line.split()
        commands.append((op, int(X)))
        
x, y, aim = 0, 0, 0

for op, X in commands:
    if op == "forward":
        x += X
        y += aim * X
    elif op == "up":
        aim -= X
    elif op == "down":
        aim += X
    else:
        raise Exception(op)

print(x, y)
answer = (x * y)
print(answer)
with open("output1.txt", "w") as f:
    #f.write(str(answer))
    print(answer, file=f)