class Card:
    def __init__(self, arr):
        self._arr = arr
        self._crossed = [[False for _ in range(5)] for _ in range(5)]
        
    def cross(self, n):
        for x in range(5):
            for y in range(5):
                if self._arr[y][x] == n:
                    self._crossed[y][x] = True
                    
    def score(self):
        r = 0
        for x in range(5):
            for y in range(5):
                if not self._crossed[y][x]:
                    r += self._arr[y][x]
        return r
                    
    def is_winner(self):
        for n1 in range(5):
            s1, s2 = 0, 0
            for n2 in range(5):
                s1 += self._crossed[n1][n2]
                s2 += self._crossed[n2][n1]
            if s1 == 5 or s2 == 5:
                return True
        return False
        
    def __repr__(self):
        r = "\n|" + "--" * 5 + "-"*4
        r += "|\n|"
        for y, row in enumerate(self._arr):
            r += " ".join([
                "%2d" % v if not self._crossed[y][x] else " *" for x, v in enumerate(row)
            ])
            r += "|\n|"
        r += "--" * 5 + "-"*4 + "|\n"
        return r

infile = "test.txt"

with open(infile) as f:
    numbers = [*map(int, f.readline().strip().split(","))]
    #print(numbers)
    
    buffer = []
    cards = []
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        buffer.append([*map(int, line.split())])
        if len(buffer) == 5:
            cards.append(Card(buffer))
            buffer = []
            
            
winner = None
for n in numbers:
    #print("===> %d <===" % n)
    for c in cards:
        c.cross(n)
        if c.is_winner():
            winner = n, c
            break
            
    #print(cards)
    if winner is not None:
        break
        
print(winner)
answer = winner[0] * winner[1].score()  
with open("output1.txt", "w") as f:
    print(answer, file=f)
    