def multiply():
    multiply_list: list = []
    
    with open('day3/day3.txt', 'r') as f:
        split_by_mul: list = f.read().split("mul(")


        for bad_string in split_by_mul:
            new_number: int = 0
            if "," in bad_string[1:4]:
                second_bad_string: list = bad_string.split(")")

                third_bad_string = second_bad_string[0].partition(",")
                
                try:
                    new_number = int(third_bad_string[0])*int(third_bad_string[2])
                except:
                    print("bad multi")
                finally:
                    print(f"{second_bad_string[0]=}, {third_bad_string=}, {new_number=}")
                    multiply_list.append(new_number)
    return sum(multiply_list)

if __name__ == "__main__":
    print(multiply())