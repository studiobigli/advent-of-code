def build_grid():
    grid = {"rows": {},
            "columns": {},
            "diagonal_tlbr_x": {},
            "diagonal_bltr_x": {},
            "diagonal_tlbr_y": {},
            "diagonal_bltr_y": {},
            "total_rows": 0,
            "total_columns": 0}
    
    with open (r'day4/day4.txt', 'r') as f:
        
        #Get dimensions of grid
        grid["total_rows"] = len(f.readlines())
        f.seek(0)
        grid["total_columns"] = len(f.readline())-1
        f.seek(0)

        #Form columns in dictionary
        for x in range(grid["total_columns"]):
            grid["columns"][x] = []
        
        for x in range(grid["total_rows"]):
            grid["rows"][x] = []

        #Store rows in dictionary
        for row_pos, row in enumerate([row.rstrip('\n') for row in f]):
            grid["rows"][row_pos] = row
        f.seek(0)

    #Store columns in dictionary
    for x in range(grid["total_columns"]):
        for row_pos, row in grid["rows"].items():
            grid["columns"][x].append(row[x])

    #Store diagonals from topleft to bottomright in dictionary
    for x in range(grid["total_rows"]):
        check_pos_x, check_pos_y = x, 0
        diagonal_line = []
        for y in range(grid["total_rows"]-x ):
            if (check_pos_x <= grid["total_rows"]-1) and (check_pos_y <= grid["total_columns"]-1-x):
                diagonal_line.append(grid["rows"][check_pos_x][check_pos_y])
                check_pos_x += 1
                check_pos_y += 1
        grid["diagonal_tlbr_x"][x] = "".join(diagonal_line)
    
    for y in range(grid["total_rows"]):
        check_pos_x, check_pos_y = 0, y
        diagonal_line = []
        for x in range(grid["total_rows"]-y ):
            if (check_pos_x <= grid["total_rows"]-1) and (check_pos_y <= grid["total_columns"]-1):
                diagonal_line.append(grid["rows"][check_pos_x][check_pos_y])
                check_pos_x += 1
                check_pos_y += 1
        grid["diagonal_tlbr_y"][y] = "".join(diagonal_line)
    del grid["diagonal_tlbr_y"][0]

    #Store diagonals from bottomleft to topright in dictionary
    for x in range(grid["total_rows"]-1, -1, -1):
        check_pos_x, check_pos_y, reverse_correction = x, 0, 139-x
        diagonal_line = []
        for y in range(grid["total_rows"]-reverse_correction ):
            if (check_pos_x >= 0) and (check_pos_y <= grid["total_columns"]-1-reverse_correction):
                diagonal_line.append(grid["rows"][check_pos_x][check_pos_y])
                check_pos_x -= 1
                check_pos_y += 1
                reverse_correction -= 1
        grid["diagonal_bltr_x"][x] = "".join(diagonal_line)

    for y in range(grid["total_rows"]):
        check_pos_x, check_pos_y = 139, y
        diagonal_line = []
        for x in range(grid["total_rows"] ):
            if (check_pos_x >= 0) and (check_pos_y <= grid["total_columns"]-1):
                diagonal_line.append(grid["rows"][check_pos_x][check_pos_y])
                check_pos_x -= 1
                check_pos_y += 1
                reverse_correction -= 1
        grid["diagonal_bltr_y"][y] = "".join(diagonal_line)
    del grid["diagonal_bltr_y"][0]

    for key, _ in grid["columns"].items():
        grid["columns"][key] = "".join(grid["columns"][key])

    return grid

def part1():
    count = 0
    grid = build_grid()
    for dict_key in ["rows", 
                     "columns", 
                     "diagonal_tlbr_x", 
                     "diagonal_bltr_x", 
                     "diagonal_tlbr_y", 
                     "diagonal_bltr_y"]:
        for _,line in grid[dict_key].items(): 
            count += check_line(line)

        for _,line in grid[dict_key].items(): 
            count += check_line(line[::-1])

    return count

def check_line(line):
    xmas_count = 0
    while line:
        if line.partition("XMAS")[1] == "XMAS":
            xmas_count += 1
            line = line.partition("XMAS")[2]
        else:
            break
    return xmas_count

def part2():
    count = 0
    grid = build_grid()

    for line_idx, line in grid["rows"].items():
        for ltr_idx, letter in enumerate(line):
            chk_letters = []
            if letter == "A":
                if ltr_idx-1 == int(-1): # Prevent grabbing letters from the end of the row
                    continue
                try:
                    if (grid["rows"][line_idx-1][ltr_idx-1] in "MS") and \
                        (grid["rows"][line_idx-1][ltr_idx+1] in "MS") and \
                        (grid["rows"][line_idx+1][ltr_idx-1] in "MS") and \
                        (grid["rows"][line_idx+1][ltr_idx+1] in "MS"):
                        chk_letters.append(grid["rows"][line_idx-1][ltr_idx-1]) # Add TL letter
                        chk_letters.append(grid["rows"][line_idx][ltr_idx])     # Add current letter
                        chk_letters.append(grid["rows"][line_idx+1][ltr_idx+1]) # Add BR letter

                        chk_letters.append(grid["rows"][line_idx+1][ltr_idx-1]) # Add BL letter
                        chk_letters.append(grid["rows"][line_idx][ltr_idx])     # Add current letter
                        chk_letters.append(grid["rows"][line_idx-1][ltr_idx+1]) # Add TR letter
                except:
                    continue

            if "".join(chk_letters) in ["SAMSAM", "MASMAS", "SAMMAS", "MASSAM"]:
                count += 1

    return count

if __name__ == "__main__":
    print(f"Answer for Day 4 Part 1: {part1()}")
    print(f"Answer for Day 4 Part 2: {part2()}")