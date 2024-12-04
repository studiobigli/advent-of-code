def part1():
    grid = {"rows": {},
            "columns": {},
            "diagonal_l_to_r": {},
            "diagonal_r_to_l": {},
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

        #Store diagonals from left to right in dictionary
        for x in range(grid["total_rows"]):
            check_pos_x, check_pos_y = x, 0
            for y in range(grid["total_rows"]-x ):
                if (check_pos_x <= grid["total_rows"]-1) and (check_pos_y <= grid["total_columns"]-1-x):
                    print(check_pos_x, check_pos_y, grid["rows"][check_pos_x][check_pos_y])
                    check_pos_x += 1
                    check_pos_y += 1

    # print(grid)



if __name__ == "__main__":
    print(f"Answer for Day 4 Part 1: {part1()}")