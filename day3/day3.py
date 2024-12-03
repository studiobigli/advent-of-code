def do_or_dont():
    dey_do_doh_dont_dey_doh: bool = True
    fine_text_list: list = []
    
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
    source_text: list = fine_text.split("mul(")
    return multiply(source_text)

def multiply(source_text):
    multiply_list: list = []

    for bad_string in source_text:
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
    with open('day3/day3.txt', 'r') as f:
        text_input = f.read().split("mul(")
        print(f"Day 3 Part 1 answer: {multiply(text_input)}")

    print(f"Day 3 Part 2 answer: {do_or_dont()}")