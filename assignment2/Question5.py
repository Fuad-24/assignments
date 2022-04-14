def sum_list(list):
    sum=list[0]
    for i in range(1,len(list)):
        sum+=list[i]
    return sum
print(sum_list([1,2,3,4,5]))