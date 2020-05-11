fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  lsplit = line.split()
  for i in lsplit:
    if i in lst : continue
    else:
      lst.append(i)
lst.sort()
print(lst)