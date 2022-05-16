# Здесь все сложнее. Мы последовательно считываем данные
# из файла и сравниваем элементы из окон.

queue = []
answer = 0

with open("input.txt") as f:
    for _ in range(3):
        line = f.readline()
        queue.append(int(line))
    
    for line in f:
        first = queue.pop(0)
        queue.append(int(line))
        last = queue[-1]
        
        if last > first:
            answer += 1
            
            
#  вывод
print(answer) 
with open("output2.txt", "w") as f:
    #f.write(str(answer))
    print(answer, file=f)