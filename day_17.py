"""
Water (|) springs from a source (+) and falls down a two-dimensional grid.
In its flow downwards it fills clay barriers (#), eg like

   012345678
 0  +
 1  |
 2 #|||||
 3 #|||#|
 4 #####|
 5      |
 6      |||||
 7     |#|#|
 8     |###|
 9     |   |

Given the clay and a spring, how will the grid finally look like?
"""

import collections

Coordinate = collections.namedtuple('Coordinate', 'x y')
# water and clay are sets of coordinates
# size is a coordinate with the max for the x and y achses
Grid = collections.namedtuple('Grid', 'size spring clay water')

def initial_grid():
    clay = set(Coordinate(*p) for p in ((0,2), (0,3), (0,4),
                                         (1,4), (2,4), (3,4), (4,4), (4,3)
                                         ))
    spring = Coordinate(1,0)
    size = Coordinate(8,9)
    water = set()
    return Grid(size, spring, clay, water)

def grid_str(grid):
    s = ''
    for y in range(grid.size.y + 1):
        for x in range(grid.size.x + 1):
            p = Coordinate(x,y) 
            if p == grid.spring:
                s += '+'
            elif p in grid.clay:
                s += '#'
            elif p in grid.water:
                s += '|'
            else:
                s += ' '
        s += '\n'
    return s

# Tests
g = initial_grid()
print(grid_str(initial_grid()))
