import re

with open('2024/day03/input.txt') as file:
    input = [line for line in file]

total = 0
for line in input:
    matches = re.findall(r'mul\((\d+),(\d+)\)', line)
    values = [int(match[0]) * int(match[1]) for match in matches]
    value = sum(values)
    total += value
    print(f'{line}\t{value} ({values})')

print(total)    