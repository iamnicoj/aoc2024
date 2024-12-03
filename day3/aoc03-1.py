import re

# Define the pattern to match
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Open the file in read mode
total = 0
with open('day3/aoc03.txt', 'r') as file:
    # Read the file line by line to handle large files
    for line in file:
        # Find all matches in the line
        matches = re.findall(pattern, line)
        for match in matches:
            num1, num2 = map(int, match)  # Convert strings to integers
            total += num1 * num2

print(total)