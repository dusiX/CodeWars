# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

def next_bigger(n):
    strn = str(n)
    if len(strn) == 1:
        return -1
    elif len(strn) == 2:
        return int(strn[::-1]) if int(strn[::-1])>n else -1
    else:
        chartab = []
        for i in range(len(strn)):
            chartab.append(int(strn[i]))
        
        for i in range(len(strn)-1,0,-1):
            if chartab[i-1] < chartab[i]:
                chartab.insert(i-1, int(strn[i]))
                del chartab[i+1]
                newn = int(''.join(str(chartab[i]) for i in range(len(chartab))))
                if newn > n:
                    return newn
            else:
                continue
        
    return -1

print(next_bigger(144))