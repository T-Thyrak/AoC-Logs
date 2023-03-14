import re

from stack import Stack

def parse(string: str) -> tuple[list[Stack], list[tuple[int, int, int]]]:
    """Parse a string into a list of stacks and a list of moves.

    Args:
        string (str): The string to parse.

    Returns:
        tuple[list[Stack], list[tuple[int, int, int]]]: A tuple containing a list of stacks and a list of moves. Each moves is a tuple of three integers indicating count, source, and target in that order.
    """
    
    # Split the string into lines.
    lines = string.splitlines()
    
    # There should only be one line that starts with a number AFTER stripping.
    # The line contains the stacks numbers.
    # The amount of stacks is the maximum number in the line.
    number_line = [line for line in lines if len(line.strip()) > 0 and line.strip()[0].isdigit()][0]
    stacks_count = max(list(map(lambda x: int(x), number_line.split())))
    stacks = [Stack() for _ in range(stacks_count)]
    
    read_pos = 1
    read_line = 0
    for i in range(stacks_count):
        while not (read_char := lines[read_line][read_pos]).isdigit():
            if read_char != ' ':
                stacks[i].push(read_char)
            read_line += 1
        
        stacks[i].reverse()
        read_pos += 4
        read_line = 0

    # Find the position of the empty line.
    # This acts as a separator between the stacks and the moves.
    empty_line = [i for i, line in enumerate(lines) if line.strip() == ''][0]
    
    # Trash everything before the empty line, and the empty line itself.
    lines = lines[empty_line + 1:]
    
    # The rest of the lines should be moves.
    moves = []
    for line in lines:
        pattern = r"move (\d+) from (\d+) to (\d+)"
        groups = re.match(pattern, line).groups()
        
        moves.append(tuple(map(lambda x: int(x), groups)))
        
    return stacks, moves