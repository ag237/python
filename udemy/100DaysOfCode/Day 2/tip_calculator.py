print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? $"))

tip = int(input("What tip percentage? "))

num_people = int(input("How many people are splitting the bill? "))

tip_percentage = ( tip / 100 ) + 1

total_with_tip = round((total_bill * tip_percentage), 2)

per_person = round(total_with_tip / num_people, 2) 

print(f"Final bill was ${total_bill}, with a {tip}% tip, total bill including tip was ${total_with_tip}, {num_people} splitting the bill with each person paying ${per_person}")
