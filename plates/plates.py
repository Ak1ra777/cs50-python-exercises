def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    check0 = True
    check_digit = True
    for l in s:
        if l.isdigit() or l.isalpha():
            if l.isdigit() and check0 == True and l == '0':
                return False
            elif l.isdigit():
                check0 = False
                check_digit = False
            elif l.isalpha() and check_digit == False:
                return False
        else:
            return False
    else:
        return True

main()
