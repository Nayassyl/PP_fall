import datetime 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dmonths = [31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap_year(year):
    if year % 4 == 0: return True
def is_valid_date(year, month, day):
    if year < 0 or month < 0 or day < 0: return False
    if is_leap_year(year):
        if month == 2 and day in range(1,30): return True
        elif month in range(1, 13) and day in range(1, days[month + 1] + 1): return True
    elif month in range(1, 13) and day in range(1, days[month + 1] + 1): return True
    return False
def get_day_of_week(year, month, day):
    a = datetime.date(year, month, day)
    return(datetime.datetime.weekday(a))

class mydate():
    def __init__(self, year = 2023, month = 11, day = 1):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = get_day_of_week(year, month, day)
    def set_date(self, year, month, day):
        if is_valid_date(year, month, day):
            self.year = year
            self.month = month
            self.day = day
            self.weekday = get_day_of_week(year, month, day)
        else: print("Wrong date!")
    def set_year(self, year):
        if is_valid_date(year, self.month, self.day):
            self.year = year
        else: print("Wrong year!")
    def set_month(self, month):
        if is_valid_date(self.year, month, self.day):
            self.month = month
        else:print("Wrong month!")
    def set_day(self, day):
        if is_valid_date(self.year, self.month, day):
            self.day  = day
        else: print("Wrong day!")
    
    def get_year(self):
        print(self.year)
    def get_month(self):
        print(self.month)
    def get_day(self):
        print(self.day)

    def next_day(self):
        if is_leap_year(self.year) and self.month == 2 and self.day == 29:
            self.month += 1
            self.day = 1
        elif self.day == dmonths[self.month - 1]:
            if self.months == 12: 
                self.year += 1
                self.year = 1
                self.day = 1
            else: 
                self.months += 1
                self.day = 1
        else: self.day += 1
    def next_months(self):
        if self.month == 12:
            self.year += 1
            self.month = 1
        elif self.month == 1:
            if is_leap_year(self.year) and self.day > 29:
                self.month = 2
                self.day = 29
            elif not(is_leap_year(self.year)) and self.day > 28:
                self.month = 2
                self.day = 28
            else:
                self.month = 2
                
        else: self.month += 1
    
    def next_year(self):
        self.year += 1


    
    
    def __str__(self):
        return str(str(days[self.weekday]) + " " + str(self.day) + " " + months[self.month - 1] + " " +str( self.year))



a = mydate()
a.set_date(2012,2,14)
print(a)




