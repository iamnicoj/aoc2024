import re

do_flag = True
buffer = []
total = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
# Open the file in read mode
with open('day3/aoc03.txt', 'r') as file:
    # Read the file line by line to handle large files
    for line in file:
        for i, c in enumerate(line):
            if c == 'd':
                if do_flag and line[i:i+7] == "don't()":
                    do_flag = False
                elif not do_flag and line[i:i+4] == "do()":
                    do_flag = True
            if do_flag:
                buffer.append(c)

        # Find all matches in buffer line
        matches = re.findall(pattern, ''.join(buffer))
        for match in matches:
            num1, num2 = map(int, match)  # Convert strings to integers
            total += num1 * num2

        buffer = []

print(total)