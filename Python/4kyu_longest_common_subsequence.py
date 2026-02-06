def lcs(x, y):
    if len(y) == 0 or len(x) == 0:
        return ""

    new_str = []
    j = 0
    
    for char in y:
        if x.find(char, j) != -1:
            new_str.append(char)
            j = x.find(char, j) + 1
    
    return "".join(new_str)

print(lcs("nothardlythefinaltest", "zzzfinallyzzz"))