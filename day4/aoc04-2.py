class Solution():
    def main(self):
        matrix = []
        with open('day4/aoc04.txt', 'r') as file:
            for line in file:
                line = line.strip()  
                matrix.append(list(line))  

        counter = 0

        for i in range(1, len(matrix) - 1):
            for j in range(1, len(matrix[i]) - 1):
                if matrix[i][j] == 'A':
                    if(
                        ((matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' ) or (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M')) and 
                        ((matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S' ) or (matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M'))
                    ):
                        counter += 1

        print(counter)

if __name__ == "__main__":
    Solution().main()