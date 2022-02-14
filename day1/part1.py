
# Шаг 1: получить данные задачи

arr = []
with open("input.txt") as f:
    for line in f:
        arr.append(int(line))
        
print(arr)

answer = 0
for c_val, n_val in zip(arr[:-1], arr[1:]):
    if n_val > c_val:
        answer += 1
                        
print(answer)
    
with open("output1.txt", "w") as f:
    #f.write(str(answer))
    print(answer, file=f)