
import re

with open("input.txt") as f:
    lines = f.readlines()

text=""
for line in lines:
    text+=line

matches = re.findall(r'mul\((\d{1,3},\d{1,3})\)',text)
pairs = [elem.split(',') for elem in matches]
value = sum([int(val[0]) * int(val[1]) for val in pairs])

print(value)


with open("input.txt") as f:
    lines = f.readlines()
text=""
for line in lines:
    text+=line

matches = re.findall(r'(don\'t|do|mul\([0-9]{1,3},[0-9]{1,3}\))',text)

clean=[]
for match in matches:
    if match == 'do':
        clean.append("START")
    elif match == "don't":
        clean.append("STOP")
    else:
        values = re.findall(r'[0-9]{1,3}', match)
        if len(values)==2:
            assert values[0].isalnum()
            assert values[1].isalnum()
            val = int(values[0])*int(values[1])
            clean.append(val)
        else:
            print(f"PROBLEM: {match}")

print(clean)
max_ind = len(clean)
s=0
i=0
enabled=True

while i<max_ind:
    elem=clean[i]
    if enabled and type(elem) is int:
        s+=elem
    elif elem=="START":
        enabled=True
    elif elem=="STOP":
        enabled=False
    else:
        print(f"-",end='')
    i+=1

print(s)

