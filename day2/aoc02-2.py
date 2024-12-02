from pathlib import Path

class solution:

    def problem(self):

        file_path = Path("day2/aoc02.txt")
        total = 0

        def rules_runner(report):
            nonlocal total
            isIncreasing = False
            isDecreasing = False
            for i in range( 1, len(report), 1):
                # increaseing path
                if report[i - 1] < report[i]:
                    isIncreasing = True 
                elif report[i - 1] > report[i]: # decreasing path
                    isDecreasing = True
                else:
                    return False
                
                if isIncreasing + isDecreasing > 1:
                    return False

                if abs(report[i - 1] - report[i]) > 3:
                    return False 

                if i + 1 == len(report):
                    total += 1
                    return True

        for line in file_path.read_text().splitlines():
            splited = line.split(' ')
            report = [int(i) for i in splited if i.isdigit()]

            if not rules_runner(report):
                for i in range(len(report)):
                    if rules_runner(report[0:i]+report[i+1:]):
                        break

        print(total)

if __name__ == "__main__":
    solution().problem()