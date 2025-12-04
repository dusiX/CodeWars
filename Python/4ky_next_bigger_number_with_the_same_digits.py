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
        prevnewn = 0
        chartab = [int(x) for x in strn]
        
        for i in range(len(strn)-1,0,-1):
            for j in range(i-1,-1,-1):
                chartab_copy = chartab[:]
                if chartab_copy[j] < chartab_copy[i]:
                    chartab_copy[j], chartab_copy[i] = chartab_copy[i], chartab_copy[j]
                    chartab_copy = chartab_copy[:j+1] + sorted(chartab_copy[j+1:])
                    newn = int(''.join(str(d) for d in chartab_copy))
                    if newn > n:
                        if prevnewn == 0 or newn < prevnewn:
                            prevnewn = newn

    return prevnewn if prevnewn > n else -1

print(next_bigger(144))