def generate_diving_board_lengths(k, big_plank_length, small_plank_length, current_length=0, memo={}):
    if k == 0:
        return [current_length]
    
    if (k, current_length) in memo:
        return memo[(k, current_length)]
    
    results = []
    # Try using a big plank
    results += generate_diving_board_lengths(k - 1, big_plank_length, small_plank_length, current_length + big_plank_length, memo)
    # Try using a small plank
    results += generate_diving_board_lengths(k - 1, big_plank_length, small_plank_length, current_length + small_plank_length, memo)
    
    memo[(k, current_length)] = results
    return results

# Example usage:
k = 4  # Number of planks
big_plank_length = 3  # Length of a big plank
small_plank_length = 1  # Length of a small plank
diving_board_lengths = generate_diving_board_lengths(k, big_plank_length, small_plank_length)
print(sorted(list(set(diving_board_lengths))))

# Example usage:
k = 2  # Number of planks
big_plank_length = 2  # Length of a big plank
small_plank_length = 1  # Length of a small plank
diving_board_lengths = generate_diving_board_lengths(k, big_plank_length, small_plank_length)
print(diving_board_lengths)
