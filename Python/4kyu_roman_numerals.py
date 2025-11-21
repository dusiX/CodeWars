# Write two functions that convert a roman numeral to and from an integer value.

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'),  (90, 'XC'),  (50, 'L'), (40, 'XL'),
            (10, 'X'),   (9, 'IX'),   (5, 'V'),  (4, 'IV'), (1, 'I')
        ]
        res = ''
        for number, numeral in numerals:
            count = val // number
            res += numeral * count
            val -= number * count
        return res

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return roman_num.count("M")*1000 + roman_num.count("D")*500 + roman_num.count("C")*100 + roman_num.count("L")*50 + roman_num.count("X")*10 + roman_num.count("V")*5 + roman_num.count("I")*1 - roman_num.count("CD")*200 - roman_num.count("CM")*200 - roman_num.count("XL")*20 - roman_num.count("XC")*20 - roman_num.count("IV")*2 - roman_num.count("IX")*2
