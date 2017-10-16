def if_condition(p, a, inside):
    s1 = "["
    r, p = jeticbf(inside, p)
    s3 = "=@a@b ~@a @a] =@b@a".replace('@a', a).replace('@b', '^')
    r2, p = jeticbf(s3, p)
    return s1 + r + r2, p

def assign(p, a, b):
    remove_b, p = zero(p, b)
    remove_c, p = zero(p, '_')
    s = "@a[@b+1 @c+1 @a-1 @a] @c[@a+1 @c-1 @c] @b".replace('@a', a).replace('@b', b).replace('@c', '_')
    r, p = jeticbf(s, p)
    return remove_b + remove_c + r, p

def zero(p, a):
    s = "@a[@a-1 @a]".replace('@a', a)
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
        if (c == '+' or c == '-'):
            number = ""
            i += 1
            while (S[i] >= '0' and S[i] <= '9'):
                number += S[i]
                i += 1
            n = int(number)
            R += c*n
            continue
        elif (c == '~'):
            r, p = zero(p, S[i+1])
            R += r
            i += 2
            continue
        elif (c == '='):
            r, p = assign(p, S[i+1], S[i+2])
            R += r
            i += 3
            continue
        elif (c == ' '):
            pass
        elif (c == '[' or c == ']' or c == '<' or c == '>'):
            R += c
        elif (c == '('):
            condition = S[i-1]
            pair = 1
            inside = ""
            while (pair > 0):
                i += 1
                inside += S[i]
                if (S[i] == '('):
                    pair += 1
                elif (S[i] == ')'):
                    pair -= 1
            inside = inside[:-1]
            r, p = if_condition(p, condition, inside)
            R += r
            i += 1
            continue
        elif (c >= 'A' and c <= 'z'):
            new_p = getP(c)
            move_p = new_p - p
            p = new_p
            if (move_p > 0):
                R += ">"*move_p
            elif (move_p < 0):
                R += "<"*-move_p
        else:
            R += c
        i += 1
    return R, p

def main():
    S = raw_input()
#    S = "s+32 i+99 j+10 i[a+1 j-1 ~A A-1 j[A+1 =jJ ~j j] =Jj A[~a b+1 j+9 ~A A] =bx x+48 x. =ax x+48 x. s. i-1 i]"
#    S = "s+32 i+99 j+10 i[a+1 j-1 ~A A-1 j(A+1) A(~a b+1 j+9) =bx x+48 x. =ax x+48 x. s. i-1 i]"
    print jeticbf(S)[0]
    
main()