hrs = float(input("Enter Hours: "))
rate = float(input("Enter payrate: "))

if hrs <= 40:
  gross = hrs * rate
else:
  forty = 40 * rate
  fortyplus = hrs - 40
  ot = rate * 1.5
  otp = fortyplus * ot
  gross = otp + forty

print (gross)