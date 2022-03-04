from collections import Counter

arr = []

with open("input.txt") as f:
    for line in f:
        arr.append(line.strip())

energy, CO2 = arr[:], arr[:]

N = len(arr[0])

for p in range(N):
    if len(energy) <= 1:
        break
        
    bits = [v[p] for v in energy]
    c = Counter(bits)
    b = "1" if c["1"] >= c["0"] else "0"
    print(b)
    energy = list(filter(lambda x: x[p] == b, energy))
    print(energy)
    
    
for p in range(N):
    if len(CO2) <= 1:
        break
        
    bits = [v[p] for v in CO2]
    c = Counter(bits)
    b = "1" if c["1"] < c["0"] else "0"
    print(b)
    CO2 = list(filter(lambda x: x[p] == b, CO2))
    print(CO2)
    
    
energy = int(energy[0], base=2)
CO2 = int(CO2[0], base=2)

print(energy * CO2)
with open("output2.txt", "w") as f:
    print(energy * CO2, file=f)