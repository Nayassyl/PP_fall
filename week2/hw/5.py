print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
m = input("Input the name of Month: ")
 
if m == "February":
    print("No. of days: 28/29 days")
elif m in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif m in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("No such a month")
