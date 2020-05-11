try:
  score = float(input("Enter score: "))
except:
  print("Please use integers")
  quit()

if score > 1.0:
  print("Score must be between 0.0 and 1.0")
  quit()
if score >= 0.9:
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
elif score < 0.6:
  print("F")