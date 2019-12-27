# 1282C - Petya and Exam

if __name__ == '__main__':
    num_tests = int(input())
    for test in range(num_tests):
        inp = input().rstrip().split(" ")
        n = int(inp[0])
        T = int(inp[1])
        a = int(inp[2])
        b = int(inp[3])
        inp = input().rstrip().split(" ")
        difficulty = [int(inp[i]) for i in range(len(inp))]
        inp = input().rstrip().split(" ")
        mandatory_at = [int(inp[i]) for i in range(len(inp))]

        joint = list(zip(mandatory_at, difficulty))
        joint.sort(key=lambda tup: tup[1])
        joint.sort(key=lambda tup: tup[0])

        num_hard = sum(difficulty)
        num_easy = n - num_hard
        scores = []
        mandatory_score = 0
        mandatory_time = 0
        for time, difficulty in joint:
            left_time = time-1 - mandatory_time
            if left_time >= 0:
                score = mandatory_score
                if int(left_time/a) <= num_easy:
                    score += int(left_time/a)
                else:
                    score += num_easy
                    left_time -= num_easy*a
                    score += min(int(left_time/b), num_hard)
                scores.append(score)
            else:
                scores.append(0)
            mandatory_time += difficulty*(b-a) + a
            mandatory_score += 1
            num_easy = num_easy - (1 - difficulty)
            num_hard = num_hard - (difficulty)
        # Border case
        left_time = T - mandatory_time
        if left_time >= 0:
            score = mandatory_score
            if int(left_time/a) <= num_easy:
                score += int(left_time/a)
            else:
                score += num_easy
                left_time -= num_easy*a
                score += min(int(left_time/b), num_hard)
            scores.append(score)
        else:
            scores.append(0)

        print(max(scores))
