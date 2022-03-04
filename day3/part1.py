from collections import Counter

arr = []

with open("input.txt") as f:
    for line in f:
        arr.append(line.strip())
        
gamma, eps = "", ""

N = len(arr[0])

for p in range(N):
    bits = [v[p] for v in arr]
    c = Counter(bits)
    
    if c["1"] > c["0"]:
        gamma += "1"
    else:
        gamma += "0"


epsilon = "".join(["0" if c == "1" else "1" for c in gamma])

print(gamma)
print(epsilon)

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print(gamma, epsilon, gamma*epsilon)

with open("output1.txt", "w") as f:
    print(gamma * epsilon, file=f)