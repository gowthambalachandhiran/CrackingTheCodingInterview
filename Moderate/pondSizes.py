def pondSizes(matrix):
    def dfs(r, c):
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] != 0:
            return 0

        size = 1
        matrix[r][c] = -1  # Mark the cell as visited

        # Explore all neighboring cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                size += dfs(r + dr, c + dc)

        return size

    sizes = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                sizes.append(dfs(r, c))

    return sizes

# Example usage:
matrix = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]

result = pondSizes(matrix)
print(result)  # Output: [1, 2, 4]
