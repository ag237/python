# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)

days = 90 * 365
weeks = 90 * 52
months = 90 * 12

ageDays = int_age * 365
ageWeeks = int_age * 52
ageMonths = int_age * 12

print(f"You have {days - ageDays} days, {weeks - ageWeeks} weeks, and {months - ageMonths} months left.")