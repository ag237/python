filename = input("Enter file name: ")
if len(filename) < 1 : filename = "mbox-short.txt"
filehandle = open(filename)
counts = dict()

for line in filehandle:
  if not line.startswith('From:') : continue
  else:
    splitline = line.split()
    emailaddress = splitline[1]
    counts[emailaddress] = counts.get(emailaddress,0) + 1

biggestcount = None
biggestemail = None

for key,value in counts.items():
  if biggestcount is None or value > biggestcount:
    biggestemail = key
    biggestcount = value

print(biggestemail,biggestcount)
