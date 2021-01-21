# Problem 1469A - Regular Bracket Sequence

def solve():
    s = input().rstrip()
    
    if len(s) % 2 == 1:
        print("NO")
        return
    
    i = 0
    count = 0
    pos = True
    arr = []
    for i in range(len(s)):
        if s[i] in ['(', ')']:
            arr.append(count)
            arr.append(s[i])
            count = 0
        else:
            count+=1
    arr.append(count)
    if arr[1] == '(':
        print("YES")
        return
    else:
        if arr[0] == 0 or arr[4] == 0:
            print("NO")
            return
        if arr[0] % 2 == 1: 
            print("YES")
            return
        elif arr[2] > 0:
            print("YES")
            return
        elif arr[4] > 1:
            print("YES")
            return
        print("NO")
        return
    

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
