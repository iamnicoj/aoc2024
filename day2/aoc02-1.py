
# load aoc01.txt file
from pathlib import Path

file_path = Path("day2/aoc02.txt")

total = 0
for line in file_path.read_text().splitlines():
    splited = line.split(' ')
    report = [int(i) for i in splited if i.isdigit()]

    isIncreasing = False
    isDecreasing = False
    for i in range( 1, len(report), 1):
        # increaseing path
        if report[i - 1] < report[i]:
            isIncreasing = True 
        elif report[i - 1] > report[i]: # decreasing path
            isDecreasing = True
        else:
            break # neither
        
        if isIncreasing + isDecreasing > 1:
            break
        if abs(report[i - 1] - report[i]) > 3:
            break
        if i + 1 == len(report):
            total += 1

print(total)