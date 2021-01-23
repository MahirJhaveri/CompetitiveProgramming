# Problem 1469D - Ceil Divisions

def solve():
    n = int(input())
    num = n-1
    den = n
    ans = ""
    count = 0
    while den > 2:
        while not (den/num <= num and den/(num-1) > (num-1)):
            ans += "\n" + str(num) + " " + str(den)
            count += 1
            num -= 1
        ans += "\n" + str(den) + " " + str(num) 
        ans += "\n" + str(den) + " " + str(num)
        count += 2
        den = num
        num -= 1
    ans = str(count) + ans
    print(ans)
    
    
def main():
    T = int(input())
    for c in range(T):
        solve()

main()
