commands = []

with open("input.txt") as f:
    for line in f:
        op, X = line.split()
        commands.append((op, int(X)))
        
x, y = 0, 0

for op, X in commands:
    if op == "forward":
        x += X
    elif op == "up":
        y -= X
    elif op == "down":
        y += X
    else:
        raise Exception(op)

print(x, y)

answer = (x * y)
print(answer)
with open("output1.txt", "w") as f:
    #f.write(str(answer))
    print(answer, file=f)