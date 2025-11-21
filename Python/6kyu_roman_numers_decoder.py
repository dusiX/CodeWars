# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. 
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# Example:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CD"      ->  400
# "XC"      ->   90
# "XL"      ->   40
# "I"       ->    1

def solution(roman : str) -> int:
    
    count = 0
    digit = 0
    length = len(roman)
    tf = False
    
    for digit in range(length):
        if tf == False:
            match roman[digit]:
                case 'I':
                    if digit != length - 1:
                        if roman[digit + 1] == 'X':
                            count += 9
                            tf = True
                        elif roman[digit + 1] == 'V':
                            count += 4
                            tf = True
                        else:
                            count += 1
                    else:
                        count += 1
                case 'V':
                    count += 5
                case 'X':
                    if digit != length - 1:
                        if roman[digit + 1] == 'C':
                            count += 90
                            tf = True
                        elif roman[digit + 1] == 'L':
                            count += 40
                            tf = True
                        else:
                            count += 10
                    else:
                        count += 10
                case 'L':
                    count += 50
                case 'C':
                    if digit != length - 1:
                        if roman[digit + 1] == 'M':
                            count += 900
                            tf = True
                        elif roman[digit + 1] == 'D':
                            count += 400
                            tf = True
                        else:
                            count += 100
                    else:
                        count += 100
                case 'D':
                    count += 500
                case 'M':
                    count += 1000
        else:
            tf = False

    return count
