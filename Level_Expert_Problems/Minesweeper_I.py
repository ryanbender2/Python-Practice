""" Minesweeper I — Grid
  This challenge is based on the game Minesweeper.

  Create a function that takes a list of # and -,
  where each hash (#) represents a mine and each
  dash (-) represents a mine-free spot. Return a
  list where each dash is replaced by a digit
  indicating the number of mines immediately adjacent
  to the spot (horizontally, vertically, and diagonally).
"""


def num_grid(game_grid):
    # Find bomb locations (#)
    bomb_locations = []
    for column in range(len(game_grid)):
        for row in range(len(game_grid)):
            if game_grid[column][row] == '#':
                bomb_locations.append((column, row))
            else:
                game_grid[column][row] = 0

    # Add surrouding bomb amounts around each bomb
    for bomb in bomb_locations:
        for bomb_amounts in [(bomb[0] - 1, bomb[1] - 1),
                  (bomb[0] - 1, bomb[1]),
                  (bomb[0] - 1, bomb[1] + 1),
                  (bomb[0], bomb[1] - 1),
                  (bomb[0], bomb[1] + 1),
                  (bomb[0] + 1, bomb[1] - 1),
                  (bomb[0] + 1, bomb[1]),
                  (bomb[0] + 1, bomb[1] + 1)]:
            try:  # index error checking for edges of grid
                if -1 not in [bomb_amounts[0], bomb_amounts[1]]:
                    if game_grid[bomb_amounts[0]][bomb_amounts[1]] != '#':
                        game_grid[bomb_amounts[0]][bomb_amounts[1]] += 1
            except IndexError:
                None

    # Convert ints back to strings
    for column in range(len(game_grid)):
        for row in range(len(game_grid)):
            game_grid[column][row] = str(game_grid[column][row])

    return game_grid


print(num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "#", "-"],
  ["-", "-", "-", "-", "-"]]))
