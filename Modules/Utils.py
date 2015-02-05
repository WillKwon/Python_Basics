'''
Created on 2015. 2. 5.

@author: Will.Kwon
'''

def squares(limit):
    answer = []
    for n in range(limit):
        answer.append(n**2)
    return answer

def total(numbers):
    sum_so_far = 0
    for number in numbers:
        sum_so_far += number
    return sum_so_far