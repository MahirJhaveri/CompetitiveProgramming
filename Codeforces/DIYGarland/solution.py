# 1283F - DIY Garland

if __name__ == "__main__":
    n = int(input())
    inp = input().rstrip().split(" ")

    assert len(inp) == n-1

    for a in range(len(inp)):
        inp[a] = int(inp[a])

    marked = {}
    edges = [[inp[i], None] for i in range(n-1)]
    next_largest_unseen = n

    # mark the root node:
    root = inp[0]
    marked[inp[0]] = True

    for i in range(1, n-1):
        parent = edges[i][0]
        if parent not in marked:
            edges[i-1][1] = parent
            marked[parent] = True
        else:
            while (next_largest_unseen in marked):
                next_largest_unseen -= 1
            edges[i-1][1] = next_largest_unseen
            marked[next_largest_unseen] = True

    while next_largest_unseen in marked:
        next_largest_unseen -= 1
    marked[next_largest_unseen] = True
    edges[n-2][1] = next_largest_unseen

    print(root)
    for edge in edges:
        edge = [str(edge[0]), str(edge[1])]
        print(" ".join(edge))
