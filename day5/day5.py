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
    count, unordered_updates = int(), list()

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
        else:
            unordered_updates.append(update)
        
    return {"count": count, "unordered_updates": unordered_updates}
                            
def part2():
    rules, updates = parse_input()["rules"], part1()["unordered_updates"]
    count, checklist = int(), list()

    while updates:
        for update in updates:
            check_update = [x for x in update]
            append_triggered = False
            update_breakdown = {x: y for x,y in enumerate(update)}
            for num in update_breakdown.values():
                for rule in rules:
                    if num in rule:
                        if rule[0] in update_breakdown.values() and rule[1] in update_breakdown.values():
                            if update.index(rule[0]) > update.index(rule[1]):
                                update.append(update.pop(update.index(rule[1])))
                                append_triggered = True

            if append_triggered:
                break
            if check_update == update:
                checklist.append(updates.pop(updates.index(update)))
    
    for update in checklist:
        count += int(update[int((len(update) -1)/2)])

    return count

if __name__ == "__main__":
    print(f"Day 5 Part 1 Answer: {part1()["count"]}")
    print(f"Day 5 Part 2 Answer: {part2()}")