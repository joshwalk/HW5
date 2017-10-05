import re

file = open("regex_sum_32867.txt")

int_list = []
for line in file:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    for nos in y:
        int_list.append(int(nos))

print (sum(int_list))
