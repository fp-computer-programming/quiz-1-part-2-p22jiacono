#Author: JTI 10/19/21

q = input("Enter the day of the month: ")
m = input("Enter the number of the mouth: ")
year = input("Enter the year: ")
j = (int(year) // 100)
k = (int(year) % 100)

if int(m) == 1:
    m = 13 
    year = int(year) - 1
if int(m) == 2:
    m = 14
    year = int(year) - 1


h = ((int(q) + ((26) * (int(m) + 1) // (10)) + int(k) + (int(k) // 4) + (int(j) // 4) + (5 * int(j))) % 7)

if int(h) == 0:
    print("Saturday")
elif int(h) == 1:
    print("Sunday")
elif int(h) == 2:
    print("Monday")
elif int(h) == 3:
    print("Tuesday")
elif int(h) == 4:
    print("Wednesday")
elif int(h) == 5:
    print("Thursday")
else:
    print("Friday")
