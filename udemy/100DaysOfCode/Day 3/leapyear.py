year = int(input("Which year do you want to check? "))

leap = 0
if year%4 == 0:
    leap = 1
    if year%100 == 0:
        leap = 0
        if year%400 == 0:
            leap = 1

if leap == 1:
    print("Leap year")
else:
    print("Not leap year")


