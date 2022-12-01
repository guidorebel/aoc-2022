
# Get the data
data = []
f = open("input.txt")
for line in f.readlines():
    data.append(line.strip())
f.close()

# Process the data
elfs = []
cals = 0

for i in data:
    if i == "":
        elfs.append(cals)
        cals = 0
    else:
        cals += int(i)

# Part 1
print (max(elfs))

# Part 2
elfs.sort()
print (sum(elfs[-3:]))