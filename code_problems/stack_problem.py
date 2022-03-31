def reverse_string(string, stack):

    """This function is meant to take a string and reverse it with the help of a stack.  
    You are allowed to use the reversed function if you wish. Make sure to use the append() method to add to the stack.  
    Make sure to return the stack at the end of the funciton.   """
    #CODE PROBLEM 1 HERE
    pass

def print_string_from_stack(stack):
    """For this function, you will convert a stack with a reversed string into a simple string.  FOr this problem, 
    you are NOT allowed to use the reversed function.   """
    
    #CODE PROBLEM 2 HERE
    pass




#------------PROBLEM 1 TEST CASES-----------------

stack = []
string = 'I Love Cows a ton!'

result = reverse_string(string, stack)
print(result) #['!', 'n', 'o', 't', ' ', 'a', ' ', 's', 'w', 'o', 'C', ' ', 'e', 'v', 'o', 'L', ' ', 'I']
print()

stack2 =[]
string =''
result = reverse_string(string, stack2)
print(result) #[]
print()

stack3 =[]
string = 'Ma'
result = reverse_string(string, stack3)
print(result) #['a', 'M']
print()

#------------PROBLEM 2 TEST CASES-----------------

stack1 = ['!', 'n', 'o', 't', ' ', 'a', ' ', 's', 'w', 'o', 'C', ' ', 'e', 'v', 'o', 'L', ' ', 'I']
value = print_string_from_stack(stack1)
print(value) #Result: I Love Cows a ton!

stack2=['a','M']
value = print_string_from_stack(stack2)
print(value) #Ma

stack3 = []
value = print_string_from_stack(stack3)
print(value) #''