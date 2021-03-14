# Problem 1495C - Garden of the Sun

def main():
    T = int(input())
    for c in range(T):
        inp = input().rstrip().split(" ")
        n, m = int(inp[0]), int(inp[1])
        mat = []
        for _ in range(n):
            mat.append(list(input().rstrip()))
        
        if n == 1 or n == 2:
            for j in range(m):
                mat[0][j] = 'X'
        else:
            i=0
            pending = False
            while i < n:
                if i == 0:
                    pass
                elif i % 3 == 1:
                    for j in range(m):
                        mat[i][j] = 'X'
                    pending = True
                elif i % 3 == 2:
                    for j in range(m):
                        if pending and mat[i][j] == 'X' and i+1 < n:
                            mat[i+1][j] = 'X'
                            pending = False
                else:
                    for j in range(m):
                        if pending and mat[i][j] == 'X':
                            mat[i-1][j] = 'X'
                            pending = False
                    if pending:
                        mat[i-1][0] = 'X'
                        mat[i][0] = 'X'
                        pending = False
                i += 1  
            
            if n % 3 == 1:
                for j in range(m):
                    if mat[-1][j] == 'X':
                        mat[-2][j] = 'X'
        for row in mat:
            print("".join(row))

main()
