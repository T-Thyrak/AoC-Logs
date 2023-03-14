from __future__ import annotations
from typing import Callable

from math import lcm

class Monkey:
    def get_default() -> list[Monkey]:
        return [
            Monkey(
                id=0,
                items=[
                    98, 97, 98, 55, 56, 72
                ],
                operation=lambda x: x * 13,
                test=lambda x: 4 if x % 11 == 0 else 7,
                tester=11
            ),
            Monkey(
                id=1,
                items=[
                    73, 99, 55, 54, 88, 50, 55
                ],
                operation=lambda x: x + 4,
                test=lambda x: 2 if x % 17 == 0 else 6,
                tester=17
            ),
            Monkey(
                id=2,
                items=[
                    67, 98
                ],
                operation=lambda x: x * 11,
                test=lambda x: 6 if x % 5 == 0 else 5,
                tester=5
            ),
            Monkey(
                id=3,
                items=[
                    82, 91, 92, 53, 99
                ],
                operation=lambda x: x + 8,
                test=lambda x: 1 if x % 13 == 0 else 2,
                tester=13
            ),
            Monkey(
                id=4,
                items=[
                    52, 62, 94, 96, 52, 87, 53, 60
                ],
                operation=lambda x: x * x,
                test=lambda x: 3 if x % 19 == 0 else 1,
                tester=19
            ),
            Monkey(
                id=5,
                items=[
                    94, 80, 84, 79
                ],
                operation=lambda x: x + 5,
                test=lambda x: 7 if x % 2 == 0 else 0,
                tester=2
            ),
            Monkey(
                id=6,
                items=[
                    89
                ],
                operation=lambda x: x + 1,
                test=lambda x: 0 if x % 3 == 0 else 5,
                tester=3
            ),
            Monkey(
                id=7,
                items=[
                    70, 59, 63
                ],
                operation=lambda x: x + 3,
                test=lambda x: 4 if x % 7 == 0 else 3,
                tester=7
            )
        ]
        
    def get_test_monkeys() -> list[Monkey]:
        return [
            Monkey(
                id=0,
                items=[
                    79, 98
                ],
                operation=lambda x: x * 19,
                test=lambda x: 2 if x % 23 == 0 else 3,
                tester=23
            ),
            Monkey(
                id=1,
                items=[
                    54, 65, 75, 74
                ],
                operation=lambda x: x + 6,
                test=lambda x: 2 if x % 19 == 0 else 0,
                tester=19
            ),
            Monkey(
                id=2,
                items=[
                    79, 60, 97
                ],
                operation=lambda x: x * x,
                test=lambda x: 1 if x % 13 == 0 else 3,
                tester=13
            ),
            Monkey(
                id=3,
                items=[
                    74
                ],
                operation=lambda x: x + 3,
                test=lambda x: 0 if x % 17 == 0 else 1,
                tester=17
            )
        ]
    
    def __init__(self, id: int, items: list[int], operation: Callable[[int], int], test: Callable[[int], int], tester: int) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.tester = tester
        self.inspect_count = 0
    
    def inspect(self, testers: list[int], relief: bool = True) -> tuple[int, int]:
        worry = self.items.pop(0)
        new_worry = self.operation(worry) % big_lcm(testers)
        if relief:
            reliefed = new_worry // 3
        else:
            reliefed = new_worry
        new_id = self.test(reliefed)
        
        self.inspect_count += 1
        
        return reliefed, new_id
    
    def inspected_all_items(self) -> bool:
        return len(self.items) == 0
    
def big_lcm(numbers: list[int]) -> int:
    l = 1
    for i in numbers:
        l = lcm(l, i)
    return l