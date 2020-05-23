#!usr/bin/env python3
import re
filename='regex_sum_531147.txt'
with open(filename,'r') as file:
    txt=file.read()
    result=re.findall(r'[\d]+',txt)

out=[int(num) for num in result]
print(sum(out))


