def calculate_average(numbers: list[int]) -> float:
    average=1
    sum1=0
    for number in numbers:
        sum1= sum1+number
    if len(numbers) != 0:
        average = sum1 / len(numbers)
        return average 
    else:
        average = average-1
        return average 
        
print(calculate_average([1, 2, 3, 4, 5]))


def remove_duplicates(l: list[int,str]) -> list:
    l_comparison=[]
    i=0
    i2=0
    new_l=[]
    for element in l:
        l_comparison.append(element)
    while i<len(l):
        if l[i] == l_comparison[i2]:
            if l[i]not in new_l:
                new_l.append(l[i])
            else:
                i2+=1
        else:
            i+=1
    return new_l
        

print(remove_duplicates([1, 2, 3, 1, 2, 4]))