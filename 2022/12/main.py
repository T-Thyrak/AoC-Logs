from rich.traceback import install
install(show_locals=True)

from tree import Tree

def main() -> None:
    with open("elev.txt", "r") as f:
        data = f.readlines()
        
    data = [line.strip() for line in data]
        
    print(len(data), len(data[0]))
    
    root = Tree("S")
    
    start_pos = [0, 0]
    for line in data:
        for char in line:
            if char == "S":
                start_pos = [data.index(line), line.index(char)]
    
    visited = [tuple(start_pos)]
    search_queue = []
    
    for df, dl in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if start_pos[0] + df >= 0 and start_pos[0] + df < len(data) and start_pos[1] + dl >= 0 and start_pos[1] + dl < len(data[0]) and data[start_pos[0] + df][start_pos[1] + dl] == "a":
            search_queue.append((start_pos[0] + df, start_pos[1] + dl, root))
            
    while search_queue:
        # print(list(map(lambda x: (x[0], x[1]), search_queue)))
        # pop the first element
        current_pos = search_queue.pop(0)
        
        if current_pos[0] < 0 or current_pos[0] >= len(data) or current_pos[1] < 0 or current_pos[1] >= len(data[0]):
            continue
        
        # mark the current position as visited
        if (current_pos[0], current_pos[1]) in visited:
            raise Exception("Visited twice")
        
        # add to tree
        tree = current_pos[2].add_child(data[current_pos[0]][current_pos[1]])
        
        # check if the current position is end
        if data[current_pos[0]][current_pos[1]] == "E":
            print(f"found E! last position was {current_pos[2].data}")
            # check if the last position was a z
            if current_pos[2].data == "z":
                end_tree = tree
                break
        else:
            visited.append((current_pos[0], current_pos[1]))
        
        # for each direction
        for df, dl in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # if not out of range and has not visited
            # and the next position is higher by at most 1
            # add to queue
            new_i = current_pos[0] + df
            new_j = current_pos[1] + dl
            
            if (not 
                    (
                        new_i < 0 
                        or new_i >= len(data) 
                        or new_j < 0 
                        or new_j >= len(data[0])
                    )
                ) and (
                    (new_i, new_j) not in visited
                ) and (
                    (new_i, new_j) not in list(map(lambda x: (x[0], x[1]), search_queue))
                ) and higher_by_at_most_1(
                    data[current_pos[0]][current_pos[1]],
                    data[new_i][new_j]
                ):
                search_queue.append((new_i, new_j, tree))

    plain = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in visited:
                plain[i][j] = f"\033[38;2;{ord(data[i][j]) - 97 + 31};{ord(data[i][j]) - 97 + 31};{ord(data[i][j]) - 97 + 31}m{data[i][j]}\033[0m"
                
    for line in plain:
        print("".join(line))
    
    path = []
    while end_tree:
        path.append(end_tree.data)
        end_tree = end_tree.get_parent()
        
    path.reverse()
    
    print(path)
    print(len(path))
    pass


def higher_by_at_most_1(current: str, goto: str) -> bool:
    if ord(goto) - ord(current) > 1:
        return False
    
    return True


if __name__ == '__main__':
    main()
