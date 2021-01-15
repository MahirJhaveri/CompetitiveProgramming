# Problem 1466C - Canine Poetry

# Observation:
# If there exists a palindrome of len 4 or more, 
# then there MUST exist a palindrome of len 2 or 3

def main():
    T = int(input())
    for c in range(T):
        s = input().rstrip()
        modified = [0 for i in range(len(s))]
        count = 0
        
        for i in range(len(s)):
            if i > 0:
                if i == 1:
                    if s[1] == s[0]:
                        modified[1] = 1
                        count += 1
                else:
                    if s[i] == s[i-1] and modified[i-1]!=1:
                        modified[i]=1
                        count+=1
                    elif s[i] == s[i-2] and modified[i-2]!=1:
                        modified[i]=1
                        count+=1
        print(count)

main()
