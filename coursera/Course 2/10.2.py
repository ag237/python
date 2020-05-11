filename = input("Enter file name: ")
if len(filename) < 1 : filename = "mbox-short.txt"
filehandle = open(filename)
counts = dict()

for line in filehandle:
  if not line.startswith('From ') : continue
  else:
    splitline = line.split()
    timestamp = splitline[5]
    splittimestamp = timestamp.split(':')
    hour = splittimestamp[0]
    counts[hour] = counts.get(hour,0) + 1

rsorted = sorted( [ (k,v) for k,v in counts.items() ] )
for k,v in rsorted:
  print(k,v)