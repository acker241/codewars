def remove_smallest(numbers):
    if numbers == []:
        return([])
    elif numbers.count(min(numbers)) == 1:
        numbers.remove(min(numbers))
        return (numbers)
    else:
        numbers.remove(numbers[numbers.index(min(numbers))])
        return(numbers)



print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([1, 2, 3, 1, 1]))