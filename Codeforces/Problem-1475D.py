# Problem 1475D - Cleaning The Phone

def solve():
    inp = input().rstrip().split(" ")
    n, m = int(inp[0]), int(inp[1])
    a_arr = input().rstrip().split(" ")
    b_arr = input().rstrip().split(" ")
    
    sum_reg = 0
    sum_imp = 0
    reg_apps = []
    imp_apps = []
    for i in range(n):
        if b_arr[i] == "1":
            reg_apps.append(int(a_arr[i]))
            sum_reg += int(a_arr[i])
        else:
            imp_apps.append(int(a_arr[i]))
            sum_imp += int(a_arr[i])
    
    reg_apps.sort()
    imp_apps.sort()
    
    if sum_reg + sum_imp < m:
        print(-1)
        return
    
    tot_removed = 0
    min_points_lost = 0
    
    while sum_reg < m - tot_removed:
        tot_removed += imp_apps.pop()
        min_points_lost += 2
    
    while tot_removed < m and len(reg_apps)+len(imp_apps) > 0:
        if len(reg_apps) == 0:
            tot_removed += imp_apps.pop()
            min_points_lost += 2
        elif len(imp_apps) == 0:
            tot_removed += reg_apps.pop()
            min_points_lost += 1
        else:
            if reg_apps[-1] >= imp_apps[-1]:
                tot_removed += reg_apps.pop()
                min_points_lost += 1
            else:
                if tot_removed + reg_apps[-1] >= m:
                    tot_removed += reg_apps.pop()
                    min_points_lost += 1
                elif len(reg_apps) > 1 and reg_apps[-1] + reg_apps[-2] > imp_apps[-1]:
                    tot_removed += reg_apps.pop()
                    tot_removed += reg_apps.pop()
                    min_points_lost += 2
                else:
                    tot_removed += imp_apps.pop()
                    min_points_lost += 2
    
    print(min_points_lost)

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
