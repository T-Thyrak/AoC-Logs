import re

from stack import Stack
from parse import parse

from time import perf_counter_ns

def main():
    start_time = perf_counter_ns()
    
    # Read the file.
    with open('stacks.txt') as f:
        string = f.read()
    
    reading_time = perf_counter_ns()
    
    # Parse the file.
    stacks, moves = parse(string)
    
    parsing_time = perf_counter_ns()
    
    # Perform the moves.
    for count, source, target in moves:
        stacks[source - 1].move(count, stacks[target - 1])
        
    moving_time = perf_counter_ns()
        
    # Get the top of each stack.
    tops = [stack.peek() for stack in stacks]
    
    # Print the result.
    print(f"Part 1: {''.join(tops)}")
    
    stacks, moves = parse(string)
    
    part_2_time = perf_counter_ns()
    for count, source, target in moves:
        stacks[source - 1].move(count, stacks[target - 1], retain_order=True)
    part_2_end_time = perf_counter_ns()
        
    tops = [stack.peek() for stack in stacks]
    
    print(f"Part 2: {''.join(tops)}")
    
    print(f"Reading time: {reading_time - start_time} ns")
    print(f"Parsing time: {parsing_time - reading_time} ns")
    print(f"Moving (Part 1) time: {moving_time - parsing_time} ns")
    print(f"Moving (Part 2) time: {part_2_end_time - part_2_time} ns")
    
    pass

if __name__ == '__main__':
    main()