#!/usr/bin/env python3

from sets import Set

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def new_orientation(facing, direction):
    if direction[0] == 'R':
        new_facing = facing + 1
        if new_facing > 3:
            return NORTH
        return facing + 1
    new_facing = facing - 1
    if new_facing < 0:
        return WEST
    return facing - 1

def new_distance(facing, direction):
    direction_amount = direction[1:]
    if facing == NORTH or facing == EAST:
        return int(direction_amount)
    return int(direction_amount) * -1

def move(facing, direction):
    next_orientation = new_orientation(facing, direction)
    return (next_orientation, new_distance(next_orientation, direction))

def mark(facing, direction, start_coords):
    next_orientation = new_orientation(facing, direction)
    distance = new_distance(next_orientation, direction)
    coords = start_coords.split(',')

    x = int(coords[0])
    y = int(coords[1])
    if next_orientation == EAST:
        return [coords[0] + ',' + str(val+1) for val in range(y, y + distance)]
    elif next_orientation == WEST:
        return [coords[0] + ',' + str(val) for val in range(y + distance, y)]
    elif next_orientation == NORTH:
        return [str(val+1) + ',' + coords[1] for val in range(x, x + distance)]
    elif next_orientation == SOUTH:
        return [str(val) + ',' + coords[1] for val in range(x + distance, x)]
    return [];

def compute_distances(facing, directions):
    orientation = facing
    distances = [0, 0]
    for d in directions:
        toChange = move(orientation, d)
        orientation = toChange[0]
        distances[orientation % 2] += toChange[1]
    return (orientation, abs(distances[0]) + abs(distances[1]))

if __name__ == '__main__':
    directions = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5'
    directions = directions.split(', ')

    assert new_orientation(NORTH, 'R') == EAST
    assert new_orientation(EAST, 'R') == SOUTH
    assert new_orientation(WEST, 'L') == SOUTH
    assert new_orientation(NORTH, 'L') == WEST
    assert new_orientation(WEST, 'R') == NORTH
    assert new_orientation(SOUTH, 'L') == EAST

    assert new_distance(NORTH, 'R3') == 3
    assert new_distance(NORTH, 'R100') == 100
    assert new_distance(SOUTH, 'R2') == -2
    assert new_distance(EAST, 'L5') == 5

    assert move(NORTH, 'R3') == (EAST, 3)
    assert move(WEST, 'L2') == (SOUTH, -2)
    assert move(SOUTH, 'L5') == (EAST, 5)

    assert mark(NORTH, 'R3', '0,0') == ['0,1', '0,2', '0,3']
    assert mark(NORTH, 'L3', '1,1') == ['1,-2', '1,-1', '1,0']
    assert mark(WEST, 'L2', '0,0') == ['-2,0', '-1,0']
    assert mark(WEST, 'R4', '-1,-2') == ['0,-2', '1,-2', '2,-2', '3,-2']
    assert mark(SOUTH, 'L5', '1,0') == ['1,1', '1,2', '1,3', '1,4', '1,5']

    print mark(NORTH, 'R3', '0,0')
    print mark(EAST, 'L1', '0,3')
    print mark(NORTH, 'L1', '1,3')
    print mark(WEST, 'L1', '1,2')

    print Set(mark(NORTH, 'R3', '0,0')).intersection(mark(WEST, 'L1', '1,2'))
    print Set(mark(NORTH, 'R3', '0,0')).union(mark(EAST, 'L1', '0,3'))

    assert 0 % 2 == 0
    assert 1 % 2 != 0

    assert compute_distances(NORTH, ['R3', 'L5']) == (NORTH, 8)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1']) == (EAST, 9)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2']) == (SOUTH, 7)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5']) == (EAST, 12)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2']) == (SOUTH, 10)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3']) == (WEST, 7)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2']) == (SOUTH, 7)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5']) == (EAST, 12)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5']) == (SOUTH, 17)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5', 'L4']) == (EAST, 21)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5', 'L4', 'L3']) == (NORTH, 18)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5', 'L4', 'L3', 'R5']) == (EAST, 23)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5', 'L4', 'L6']) == (NORTH, 15)
    assert compute_distances(NORTH, ['R3', 'L5', 'R1', 'R2', 'L5', 'R2', 'R3', 'L2', 'L5', 'R5', 'L4', 'L7']) == (NORTH, 16)
    assert compute_distances(NORTH, ['R2', 'R2', 'R2']) == (WEST, 2)
    assert compute_distances(NORTH, ['R2', 'R2', 'R2', 'R2']) == (NORTH, 0)
    assert compute_distances(NORTH, ['L1', 'L2', 'L2', 'L5']) == (NORTH, 4)

    assert compute_distances(NORTH, ['R2', 'L3'])[1] == 5
    assert compute_distances(NORTH, ['R5', 'L5', 'R5', 'R3'])[1] == 12

    print(compute_distances(NORTH, directions))
