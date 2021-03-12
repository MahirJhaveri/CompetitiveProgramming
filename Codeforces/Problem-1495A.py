# Problem 1495A - Diamond Miner

def distance(v1, v2):
    return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)**0.5

def main():
    t = int(input())
    for c in range(t):
        n = int(input())
        miners = []
        diamonds = []
        for _ in range(2*n):
            inp = input().rstrip().split(" ")
            if inp[0] == "0":
                miners.append((0, abs(int(inp[1]))))
            else:
                diamonds.append((abs(int(inp[0])), 0))
        miners.sort()
        diamonds.sort()
        
        res = 0.0
        while len(diamonds) > 0:
            res += distance(miners.pop(), diamonds.pop())
        print(res)
        
main()
