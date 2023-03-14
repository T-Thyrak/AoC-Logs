from time import perf_counter_ns

from string import ascii_letters
scores = {letter:n for n,letter in enumerate(ascii_letters, 1)}

with open('sacks.txt') as f:
    raw_data = f.read()

t = []
def f_part_one(d):
    data = d.splitlines()
    score = 0
    for line in data:
        l = len(line)//2
        p1, p2 = line[0:l],line[l:]
        target = list(set(p1) & set(p2))
        target = target[0]
        score+=scores[target]
    return score

for i in range(1000):
    data = open('sacks.txt', 'r').read().splitlines()
    p1 = perf_counter_ns()
    a1 = f_part_one(raw_data)
    p2 = perf_counter_ns()
    t.append(p2 - p1)
    
print(f"Answer to part 1: {a1}")
# print(f"Answer to part 2: {a2}")

print(f"Time for both part: [~ {sum(t)/len(t)}ns, ^ {max(t)}ns, v {min(t)}ns]")
