import numpy as np

with open('2024/day02/input.txt') as file:
    input = [list(map(int, line.split())) for line in file]


def is_increasing_and_safe(prev, remaining_report, skipps_left = 0):
    if skipps_left < 0:
        return False
    if len(remaining_report) <= skipps_left:
        return True
    
    level = remaining_report[0]
    return level - prev >= 1 and level - prev <= 3 and is_increasing_and_safe(level, remaining_report[1:], skipps_left) \
        or is_increasing_and_safe(prev, remaining_report[1:], skipps_left - 1)


def is_decreasing_and_safe(prev, remaining_report, skipps_left = 0):
    if skipps_left < 0:
        return False
    if len(remaining_report) <= skipps_left:
        return True
    
    level = remaining_report[0]
    return prev - level >= 1 and prev - level <= 3 and is_decreasing_and_safe(level, remaining_report[1:], skipps_left) \
        or is_decreasing_and_safe(prev, remaining_report[1:], skipps_left - 1)

sum = 0
for report in input:
    if is_increasing_and_safe(report[0], report[1:], 1) or is_decreasing_and_safe(report[0], report[1:], 1) \
        or is_increasing_and_safe(report[1], report[2:], 0) or is_decreasing_and_safe(report[1], report[2:], 0):
        sum += 1
        print(f'{report}: True')
    else:
        print(f'{report}: False')

print(sum)