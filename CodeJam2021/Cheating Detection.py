# Qualification Round 2021 - Cheating Detection

# IDEA:
# compute and sort question based on difficulty
# compute the question difficulty for all questions
# compute the skill level for each of the players
# compare the sum of each player on the easy 500 and difficult 5000 questions
# compare with the expected sum based on skill and question difficulty
# return player with max abs difference

import math

e = 2.71828182845

def compute_sigmoid(eS, eQ):
    return eS*eQ/(1 + eS*eQ)

def main():
    T = int(input())
    P = int(input())
    for c in range(1, T+1):
        arr = []
        for i in range(100):
            inp = input().rstrip()
            arr.append(inp)
        
        S = [0 for i in range(100)]
        Q = [0 for i in range(10000)]
        for i in range(100):
            for j in range(10000):
                S[i] += int(arr[i][j])
                Q[j] += int(arr[i][j])
        

        Q = [[i, Q[i]] for i in range(len(Q))] # zip question index with difficulty (avg. performance)
        Q.sort(key=lambda tup: tup[1])
        
        # Compute the expected value of S for each of the students            
        c1 = math.pow(e, 3)
        c2 = math.pow(e, -3)
        for i in range(100):
            c3 = math.pow(e, (6*S[i])/10000.0)
            S[i] = (c3-1)/(c1-c3*c2)
        for i in range(10000):
            c3 = math.pow(e, (6*Q[i][1])/100.0)
            Q[i][1] = (c3-1)/(c1-c3*c2)
        
        ans = None
        max_val = -100000000
        for i in range(100):
            actual_diff = 0
            expected_diff = 0
            for j in range(500):
                actual_diff += int(arr[i][Q[j][0]])
                expected_diff += compute_sigmoid(S[i], Q[j][1])
            for j in range(99500, 10000):
                actual_diff += int(arr[i][Q[j][0]])
                expected_diff += compute_sigmoid(S[i], Q[j][1])

            if expected_diff == 0:
                ans = i+1
                break
            
            metric = abs(actual_diff-expected_diff)
            
            if metric > max_val:
                max_val = metric
                ans = i+1
        
        print("Case #%d: %d" % (c, ans))
        
main()
