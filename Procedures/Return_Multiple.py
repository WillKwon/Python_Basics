def min_list(list):
    min_so_far = list[0]
    for elements in list:
        if min_so_far > elements:
            min_so_far = elements
    return min_so_far

def max_list(list):
    max_so_far = list[0]
    for elements in list:
        if max_so_far < elements:
            max_so_far = elements
    return max_so_far

def max_min_list(list):
    MIN = min_list(list)
    MAX = max_list(list)
    return (MAX, MIN) # Use tuples (pair in this case)


mylist = [3,4,5,2,99,1,4,5,6]
(maximum, minimum) = max_min_list(mylist) # save using tuples
print maximum
print maximum, minimum # Can print more than one
