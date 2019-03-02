#!/usr/bin/env python3

def solve(numbers):
    frequency = 0
    tracker = {frequency}
    index = 0
    while True:
        frequency += numbers[index]
        if frequency in tracker:
            print('found duplicate frequency {}!'.format(frequency))
            return
        else:
            tracker.add(frequency)
        index += 1
        if index >= len(numbers):
            index = 0


if __name__ == '__main__':
    values = []
    with open('input1.txt') as f:
        for line in f:
            try:
                values.append(int(line))
            except:
                pass
    solve(values)
        
