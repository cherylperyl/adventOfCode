"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=3 ; task=1)
"""

import sys


def main():
    corrupted_mem = ""
    for line in sys.stdin:
        corrupted_mem += line.strip("\n")
    result = 0
    valid_format = "mul(x,x)" # where x means a 1-3 digit num  
    num1 = ""
    num2 = ""
    is_num = False
    valid_mul = ""

    
    for ch in corrupted_mem:
        if (len(valid_mul) == len(valid_format)) and( len(num1) <= 3) and (len(num2) <= 3):
            print(valid_format, num1, num2)
            result += int(num1) * int(num2)
            num1, num2, valid_mul = "", "", ""

        # collecting the num
        if ch.isdigit():
            if len(valid_mul) == 4:
                if not is_num:
                    is_num = True
                num1 += ch
            elif len(valid_mul) == 6:
                if not is_num:
                    is_num = True
                num2 += ch
            continue
        elif is_num and not ch.isdigit():
            valid_mul += "x"
            is_num = False
    
        # checking the rest of the valid format aside from the nums
        if ch != valid_format[len(valid_mul)]:
            num1, num2, valid_mul = "", "", ""
    
        if ch == valid_format[len(valid_mul)]:
            valid_mul += ch
    
    print(result)

if __name__ == "__main__":
    main()