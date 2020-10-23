# Problem 1360 - Number of days between two dates

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False 
    return True

def compute_days(month, day, year):
    
    days_in_month = {
        1: 31, 2: 29 if is_leap(year) else 28,
        3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    curr = 1971
    days = 0
    while curr < year:
        days += 366 if is_leap(curr) else 365
        curr += 1
    
    curr = 1
    while curr < month:
        days += days_in_month[curr]
        curr += 1
    
    days += day-1
    
    return days 

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        date1 = date1.split("-")
        date2 = date2.split("-")
        return abs(compute_days(int(date1[1]), int(date1[2]), int(date1[0])) - compute_days(int(date2[1]), int(date2[2]), int(date2[0])))
        
