
# load aoc01.txt file
from pathlib import Path

file_path = Path("day1/aoc01.txt")

list1 = []
list2 = []
for line in file_path.read_text().splitlines():
    splited = line.split(' ')
    list1.append(int(splited[0]))
    list2.append(int(splited[3]))

list1.sort()
list2.sort()

if len(list1) != len(list2):
    print("Error: list1 and list2 have different lengths")
    exit()

total = 0
for i in range(len(list1)):
    total += abs(list2[i] - list1[i])

print(total)