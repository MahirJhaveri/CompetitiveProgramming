# Problem 1169 - Invalid Transactions

class Solution(object):
    def invalidTransactions(self, transactions):
        i = 0
        ans = []
        recents = {}
        while i < len(transactions):
            t = transactions[i].split(",")
            name = t[0]
            time = int(t[1])
            amount = int(t[2])
            city = t[3]
            if name not in recents:
                recents[name] = []
            recents[name].append([name, time, city, amount])
            i += 1
        i = 0
        for n in recents:
            for name, time, city, amount in recents[n]:
                if amount > 1000 or other_city_seen_recently(recents, name, city, time):
                    ans.append(",".join([name, str(time), str(amount), city]))
        return ans

def other_city_seen_recently(recents, name, city, time):
    i = len(recents[name])-1
    while i>= 0:
        if abs(time - recents[name][i][1]) <= 60 and recents[name][i][2] != city:
            return True
        i -= 1
    return False
