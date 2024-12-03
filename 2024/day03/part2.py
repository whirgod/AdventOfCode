import re

with open('2024/day03/input.txt') as file:
    input = [line for line in file]

pattern = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

total = 0
enabled = True
for line in input:
    # enabled = True
    
    match = re.search(pattern, line)
    while match:
        print(match.group(0))

        if match.group(0) == "do()":
            enabled = True 
        elif match.group(0) == "don't()":
            enabled = False 
        elif enabled:
            total += int(match.group(1)) * int(match.group(2))  
        
        line = line[match.span(0)[1]:]
        match = re.search(pattern, line)

print(total)    