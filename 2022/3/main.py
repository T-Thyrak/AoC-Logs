from time import perf_counter_ns

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open('sacks.txt', 'r') as f:
    t1 = []
    t2 = []
    
    datas = f.readlines()
    
    for i in range(1000):
        p1 = perf_counter_ns()
        a1 =                                                                                                                                                        sum([ord(char) - ord('A') + 27 if ord(char) >= ord('A') and ord(char) <= ord('Z') else ord(char) - ord('a') + 1 for char in [list(first_part & second_part)[0] for first_part, second_part in [(set(line[:int(len(line)/2)]), set(line[int(len(line)/2):])) for line in list(map(lambda s: s.strip(), datas))]]])
        p2 = perf_counter_ns()
        a2 =                                                                                                                                                        sum([ord(char) - ord('A') + 27 if ord(char) >= ord('A') and ord(char) <= ord('Z') else ord(char) - ord('a') + 1 for char in [list(set(s1) & set(s2) & set(s3))[0] for s1, s2, s3 in list(chunks(list(map(lambda s: s.strip(), datas)), 3))]])
        p3 = perf_counter_ns()

        t1.append(p2 - p1)
        t2.append(p3 - p2)
        
    print(f"Answer to part 1: {a1}")
    print(f"Answer to part 2: {a2}")
    print()
    print(f"Time for part 1: [~ {sum(t1)/len(t1)}ns, ^ {max(t1)}ns, v {min(t1)}ns]")
    print(f"Time for part 2: [~ {sum(t2)/len(t2)}ns, ^ {max(t2)}ns, v {min(t2)}ns]")