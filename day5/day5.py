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
    count = int()

    for update in updates:
        add_middle_page = True

        update_breakdown = {x: y for x,y in enumerate(update)}
        for num in update_breakdown.values():
            for rule in rules:
                if num in rule and add_middle_page:
                    if rule[0] in update_breakdown.values() and rule[1] in update_breakdown.values():
                        if update.index(rule[0]) > update.index(rule[1]):
                            add_middle_page = False

        if add_middle_page:
            count += int(update[int((len(update) -1)/2)])

    return count
                            
                    
                
                    



if __name__ == "__main__":
    print(f"Day 5 Part 1 Answer: {part1()}")