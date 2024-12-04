class Solution():
    def main(self):
        matrix = []
        with open('day4/aoc04.txt', 'r') as file:
            for line in file:
                line = line.strip()  
                matrix.append(list(line))  

        nearby = [[1, 1], [1, 0], [1, -1], [0,-1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
        lookfor = ['M', 'A', 'S']
        counter = 0

        def getNeighbors(i, j):
            for direction, (d_i, d_j) in enumerate(nearby):
                yield i + d_i, j + d_j, direction

        def dfs(i, j, index, dir):
            nonlocal counter
            if index == len(lookfor):
                counter += 1
                return

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if matrix[i][j] == lookfor[index]:
                    dfs(i + nearby[dir][0], j + nearby[dir][1], index + 1, dir)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'X':
                    for ni, nj, dir in getNeighbors(i, j):
                        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                            dfs(ni, nj, 0, dir)

        print(counter)

if __name__ == "__main__":
    Solution().main()