import urllib.request

u = urllib.request.urlopen(
    "https://gist.githubusercontent.com/tacksoo/3944382fa397fd42095890ef94e88365/raw"
    "/285ea8af3c2555d4883e86f1b557aae307772d5c/gme.csv")
data = u.read().decode('utf-8')
lines = data.split("\n")

print(lines[0])
# Using the Counter Library
# where the key is the "one,two, three (numbers)" and the value is the count

from collections import Counter

counter2 = Counter()
for line in lines[1:]:
    cols = line.split(",")
    first_char = cols[1][0]
    counter2[first_char] += 1

for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    print(num, counter2[num])

first_digits = []
for line in lines[1:]:
    cols = line.split(",")
    first_digits.append(cols[1][0])  # open price leading digit
    first_digits.append(cols[2][0])  # close price leading digit
    first_digits.append(cols[3][0])
    first_digits.append(cols[4][0])
    first_digits.append(cols[6][0])

total_counter = Counter(first_digits)
print(total_counter)

for num in range(1, 10):
    print(num, total_counter[str(num)])

# The code shows that the pattern did not necessarily follow Benford's distribution as expected