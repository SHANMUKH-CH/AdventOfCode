def _Q2(line):
    for xo in range(len(line)):
        x, i, crap_i_saw, broke = 0, 0, set(), False
        while i not in crap_i_saw:
            crap_i_saw.add(i)
            y, num = line[i]
            if xo == i:
                if y == 'jmp': y = 'nop'
                elif y == 'nop': y = 'jmp'
            if y == 'nop': i += 1; continue
            elif y == 'jmp': i += int(num)
            elif y == 'acc': i += 1; x += int(num)
            if i == len(line): broke = True; break
        if broke: break
    return (x)
if __name__=='__main__':
    with open('day8_input.txt') as x:
            line = [line.split() for line in  x.read().split("\n")]
            print(_Q2(line))