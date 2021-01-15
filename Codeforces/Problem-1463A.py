# Problem 1463A - Dungeon

def main():
    T = int(input())
    for c in range(T):
        h = input().rstrip().split(" ")
        s = int(h[0])+int(h[1])+int(h[2])
        m = min(int(h[0]), int(h[1]), int(h[2]))
        if s % 9 == 0 and m >= (s/9):
            print("YES")
        else:
            print("NO")
main()
