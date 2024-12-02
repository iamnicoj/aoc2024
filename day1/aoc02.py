import collections

# load aoc01.txt file
from pathlib import Path

file_path = Path("day1/aoc01.txt")

list1 = []
list2 = []
for line in file_path.read_text().splitlines():
    splited = line.split(' ')
    list1.append(int(splited[0]))
    list2.append(int(splited[3]))

list2Counter = collections.Counter(list2)

total = 0
for num in list1:
    if num in list2Counter:
        total += num * list2Counter[num]

print(total)

