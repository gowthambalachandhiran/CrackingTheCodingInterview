def printKMoves(K):
    # Define directions: 0 - right, 1 - down, 2 - left, 3 - up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize an empty grid with a white cell at the center
    grid = {(0, 0): 0}  # 0 represents white, 1 represents black
    ant_position = (0, 0)
    ant_direction = 0  # Initial direction is right

    for _ in range(K):
        # Check the color of the current cell
        current_color = grid.get(ant_position, 0)  # Default to white if not found

        # Update the color and direction based on the rules
        if current_color == 0:  # White
            grid[ant_position] = 1  # Change color to black
            ant_direction = (ant_direction + 1) % 4  # Turn right
        else:  # Black
            grid[ant_position] = 0  # Change color to white
            ant_direction = (ant_direction - 1) % 4  # Turn left

        # Move the ant forward
        ant_position = (
            ant_position[0] + directions[ant_direction][0],
            ant_position[1] + directions[ant_direction][1],
        )

    # Find the bounds of the grid
    min_x = min(grid, key=lambda x: x[0])[0]
    max_x = max(grid, key=lambda x: x[0])[0]
    min_y = min(grid, key=lambda x: x[1])[1]
    max_y = max(grid, key=lambda x: x[1])[1]

    # Print the final grid
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print("X" if grid.get((i, j), 0) == 1 else " ", end="")
        print()


# Example usage:
printKMoves(100)
