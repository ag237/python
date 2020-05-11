fname = input("Enter file name: ")
fh = open(fname)
count = 0
spam = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
      count = count + 1
      pos = line.find(':')
      num = line[pos+1:]
      fnum = float(num)
      spam = spam + fnum

spamavg = spam / count
print("Average spam confidence:", spamavg)