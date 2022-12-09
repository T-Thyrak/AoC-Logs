def parse_grid(filename: str) -> list[list]:
    with open(filename) as f:
        return [list(map(lambda x: int(x), line.strip())) for line in f]