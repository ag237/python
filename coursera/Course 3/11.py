import re

filename = input("Enter file name: ")
filehandle = open(filename)
numbers = list()

for line in filehandle:
  line = line.rstrip()
  match = re.findall('[0-9]+', line)
  if not len(match) >= 1 : continue
  for m in match :
    fm = float(m)
    numbers.append(fm)
  
sums = sum(numbers)
print(sums)
