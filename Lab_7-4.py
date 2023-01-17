#Lab_7-4

def find_sum(num1, num2):
    '''Adds the two numbers together for the sum'''
    num_sum=num1 + num2
    return num_sum
#making a function to return the sum

my_sum=find_sum(111, 222)
print(my_sum)
#Running the program gives me the sum of the two numbers

#TEST CASES 
print (find_sum(10,15))
#Should equal 25
print (find_sum(-10, 15))
#Soudl equal 5
print (find_sum(.10, .15))
#Should equal .25
print (find_sum(10,-15))
#Should equal -5