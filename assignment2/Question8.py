def calculate_sum(s):
    sum=0
    for i in s:
        sum+=(ord(i)-ord('0'))
    return sum

print(calculate_sum("2514"))