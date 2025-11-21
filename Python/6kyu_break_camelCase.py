# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    final = s
    for i in range(len(s)):
        if s[i].isupper():
            final = final[:i + (len(final)-len(s))] + " " + s[i:]
    return final
