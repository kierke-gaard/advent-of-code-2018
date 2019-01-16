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

P = collections.namedtuple('P', 'x y')
# water and clay are sets of coordinates
Grid = collections.namedtuple('Grid', 'size spring clay')

def grid_1()->Grid:
    clay = set(P(*p) for p in 
                ((0,2), (0,3), (0,4),
                 (1,4), (2,4),
                 (3,4),
                 (4,4), (4,3)))
    spring = P(1,0)
    size = P(8,9)
    return Grid(size, spring, clay)

def grid_str(grid, water=())->str:
    s = ''
    for y in range(grid.size.y):
        for x in range(grid.size.x):
            p = P(x,y) 
            if p == grid.spring:
                s += '+'
            elif p in grid.clay:
                s += '#'
            elif p in water:
                s += '|'
            else:
                s += ' '
        s += '\n'
    return s

def maybe_first_clay_layer(spring: P, clay):
    try:
        return min(p.y for p in clay if p.x==spring.x and p.y>=spring.y)
    except ValueError:
        return None

def column(spring: P, y_end):
    return tuple(P(spring.x, y) for y in range(spring.y, y_end + 1))

def row(spring: P, x_end):
    if spring.x <= x_end:
        r = range(spring.x, x_end + 1)
    else:
        r = range(x_end, spring.x + 1)
    return tuple(P(x,spring.y) for x in r)

def horizontal_endpoint(spring: P, direction, grid:Grid, water):
    # Returns the end point of water flow in a horizontal direction
    # and whether this end point will give rise to vertical downflow (True)
    if direction == 'left':
        neighbor = P(spring.x - 1, spring.y)
    else: #right
        neighbor = P(spring.x + 1, spring.y)
    if neighbor in grid.clay:
        return spring, False
    else:
        neighbor_ground = P(neighbor.x, neighbor.y + 1)
        if neighbor_ground in water or neighbor_ground in grid.clay:
            return horizontal_endpoint(neighbor, direction, grid, water)
        else:
            return neighbor, True

def horizontal_flow(spring: P, grid: Grid, water: set):
    # Changes water, returns none
    left, left_is_spring = horizontal_endpoint(
                            spring, 'left', grid, water)
    water |= set(row(spring, left.x))
    right, right_is_spring = horizontal_endpoint(
                              spring, 'right', grid, water)
    water |= set(row(spring, right.x))
    if left_is_spring:
        vertical_flow(P(left.x, spring.y), grid, water)
    if right_is_spring:
        vertical_flow(P(right.x, spring.y), grid, water)
    if not left_is_spring and not right_is_spring:
        spring_one_level_up = P(spring.x, spring.y - 1)
        horizontal_flow(spring_one_level_up, grid, water)

def vertical_flow(spring: P, grid: Grid, water: set):
    # Changes water, returns none
    y_first_clay = maybe_first_clay_layer(spring, grid.clay)
    if y_first_clay:
       water_level = y_first_clay - 1
       new_spring = P(spring.x, water_level)
       water |= set(column(spring, water_level))
       horizontal_flow(new_spring, grid, water)
    else:
        water |= set(column(spring, grid.size.y))