#!/usr/bin/env python3

from collections import Counter

def part_one():
    with open('input.txt') as f:
        twos_count, threes_count = 0, 0
        for box_id in f:
            char_counter = Counter(box_id)
            found_two, found_three = False, False
            for count in char_counter.values():
                if count == 2:
                    found_two = True
                elif count == 3:
                    found_three = True
                if found_two and found_three:
                    break
            if found_two:
                twos_count += 1
            if found_three:
                threes_count += 1
        checksum = twos_count * threes_count
        print(f'part one answer: {checksum}')


def find_boxes(box_ids):
    '''Not terribly smart O(n^2) solution.'''
    for base in box_ids:
        for compare in box_ids:
            num_diffs = 0
            # zip would be better
            for i, c in enumerate(base):
                if c != compare[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    break
            if num_diffs == 1:
                print(f'found them! {base} {compare}')
                return base, compare

def part_two():
    box_ids = []
    with open('input.txt') as f:
        box_ids = [line.strip() for line in f]

    box1, box2 = find_boxes(box_ids)
    shared_letters = []
    for i, c in enumerate(box1):
        if c == box2[i]:
            shared_letters.append(c)
    result = ''.join(shared_letters)
    print(f'shared letters: {result}')

'''
Feel like there is some solution by creating a 'score' for each box:
    (use powers)
        # acb (0 in 0, 2 in 1, 1 in 2) [0,3,3] -> 6
        # aba (0 in 0, 1 in 1, 0 in 2) [0,2,2] -> 4
        # abb (0 in 0, 1 in 1, 1 in 2) [0,2,3] -> 5
        # dcb (3 in 0, 2 in 1, 1 in 2) [3,3,3] -> 9

aaa [0,1,2] -> 3
abb [0,2,3] -> 5
baa [1,1,2] -> 4

# could sort whole words and then sort word[1:]

make scores omitting a character each time

use tries? (yes, use a suffix tree/trie with a set of 'grandchildren' strings) O(n*m)
'''

if __name__ == '__main__':
    part_two()
