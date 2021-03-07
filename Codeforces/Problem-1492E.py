# Problem 1492E - Almost Fault-Tolerant Database
import itertools

# computes num diffs in arr1 and arr2
def diff(arr1, arr2):
    count = 0
    assert(len(arr1) == len(arr2))
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count += 1
    return count

# returns an arr with indices where vals are diff
def diff_pos(arr1, arr2):
    res = []
    assert(len(arr1) == len(arr2))
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            res.append(i)
    return res

def diff_without_counting_dpos(arr1, arr2, dpos):
    count = 0
    for i in range(len(arr1)):
        if i not in dpos and arr1[i] != arr2[i]:
            count += 1
    return count

def main():
    inp = input().rstrip().split(" ")
    n, m = int(inp[0]), int(inp[1])
    copies = []
    for _ in range(n):
        inp = input().rstrip().split(" ")
        copies.append([int(c) for c in inp])
    
    i=1
    while i < n and diff(copies[0], copies[i]) < 3:
        i += 1
        
    if i < n and diff(copies[0], copies[i]) > 4:
        print('No')
        return
    
    if i < n:
        dpos = diff_pos(copies[i], copies[0])
        if len(dpos) == 4:
            temp = [0,0,1,1]
            temp = list(itertools.permutations(temp))
            states = []
            for t in temp:
                state = []
                for c in range(4):
                    state.append(copies[0][dpos[c]] if t[c] == 0 else copies[i][dpos[c]])
                states.append(state)
            c = 1
            while c < n:
                new_states = []
                for state in states:
                    count_without_dpos = diff_without_counting_dpos(copies[0], copies[c], dpos)
                    if count_without_dpos < 3:
                        count = count_without_dpos
                        for p in range(4):
                            pos = dpos[p]
                            if copies[c][pos] != state[p]:
                                count += 1
                        if count < 3:
                            new_states.append(state)
                states = new_states
                if len(states) == 0:
                    break
                c += 1
            if len(states) == 0:
                print("No")
                return
            ans = [str(b) for b in copies[0]]
            for p in range(4):
                ans[dpos[p]] = str(states[0][p])
            print('Yes')
            print(" ".join(ans))
            return
        elif len(dpos) == 3:
            temp = [0,1,'x']
            temp = list(itertools.permutations(temp))
            states = []
            for t in temp:
                state = []
                for c in range(3):
                    if t[c] == 'x':
                        state.append('x')
                    else:
                        state.append(copies[0][dpos[c]] if t[c] == 0 else copies[i][dpos[c]])
                states.append(state)
            c = 1
            while c < n:
                new_states = []
                for state in states:
                    count_without_dpos = diff_without_counting_dpos(copies[0], copies[c], dpos)
                    if count_without_dpos < 3:
                        count = count_without_dpos
                        for p in range(3):
                            pos = dpos[p]
                            if copies[c][pos] != state[p]:
                                count += 1
                        if count < 3:
                            new_states.append(state)
                        if count == 3:
                            pos = dpos[p]
                            for p in range(3):
                                state[p] = copies[c][pos] if state[p] == 'x'else state[p]
                                count -= 1
                        if count < 3:
                            new_states.append(state)
                states = new_states
                if len(states) == 0:
                    break
                c += 1
            if len(states) == 0:
                print("No")
                return
            ans = [str(b) for b in copies[0]]
            for p in range(3):
                ans[dpos[p]] = str(states[0][p]) if states[0][p] != 'x' else '1'
            print('Yes')
            print(" ".join(ans))
            return
            
    else:
        print('Yes')
        ans = [str(i) for i in copies[0]]
        print(" ".join(ans))

main()
