# Given an array of integers, write a method to total the odd numbers.
def Odd_Total(array):
    total = 0
    for num in array:
        if num%2 != 0:
            total += num
    print(total)


'''Given an array of integers, write a method to sum the elements in the array,
    knowing that some of the elements may be very large integers.'''
# The size of the number is not a specific concern in python like it is in C#
def Array_Total(array):
    total = 0
    for num in array:
        total += num
    print(total)

# Given a string, reverse it
def Reverse_String(string):
    rev_str = string[::-1]
    print(rev_str)

# Given a string, remove any repeated letters
def Remove_Repeated(string):
    new_string = ''
    for letter in string:
        if letter not in new_string:
            new_string += letter
    print(new_string)

# FizzBuzz
def FizzBuzz():
    for num in range(1,101):
        if num%3 == 0 == num%5:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')




if __name__ == '__main__':
    array = [1,2,3,4,5]
    string = 'Hello World!'
    Odd_Total(array)
    Array_Total(array)
    Reverse_String(string)
    Remove_Repeated(string)
    FizzBuzz()
