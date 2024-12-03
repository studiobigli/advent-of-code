def do_or_dont():
    dey_do_doh_dont_dey_doh: bool = True
    fine_text_list: list = []
    multiply_list: list = []

    with open('day3/day3.txt', 'r') as f:
        text_input = f.read()
    
    while text_input:
        if dey_do_doh_dont_dey_doh:
            fine_text_list.append(text_input.partition("don't()")[0])
            text_input = text_input.partition("don't()")[2]
            dey_do_doh_dont_dey_doh = False

        elif not dey_do_doh_dont_dey_doh:
            text_input = text_input.partition("do()")[2]
            dey_do_doh_dont_dey_doh = True

        else:
            break
    
    fine_text: str = "".join(fine_text_list)
    split_by_mul: list = fine_text.split("mul(")

    for bad_string in split_by_mul:
        new_number: int = 0
        
        if "," in bad_string[1:4]:
            second_bad_string: list = bad_string.split(")")
            third_bad_string = second_bad_string[0].partition(",")
            
            try:
                new_number = int(third_bad_string[0])*int(third_bad_string[2])
            except:
                continue
            finally:
                multiply_list.append(new_number)

    return sum(multiply_list)

if __name__ == "__main__":
    print(do_or_dont())