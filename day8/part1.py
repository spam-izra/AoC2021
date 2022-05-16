def Display(codes):
    r = ["| " for _ in range(7)]
    
    for c in codes:
        if "a" in c:
            r[0] += " aaa  | "
        else:
            r[0] += "      | "
    for c in codes:
        if "b" in c and "c" in c:
            r[1] += "b   c | "
        elif "b" in c and "c" not in c:
            r[1] += "b     | "
        elif "b" not in c and "c" in c:
            r[1] += "    c | "
        else:
            r[1] += "      | "
    for c in codes:
        if "d" in c:
            r[3] += " ddd  | "
        else:
            r[3] += "      | "
    for c in codes:
        if "e" in c and "f" in c:
            r[4] += "e   f | "
        elif "e" in c and "f" not in c:
            r[4] += "e     | "
        elif "e" not in c and "f" in c:
            r[4] += "    f | "
        else:
            r[4] += "      | "
    for c in codes:
        if "g" in c:
            r[6] += " ggg  | "
        else:
            r[6] += "      | "
            
    r[2] = r[1]
    r[5] = r[4]
    r.insert(0, " -------"*len(codes))
    r.append(" -------"*len(codes))
    print("\n".join(r))
            

        
import re

infile = "test.txt"
infile = "input.txt"
rx = re.compile(r'[abcdefg]+')

inp = []
with open(infile) as f:
    for line in f:
        line = line.strip()
        values = rx.findall(line)
        assert len(values) == 14

        codes, display = values[:-4], values[-4:]
        inp.append((codes, display))
        
answer = 0
for _, display in inp:
    for digit in display:
        if len(digit) in [2, 3, 4, 7]:
            answer += 1
            
print(answer)
with open('output1.txt', 'w') as f:
    print(answer, file=f)