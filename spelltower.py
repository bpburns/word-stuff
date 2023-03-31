raw_grid = '''
abcdefg
hijklmn
opqrstu
vwxyz
'''

def get_grid_max_line_len(grid):
    max_len = 0
    for line in grid:
        line_len = len(line)
        if line_len > max_len:
            max_len = line_len
    return max_len

def pad_grid(grid):
    max_len = get_grid_max_line_len(grid)
    for line in grid:
        while len(line) < max_len:
            line.append(' ')

def get_grid_width(grid):
    width = get_grid_max_line_len(grid)
    return width

def get_grid_height(grid):
    height = len(grid)
    return height

def get_grid_dimensions(grid):
    width = get_grid_width(grid)
    height = get_grid_height(grid)
    return (height, width)

def wrap_grid(grid):
    dimensions = get_grid_dimensions(grid)
    width = dimensions[1]
    width += 2
    border_line = list('*' * width)
    for line in grid:
        line.insert(0, '*')
        line.append('*')
    grid.insert(0, border_line)
    grid.append(border_line)

def gen_grid(string):
    lines = string.strip().splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

grid = gen_grid(raw_grid)

pad_grid(grid)
wrap_grid(grid)


for line in grid:
    print(line)