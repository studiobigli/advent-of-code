def part1():
    grid = {"rows": {},
            "columns": {},
            "diagonal_tl_to_br": {},
            "diagonal_bl_to_tr": {},
            "total_rows": 0,
            "total_columns": 0}
    
    count = 0
    
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
                # print(f"X:{check_pos_x}, Y:{check_pos_y}, Letter: {grid["rows"][check_pos_x][check_pos_y]}")
                diagonal_line.append(grid["rows"][check_pos_x][check_pos_y])
                check_pos_x += 1
                check_pos_y += 1
        grid["diagonal_tl_to_br"][x] = "".join(diagonal_line)

    #Store diagonals from bottomleft to topright in dictionary
    for x in range(grid["total_rows"]-1, -1, -1):
        check_pos_x, check_pos_y, reverse_correction = x, 0, 139-x
        diagonal_line = []
        for y in range(grid["total_rows"]-reverse_correction ):
            if (check_pos_x >= 0) and (check_pos_y <= grid["total_columns"]-1-reverse_correction):
                # print(f"X:{check_pos_x}, Y:{check_pos_y}, Letter: {grid["rows"][check_pos_x][check_pos_y]}")
                diagonal_line.append(grid["rows"][check_pos_x][check_pos_y])
                check_pos_x -= 1
                check_pos_y += 1
                reverse_correction -= 1
        grid["diagonal_bl_to_tr"][x] = "".join(diagonal_line)

    # Join column keypair lists into strings
    for key, _ in grid["columns"].items():
        grid["columns"][key] = "".join(grid["columns"][key])

    #Iterate through all strings looking for XMAS entries, forwards and backwards

    for dict_key in ["rows", "columns", "diagonal_tl_to_br", "diagonal_bl_to_tr"]:
        for _,line in grid[dict_key].items(): 
            count += check_line(line)

        for _,line in grid[dict_key].items(): 
            count += check_line(line[::-1])

    return count

def check_line(line):
    xmas_count = 0
    if len(line) < 4:
        return 0
    while line:
        if line.partition("XMAS")[1] == "XMAS":
            xmas_count += 1
            line = line.partition("XMAS")[2]
        else:
            break
    return xmas_count

if __name__ == "__main__":

    print(f"Answer for Day 4 Part 1: {part1()}")