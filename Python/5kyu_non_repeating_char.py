# Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("");

# † Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

def first_non_repeating_letter(s):
    digit = 0
    storage = []
    for digit in range(len(s)):
        if s.upper().find(s[digit], digit + 1) == -1 and s.lower().find(s[digit], digit + 1) == -1 and s[digit] not in storage:
            print(s[digit])
            return s[digit]
        else:
            storage.append(s[digit])
    
    return ''
