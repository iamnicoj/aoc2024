def turn_right(direction):
    # Directions are represented as (dx, dy) for movements
    # Let's say: up = (-1, 0), right = (0, 1), down = (1, 0), left = (0, -1)
    # Turning right means cycling through these directions
    if direction == (-1, 0):  # up
        return (0, 1)         # right
    elif direction == (0, 1): # right
        return (1, 0)         # down
    elif direction == (1, 0): # down
        return (0, -1)        # left
    elif direction == (0, -1):# left
        return (-1, 0)        # up

def direction_from_char(ch):
    if ch == '^':
        return (-1, 0)
    elif ch == 'v':
        return (1, 0)
    elif ch == '<':
        return (0, -1)
    elif ch == '>':
        return (0, 1)
    else:
        return None

def char_from_direction(direction):
    if direction == (-1, 0):
        return '^'
    elif direction == (1, 0):
        return 'v'
    elif direction == (0, -1):
        return '<'
    elif direction == (0, 1):
        return '>'

def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def simulate(grid, start_r, start_c, start_dir):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    r, c = start_r, start_c
    direction = start_dir
    
    visited_states = set()
    
    while True:
        state = (r, c, direction)
        if state in visited_states:
            # We have a repeated state -> loop detected
            return "loop"
        visited_states.add(state)
        
        # Check cell in front
        nr, nc = r + direction[0], c + direction[1]
        
        # If front is out of bounds, guard leaves the map
        if not in_bounds(nr, nc, rows, cols):
            return "leave"
        
        # If front cell is blocked, turn right
        if grid[nr][nc] == '#':
            direction = turn_right(direction)
        else:
            # Move forward
            r, c = nr, nc

def main():
    # Read input from file "input.txt"
    with open("day6/aoc06s.txt", "r") as f:
        lines = [list(line.rstrip('\n')) for line in f]
    
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    
    # Find guard start position and direction
    start_r, start_c = None, None
    start_dir = None
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] in '^v<>':
                start_r, start_c = i, j
                start_dir = direction_from_char(lines[i][j])
                lines[i][j] = '.'  # Replace guard start with empty floor
                break
        if start_r is not None:
            break
    
    # Original simulation result (without new obstacle)
    # Just for reference, not strictly needed for part two.
    # original_result = simulate(lines, start_r, start_c, start_dir)
    
    loop_count = 0
    # Try placing a new obstacle in every empty cell except the start position
    for i in range(rows):
        for j in range(cols):
            # We cannot place an obstacle at the guard's starting position
            if (i, j) == (start_r, start_c):
                continue
            if lines[i][j] == '.':
                # Temporarily place an obstacle
                lines[i][j] = '#'
                
                result = simulate(lines, start_r, start_c, start_dir)
                if result == "loop":
                    loop_count += 1
                
                # Remove the obstacle
                lines[i][j] = '.'
    
    print(loop_count)

if __name__ == "__main__":
    main()