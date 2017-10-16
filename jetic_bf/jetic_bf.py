def assign(p, a, b):
    remove_b = zero(p, b)
    p = getP(b)
    s = "a[b+1 c+1 a-1 a] c[a+1 c-1 c] b".replace('a', a).replace('b', b).replace('c', '_')
    return remove_b + jeticbf(s, p)

def zero(p, a):
    s = "a[a-1 a]".replace('a', a)
    return jeticbf(s, p)

def getP(a):
    return ord(a) - 96

def jeticbf(S, p = 0):
    S += " "
    R = ""
    i = 0
    while (i < len(S)):
        c = S[i]
        # current
        if (c >= '_' and c <= 'z'):
            new_p = getP(c)
            move_p = new_p - p
            p = new_p
            if (move_p > 0):
                R += ">"*move_p
            elif (move_p < 0):
                R += "<"*-move_p
        elif (c == '+' or c == '-'):
            number = ""
            i += 1
            while (S[i] >= '0' and S[i] <= '9'):
                number += S[i]
                i += 1
            n = int(number)
            R += c*n
            continue
        elif (c == '~'):
            R += zero(p, S[i+1])
            p = getP(S[i+1])
            i += 2
            continue
        elif (c == '='):
            R += assign(p, S[i+1], S[i+2])
            p = getP(S[i+2])
            i += 3
            continue
        elif (c == ' '):
            pass
        else:
            R += c
        i += 1
    return R

def main():
    S = raw_input()
#    S = "s+32 i+9 i[a+1 =ab b+48 b. s. i-1 i]"
#    S = "a+49 =ab b."
    print jeticbf(S)        
    
main()