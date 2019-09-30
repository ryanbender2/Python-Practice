""" Minesweeper I — Grid
  This challenge is based on the game Minesweeper.

  Create a function that takes a list of # and -,
  where each hash (#) represents a mine and each
  dash (-) represents a mine-free spot. Return a
  list where each dash is replaced by a digit
  indicating the number of mines immediately adjacent
  to the spot (horizontally, vertically, and diagonally).
"""


def num_grid(lst):
    # Find bomb locations (#)
    bomb_locations = []
    for column in range(len(lst)):
        for row in range(len(lst)):
            if lst[column][row] == '#':
                bomb_locations.append((column, row))
            else:
                lst[column][row] = 0

    # Add mines around each bomb
    for b in bomb_locations:
        for l in [(b[0] - 1, b[1] - 1),
                  (b[0] - 1, b[1]),
                  (b[0] - 1, b[1] + 1),
                  (b[0], b[1] - 1),
                  (b[0], b[1] + 1),
                  (b[0] + 1, b[1] - 1),
                  (b[0] + 1, b[1]),
                  (b[0] + 1, b[1] + 1)]:
            try:
                if -1 not in [l[0], l[1]]:
                    if lst[l[0]][l[1]] != '#':
                        lst[l[0]][l[1]] += 1
            except IndexError:
                None

    # Convert ints back to strings
    for column in range(len(lst)):
        for row in range(len(lst)):
            lst[column][row] = str(lst[column][row])

    return lst


print(num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]]))
