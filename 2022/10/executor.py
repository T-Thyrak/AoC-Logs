from __future__ import annotations


class Executor:
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = instructions
        self.x = 1
        self.add_mode = False
        self.cycle = 1
        self.result_20_cycles = []
        self.screen = []
        
    def execute(self) -> Executor:
        while True:
            if len(self.instructions) == 0:
                break
            
            if self.cycle % 40 == 20:
                self.result_20_cycles.append(self.x * self.cycle)
        
            sprite_pos = (self.x - 1, self.x, self.x + 1)
            
            if (self.cycle - 1) % 40 in sprite_pos:
                print(f"Lit at cycle {self.cycle}")
                self.screen.append("#")
            else:
                self.screen.append(".")
            
            instruction = self.instructions.pop(0)
            if self.add_mode:
                self.add_mode = False
                self.x += int(instruction)
            else:
                # print(instruction)
                if instruction == "noop":
                    pass
                elif instruction == "addx":
                    self.add_mode = True
                else:
                    pass

            self.cycle += 1
        
        return self
            
    def get_20_signal(self) -> list[int]:
        return self.result_20_cycles
    
    def get_screen(self) -> list[str]:
        return self.screen