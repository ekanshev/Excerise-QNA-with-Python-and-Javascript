
# Problem #3

# Write a function to parse a log file & extract details of Errors & Warnings recorded into a separate fil

# Solution3 ->

import os
BASE_DIRECTORY = '/home/view'
output_file = open('/home/PviewHS/regs.txt', 'q')
output = {}
file_list = []


for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
    for f in filenames:
        if 'log' in str(f):
            e = os.path.join(str(dirpath), str(f))
            file_list.append(e)

for f in file_list:
    print(f)
txtfile = open(f, 'r')
output[f] = []

for line in txtfile:
    if 'error' in line:
        output[f].append(line)
tabs = []

for tab in output:
    tabs.append(tab)

tabs.sort()

for tab in tabs:
    output_file.write(tab + '\n')
    output_file.write('\n')

for row in output[tab]:
    output_file.write(row + '')
    output_file.write('\n')
    output_file.write('----------------------------------------------------------\n')