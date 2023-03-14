from executor import Executor

def main() -> None:
    with open('asm.txt', 'r') as f:
        data = f.readlines()
        
    instructions = []
    
    for line in data:
        instructions.extend(translate_data(line))
        
    # print(instructions)
        
    result = Executor(instructions).execute()
    signal_20 = result.get_20_signal()
    print(f"20 + 40n: {signal_20}")
    print(f"Sum: {sum(signal_20)}")
    print()
    
    screen = result.get_screen()
    
    # chunk into 40 chars pieces
    screen = [screen[i:i+40] for i in range(0, len(screen), 40)]
    
    for row in screen:
        print("".join(row))
    pass


def translate_data(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("noop"):
        return [line]
    elif line.startswith("addx"):
        return line.split(" ")
    else:
        return ["noop"]

if __name__ == '__main__':
    main()