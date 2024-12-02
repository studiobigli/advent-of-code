def iterate_through_file() -> int:
    safe_reports: int = 0
    with open ('day2/day2.txt', 'r') as f:
        for line in f:
            safe_reports += generate_reports([int(x) for x in line.split()])
    return safe_reports

def generate_reports(input_levels) -> int:
    safe_result: bool = False

    for x in range(len(input_levels)):
        check_levels: list = [y for y in input_levels]
        check_levels.pop(x)

        if check_safety(check_levels):
            safe_result = True
            break
        else:
            continue
 
    if safe_result:
        return 1
    else:
        return 0

def check_safety(levels) -> int:
    #Check adjacent levels differ by at least one and at most three:
    for i in range(len(levels)):
        if i == 0:
            continue

        level_check: tuple = int(levels[i]), int(levels[i-1])
        check_int: int = max(level_check) - min(level_check)

        if check_int > 3 or check_int < 1:
            return 0
    
    #Check all levels are either all increasing or all decreasing:
    while levels:
        if levels == sorted(levels):
            break
        elif levels == sorted(levels, reverse = True):
            break
        else:
            return 0
        
    return 1

if __name__ == "__main__":
    print(f"SAFE REPORTS: {iterate_through_file()}")