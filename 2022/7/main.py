from path import Path
from pathtree import PathTree
from pathnode import PathNode

from time import perf_counter_ns

def main():
    t_parse = []
    t_part1 = []
    t_part2 = []
    
    for i in range(1000):
        parse_time_start = perf_counter_ns()
        tree = parse_tree("term.txt")
        parse_time_end = perf_counter_ns()
        
        t_parse.append(parse_time_end - parse_time_start)
    
    part1_ans = 0
    for i in range(1000):
        ans = 0
        
        def addtoa(node: PathNode):
            nonlocal ans
            if not node.is_file() and node.get_size() < 100000:
                ans += node.get_size()
        
        part1_time_start = perf_counter_ns()
        tree.walk(addtoa)
        part1_time_end = perf_counter_ns()
        
        t_part1.append(part1_time_end - part1_time_start)
        
        part1_ans = ans
            
    unused = 70_000_000 - tree._root.get_size()
    target_unused = 30_000_000
    
    part2_ans = 0
    for i in range(1000):
        minimum_unused_size = 70_000_000
        
        def smallest_deletable_directory(node: PathNode):
            nonlocal minimum_unused_size
            if not node.is_file() and node.get_size() < minimum_unused_size and node.get_size() + unused > target_unused:
                minimum_unused_size = node.get_size()
        
        part2_time_start = perf_counter_ns()
        tree.walk(smallest_deletable_directory)
        part2_time_end = perf_counter_ns()
        
        t_part2.append(part2_time_end - part2_time_start)
        
        part2_ans = minimum_unused_size
    
    print(f"part 1 : {part1_ans}")
    print(f"part 2 : {part2_ans}")
    
    print(f"parse time: [~ {sum(t_parse) / len(t_parse)} ns, ^ {max(t_parse)} ns, v {min(t_parse)} ns]")
    print(f"part1 time: [~ {sum(t_part1) / len(t_part1)} ns, ^ {max(t_part1)} ns, v {min(t_part1)} ns]")
    print(f"part2 time: [~ {sum(t_part2) / len(t_part2)} ns, ^ {max(t_part2)} ns, v {min(t_part2)} ns]")
    
    pass


def test():
    tree = PathTree()
    tree.add_dir("a")
    tree.add_dir("b")
    tree.cd("a")
    tree.add_file("c", 10)
    tree.cd("..")
    tree.cd("b")
    tree.add_dir("d")
    tree.cd("d")
    tree.add_file("e", 2000)
    # tree.cd("/")
    tree.walk(callback=lambda node: print((node, len(node._children), node.get_size())))
    
    pass

def parse_tree(filename: str):
    tree = PathTree()
    
    with open("term.txt", "r") as f:
        lines = iter(f.readlines())
    
    for line in lines:
        line = line.strip()
        if line.startswith("$"):
            if line.startswith("$ cd "):
                tree.cd(line[5:].strip())
        else:
            if line.startswith("dir "):
                # add a dir to the tree
                tree.add_dir(line[4:].strip())
            else:
                size, filename = line.split()
                tree.add_file(filename, int(size))
                
    return tree
    
if __name__ == "__main__":
    main()