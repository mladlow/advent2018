#!/usr/bin/env python3

import re

'''
Both of these solutions aren't terribly efficient. What could be done using
math and some kind of spacial-aware area calculations?

What other interesting data structures could be in use here?
'''


def part_one(f):
    '''This solution uses two sets.

    The first set tracks the square inches seen
    so far. The second set tracks the square inches that we've seen at least
    twice.
    '''
    seen_coords, dup_coords = set(), set()
    dups = 0
    for claim in f:
        claim_parts = re.split('[ :,x]', claim.strip())
        # a claim part looks like ['#claim_id', '@', 'loffset', 'toffset', '', 'width', 'height']
        l_offset, t_offset, width, height = (int(val) for val in [
            claim_parts[2], claim_parts[3], claim_parts[5], claim_parts[6]])
        for i in range(l_offset, l_offset + width):
            for j in range(t_offset, t_offset + height):
                coord = (i, j)
                if coord not in seen_coords:
                    seen_coords.add(coord)
                elif coord in seen_coords and coord not in dup_coords:
                    dup_coords.add(coord)
                    dups += 1
    # Could also just do len(dup_coords) instead of counting everything
    print(f'found {dups} square inches of overlap')


def part_two(f):
    seen_coords = {}
    dup_coords = set()
    good_claims = set()
    for claim in f:
        claim_parts = re.split('[ :,x]', claim.strip())
        l_offset, t_offset, width, height = [int(val) for val in [
            claim_parts[2], claim_parts[3], claim_parts[5], claim_parts[6]]]
        claim_id = claim_parts[0]
        good_claims.add(claim_id)
        for i in range(l_offset, l_offset + width):
            for j in range(t_offset, t_offset + height):
                coord = (i, j)
                if coord not in seen_coords:
                    seen_coords[coord] = claim_id
                else:
                    dup_coords.add(coord)
                    # discard is safe to use even if the thing you're
                    # discarding isn't in the set
                    good_claims.discard(claim_id)
                    good_claims.discard(seen_coords[coord])
                '''
                elif coord in seen_coords and coord not in dup_coords:
                    dup_coords.add(coord)
                    good_claims.discard(claim_id)
                    good_claims.discard(seen_coords[coord])
                elif coord in seen_coords and coord in dup_coords:
                    good_claims.discard(claim_id)
                '''
    print(f'found good claims: {good_claims}')
    


if __name__ == '__main__':
    with open('input.txt') as f:
        part_two(f)
