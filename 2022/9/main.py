import sys

from time import perf_counter_ns

class RopeKnot:
    def __init__(self):
        self.x = 0
        self.y = 0

def main(rope_length: int, data, verbose: bool = False) -> None:
    if not verbose:
        def print(*args, **kwargs): pass
    
    visited: set[tuple[int, int]] = set()
    knots = [RopeKnot() for _ in range(rope_length)]
    head = knots[0]
    tail = knots[-1]
    
    visited.add((tail.x, tail.y))
    for line in data:
        direction, distance = line[0], int(line[2:])
        print(f"--LINE: {line}")
        
        for _ in range(distance):
            if direction == "U":
                head.y += 1
            elif direction == "D":
                head.y -= 1
            elif direction == "R":
                head.x += 1
            elif direction == "L":
                head.x -= 1
            else:
                raise ValueError(f"Invalid direction: {direction}")
            
            for k in range(rope_length - 1):
                print(f"updating knot number {k + 1}")
                knots[k + 1].x, knots[k + 1].y = update_tail(knots[k].x, knots[k].y, knots[k + 1].x, knots[k + 1].y, verbose=verbose)
                
            print("---End Update---")
            print()
        
            visited.add((tail.x, tail.y))
        
    print(f"Visited {len(visited)} locations")
    return visited

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def update_tail(head_x, head_y, tail_x, tail_y, verbose=False):
    if not verbose:
        def print(*args, **kwargs): pass
    
    print(f"---Update---")
    print(f"New Head Position: ({head_x}, {head_y})")
    print(f"Old Tail Position: ({tail_x}, {tail_y})")
    
    # if head_x and tail_x, and head_y and tail_y differs by at most 1, then
    # don't do anything

    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        print(f"Close Enough: No movement")
        return tail_x, tail_y
    
    # otherwise, move the tail in the direction of the head
    return sign(head_x - tail_x) + tail_x, sign(head_y - tail_y) + tail_y

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    t1 = []
    t2 = []
    
    for i in range(10):
        st_time = perf_counter_ns()
        a1 = main(2, lines)
        t1.append(perf_counter_ns() - st_time)
        
        st_time = perf_counter_ns()
        a2 = main(10, lines)
        t2.append(perf_counter_ns() - st_time)
    
    print(f"Answer part 1: {len(a1)}")
    print(f"Answer part 2: {len(a2)}")
    
    print(f"A1 time: [~ {sum(t1)/len(t1)}ns, ^ {max(t1)}ns, v {min(t1)}ns]")
    print(f"A2 time: [~ {sum(t2)/len(t2)}ns, ^ {max(t2)}ns, v {min(t2)}ns]")
    
    verbose = False
    
    if verbose:
        plot = a1
        
        # the plot is a set of tuples of visited locations
        
        # create a 2d array of the plot
        # the width is the max(x) - min(x) + 1
        # the height is the max(y) - min(y) + 1
        # the origin is the min(x), min(y)
        
        x = [i[0] for i in plot]
        y = [i[1] for i in plot]
        
        width = max(x) - min(x) + 1
        height = max(y) - min(y) + 1
        
        origin = (min(x), min(y))
        
        # pad the edges by 1 to make sure the plot is fully visible
        width += 2
        height += 2
        
        origin = (origin[0] - 1, origin[1] - 1)
        
        # create the 2d array
        plot_2d = [["." for _ in range(width)] for _ in range(height)]
        
        # fill in the plot
        for i in plot:
            plot_2d[height - (i[1] - origin[1]) - 1][i[0] - origin[0]] = "#"
        
        # set the origin to "s"
        plot_2d[origin[1] - 1][-origin[0]] = "s"
        
        lol_plot = []
        # print the plot
        for i in plot_2d:
            lol_plot.append("".join(i))
            
        with open("plot.txt", "w") as f:
            f.write("\n".join(lol_plot))