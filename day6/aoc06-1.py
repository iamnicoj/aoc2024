from collections import defaultdict

class Solution():

    def main(self):
        total = 0
        cursor = None
        direccion = ''
        seen = set()
        n = 0
        m = 0
        obstaclesRows = defaultdict(list)
        obstaclesCols = defaultdict(list)

        def moveUp():
            nonlocal total, cursor, direccion, seen, obstaclesCols
            goto = -1
            for row in obstaclesCols[cursor[1]]:
                if row < cursor[0]:
                    goto = max(row, goto)
            for i in range(goto + 1, cursor[0] + 1):
                if (i, cursor[1]) not in seen:
                    total += 1
                    seen.add((i, cursor[1]))
            if goto == -1:
                return True
            direccion = '>'
            cursor[0] = goto + 1
            return False

        def moveDown():
            nonlocal total, cursor, direccion, seen, n, obstaclesCols
            goto = n
            for row in obstaclesCols[cursor[1]]:
                if row > cursor[0]:
                    goto = min(row, goto)
            for i in range(cursor[0], goto):
                if (i, cursor[1]) not in seen:
                    total += 1
                    seen.add((i, cursor[1]))
            if goto == n:
                return True
            direccion = '<'
            cursor[0] = goto - 1
            return False
        
        def moveLeft():
            nonlocal total, cursor, direccion, seen, obstaclesRows
            goto = -1
            for col in obstaclesRows[cursor[0]]:
                if col < cursor[1]:
                    goto = max(col, goto)
            for j in range(goto + 1, cursor[1] + 1):
                if (cursor[0], j) not in seen:
                    total += 1
                    seen.add((cursor[0], j))
            if goto == -1:
                return True
            direccion = '^'
            cursor[1] = goto + 1
            return False

        def moveRight():
            nonlocal total, cursor, direccion, seen, m, obstaclesRows
            goto = m
            for col in obstaclesRows[cursor[0]]:
                if col > cursor[1]:
                    goto = min(col, goto)
            for j in range(cursor[1], goto):
                if (cursor[0], j) not in seen:
                    total += 1
                    seen.add((cursor[0], j))
            if goto == m:
                return True
            direccion = 'v'
            cursor[1] = goto - 1
            return False
        

        # Read the input file and populate data structures
        with open('day6/aoc06s.txt', 'r') as file:
            lines = file.readlines()
            n = len(lines)
            if n > 0:
                m = len(lines[0].rstrip('\n'))

            # Process each line
            for i, line in enumerate(lines):
                line = line.rstrip('\n')
                for j, c in enumerate(line):
                    if c in '^v<>':
                        cursor = [i, j]  # zero-based indexing
                        direccion = c.lower()
                    elif c == '#':
                        obstaclesRows[i].append(j)
                        obstaclesCols[j].append(i)

        # Initialize visited with the guard's starting position
        if cursor is not None:
            seen.add((cursor[0], cursor[1]))
            total = 1

        # Run the movement simulation until the guard leaves the map
        while True:
            if direccion == '^':
                if moveUp():
                    break
            elif direccion == 'v':
                if moveDown():
                    break                
            elif direccion == '<':
                if moveLeft():
                    break
            elif direccion == '>':
                if moveRight():
                    break

        print(total)

if __name__ == "__main__":
    Solution().main()