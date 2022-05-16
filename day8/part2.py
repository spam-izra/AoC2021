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
        codes = [
            set(c) for c in codes
        ]
        display = [
            set(c) for c in display
        ]
        inp.append((codes, display))

answer = 0
for codes, display in inp:
    #print(codes)
    decode = {
        k: None for k in range(10)
    }
    
    while codes:
        c = codes.pop(0)
        
        if len(c) == 2:
            decode[1] = c
        elif len(c) == 3:
            decode[7] = c
        elif len(c) == 4:
            decode[4] = c
        elif len(c) == 7:
            decode[8] = c
            
        elif decode[4] is not None and decode[4] < c:
            decode[9] = c
            
        elif decode[7] is not None and len(c) == 5 and decode[7] < c:
            decode[3] = c
        elif decode[7] is not None and decode[9] is not None and len(c) == 6 and decode[7] < c:
            decode[0] = c
            
        elif decode[0] is not None and decode[9] is not None and len(c) == 6:
            decode[6] = c
        elif decode[6] is not None and decode[3] is not None and len(c) == 5 and c < decode[6]:
            decode[5] = c
        elif decode[3] is not None and decode[5] is not None and len(c) == 5:
            decode[2] = c
        else:
            codes.append(c)
        
            
    #for i in range(10):
    #    print(f'{i:d} => {decode[i]}')
    
    
    num = 0
    for i, c in enumerate(reversed(display)):
        for d in decode:
            if decode[d] == c:
                num += d * 10**i
                break
        else:
            raise Exception()
            
        
    print(num)
    answer += num
    #break
            
print(answer)
with open('output2.txt', 'w') as f:
    print(answer, file=f)