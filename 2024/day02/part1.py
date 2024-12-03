import numpy as np

with open('2024/day02/input.txt') as file:
    input = [list(map(int, line.split())) for line in file]

def is_increasing_and_safe(report):
    prev = report[0]
    for x in report[1:]:
        if x <= prev or x - prev > 3:
            return False
        prev = x
        
    return True

def is_decreasing_and_safe(report):
    prev = report[0]
    for x in report[1:]:
        if x >= prev or prev - x > 3:
            return False
        prev = x
        
    return True

sum = 0
for report in input:
    if is_increasing_and_safe(report) or is_decreasing_and_safe(report):
        sum += 1
        print(f'{report}: True')
    else:
        print(f'{report}: False')

print(sum)