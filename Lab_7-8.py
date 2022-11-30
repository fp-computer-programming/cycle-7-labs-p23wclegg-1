#Lab_7-8

def high(numbers):
    high_num= max(numbers)
    return high_num
#the first function that takes the highest number

def low(numbers):
    low_num= min(numbers)
    return low_num
#the second funtion that takes the lowest number 

def high_low_numbers(numbers):
    max_min=[high(numbers), low(numbers)]
    return max_min
#This function combines the other two functions 

#Test Cases
print(high_low_numbers([3, 1, 5, 6, 2, 7, 7, 10, 3]))
#List positive numbers
print(high_low_numbers([1,-1,4,-2]))
#List with positive and negative numbers
print(high_low_numbers([2, 4, 0,1]))
#List with positive numbers and a zero