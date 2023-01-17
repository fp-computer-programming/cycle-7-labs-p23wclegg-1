def num_sorting(num1,num2,num3):
    # Made the List of numbers into a function
    numbers = [num1,num2,num3]
    #sorting the list from the lowest to highest number
    numbers.sort()
    return("The lowest number is "+str(numbers[0])+", The highest number is "+str(numbers[len(numbers)-1]))

    #TEST CASES 6-5
print (num_sorting(10,15,20))
print(num_sorting(-10,-20,15))
print (num_sorting(0, 10, 15))
print(num_sorting(.25,3,10))
#Each test should print the numbers in order from highest to lowest and return the highest and lowest


def word_sorting(input_1,input_2,input_3,input_4,input_5):
    words = [input_1,input_2,input_3,input_4,input_5]
    word_lengths = [input_1,input_2,input_3,input_4,input_5]
    return(words, word_lengths)

    #TEST CASES 6-6
print(word_sorting('key', 'board', 'and', 'mouse', 'computer'))
print (word_sorting('verylongword', 'word', 'words', 'shortword','medium word'))
print(word_sorting('first', 'second', 'last', 'third','fourth'))
print (word_sorting('hello', 'goodbye', 'hi', 'bye','greetings'))
#Each test should print the words in order of their length and say which words are the longest and shortest


def input_doubles(input1,input2,input3):
    nums = [int(input1)*2,int(input2)*2,int(input3)*2]
    return(nums)
    #TEST CASES 6-7

print (input_doubles(10,15,20))
print(input_doubles(-10,-20,15))
print (input_doubles(0, 10, 15))
print(input_doubles(.25,3,10))
#Each value in the tests should double 


def even_odd(input1, input2, input3):
#user list of inputs and the list of them

    if input1 %2 == 0 and input2 %2 == 0 and input3 %2 == 0:
        print("Even")
    elif input1 %2 != 0 and input2 %2 != 0 and input3 %2 != 0:
        print('Odd')
    else: print('Mixed')
#making conditional statements on whether the numbers are 
#even, odd, or mixed by dividing the integers

    #TEST CASES 6-8
print (even_odd(10,15,20))
print(even_odd(-10,-20,15))
print (even_odd(0, 10, 15))
print(even_odd(.25,3,10))
#Each test should print whether the numbers are odd or even 