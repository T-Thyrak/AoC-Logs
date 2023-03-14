from monkey import Monkey

def main() -> None:

    monkeys = Monkey.get_default()
    testers = [monkey.tester for monkey in monkeys]
    
    for i in range(10000):
        print(f"Round {i}:")
        for monkey in monkeys:
            while not monkey.inspected_all_items():
                worry, new_id = monkey.inspect(testers=testers, relief=False)
                monkeys[new_id].items.append(worry)
            
        # print(f"Round {i}:")
        # for monkey in monkeys:
            # print(f"Monkey {monkey.id}: {monkey.items}")
        
    inspect_counts = [monkey.inspect_count for monkey in monkeys]
    part_answer = product(top(inspect_counts, 2))
    print(f"Part answer: {part_answer}")
    pass

def product(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result

def top(numbers: list[int], count: int) -> list[int]:
    return sorted(numbers, reverse=True)[:count]

if __name__ == '__main__':
    main()
