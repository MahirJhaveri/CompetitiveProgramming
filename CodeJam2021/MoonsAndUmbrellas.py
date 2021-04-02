# CodeJam 2021 Qualification Round - Moons and Umbrellas

def main():
    T = int(input())
    for c in range(1, T+1):
        inp = input().rstrip().split(" ")
        X, Y = int(inp[0]), int(inp[1])
        s = inp[2]
        temp = s[0]
        for i in range(1, len(s)):
            if s[i] == '?' and s[i-1]=='?':
                pass
            else:
                temp += s[i]
        s = temp
        cost  = 0
        for i in range(1,len(s)-1):
            if s[i] == '?':
                if s[i-1] != s[i+1]:
                    cost += X if s[i-1] == 'C' else Y
            elif s[i] == 'C' and s[i-1] == 'J':
                cost += Y
            elif s[i] == 'J' and s[i-1] == 'C':
                cost += X
        if len(s) >= 2:
            if s[len(s)-1] == 'C' and s[len(s)-2] == 'J':
                cost += Y
            elif s[len(s)-1] == 'J' and s[len(s)-2] == 'C':
                cost += X
        print("Case #%d: %d" % (c, cost))
        
        

main()
