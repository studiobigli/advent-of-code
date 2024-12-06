def parse_input():
    input_lines = []

    with open('day5/day5.txt', 'r') as f:
        while (line := f.readline()):
            input_lines.append(line.rstrip('\n'))

    data = { "rules":  [(line.partition("|")[0], line.partition("|")[2]) 
                        for line in input_lines if line.partition("|")[1] == "|"],
            "updates": [line.split(",") for line in input_lines if "," in line]}
    
    return data

def part1():
    rules, updates = parse_input()["rules"], parse_input()["updates"]

    for update in updates:
        print(update)



if __name__ == "__main__":
    print(f"Day 5 Part 1 Answer: {part1()}")