from wordlist import WORD_LIST, WORD_TRIE
from copy import deepcopy
import time

def search(prefix):
    results = []
    for word in WORD_LIST:
        if word.startswith(prefix):
            results.append(word)
    return results


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

def print_grid(grid):
    for line in grid:
        for cell in line:
            print(cell, end='')
        print()

'''
123
8?4
765
'''
def walk_cell(grid, prefix, x, y):

    results = set()

    if x < 0 or y < 0:
        return results
    try:
        value = grid[y][x]
    except IndexError:
        return results

    if value in {'*', ' '}:
        return results

    prefix = prefix + value
    result = search(prefix)
    print_grid(grid)
    print('Prefix:', prefix)
    print('Num results:', len(result))
    if len(result) == 0:
        return results

    if len(prefix) > 2 and prefix in WORD_LIST:
        results.add(prefix)

    grid = deepcopy(grid)
    grid[y][x] = '*'

    one = (x - 1, y + 1)
    results.update(walk_cell(grid, prefix, one[0], one[1]))
    two = (x, y + 1)
    results.update(walk_cell(grid, prefix, two[0], two[1]))
    three = (x + 1, y + 1)
    results.update(walk_cell(grid, prefix, three[0], three[1]))
    four = (x + 1, y)
    results.update(walk_cell(grid, prefix, four[0], four[1]))
    five = (x + 1, y - 1)
    results.update(walk_cell(grid, prefix, five[0], five[1]))
    six = (x, y - 1)
    results.update(walk_cell(grid, prefix, six[0], six[1]))
    seven = (x - 1, y - 1)
    results.update(walk_cell(grid, prefix, seven[0], seven[1]))
    eight = (x - 1, y)
    results.update(walk_cell(grid, prefix, eight[0], eight[1]))

    return results
    
grid = gen_grid(raw_grid)

pad_grid(grid)
wrap_grid(grid)

print_grid(grid)

grid_width = get_grid_width(grid)
grid_height = get_grid_height(grid)
print('width', grid_width, 'height', grid_height)

results = set()
for x in range(grid_width):
    for y in range(grid_height):
        print(f'Scanning position {x}, {y}')
        results.update(walk_cell(grid, '', x, y))
print(len(results))
for result in sorted(results, key=lambda x: len(x)):
    print(result)
