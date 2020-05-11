fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
  strip = line.rstrip()
  print(strip.upper())