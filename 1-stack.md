# Stacks
## Introduction
In this section we will be learning about the programming data structure that is called the Stack.  Stacks are a common programming sturcture that all programmer should know.  As you continue reading on, this module will explain what stacks are, how to use them, what there efficency is, and give a problem for you to solve using a stack.

##  What are Stacks?
Stacks is a data structure that follows a particular order.  For example, if you were to put two items on the stack, you cannot get to the first itm unless the second is remove.  Stacks often follow the acronm FIFO (First in Frist Out) or LIFO (Last in First Out).  To help visulize this, look at a picture of stacks pancakes below:

![Pancake Picture](images/pancakes.jpg)

Notice how each pancake is on top of one another.  To reach the bottom pancake, you must remove all the other ones on top in order to get to it!  With stacks in programming it is no different except with the fact pancakes are a little more tasty!

### Why are Stacks important?

Stacks are important for a few reasons.  Since order is important, we can use it to save previous versions of a file.  Many software have a undo or redo button these days.  For example, Microsoft Word uses a stack that allows you to see previous versions of your document. I assume a lot of people can agree that a feature like this has come in handy!

Another example of where stacks could be used is on web browsers.  If you want to go back to a previous page you were on, you can simply hit the back arrow and go back to where you were.  Stacks are nice in this case because we can simply remove the current page we are on to get back to where we were.

So why are stacks important?  Well if order and data storage is important, stacks could be the right tool for the job!




## How to impliment stacks
Now that we know what stacks are, what do they look like in python code?  It looks pretty simple actually.  To make a stack, simply use a list:

```python
    stack = []
 ```

 Now we must ask the question, what can we store in a stack?  Really, any kind of value you want, but in reality we probably will simply have the same kind of types in real world problems.


##  How to Manipulate Stacks and Efficeny of Stacks
Stacks are pretty simply and easy to use.  As we start using a stack, make sure to remember that stacks follow the FIFO (First in Frist Out) or LIFO (Last in First Out) rules.  If we are dealing with versions of a program or have a waiting list for heart transplants, we do not want the order messed up!

Set Operation   |Description                     |  Code Syntax      | Effincency
----------------|--------------------------------|-------------------|-----------
push( )         |Adds value on top of stack      |stack.append(value)| O(1)
pop( )          |Removes value from top of stack |stack.remove(value)| O(1)
size( )         |Shows size of stack             | len(stack)        | O(1)
empty ( )       |If the length of the stack is 0.| if len(stack) ==0:| O(1)


###  Example: Version Control

Now that we have seen a glimpse of the different commands to manipluate a stack, let us take a look at how each command works in code!  In the code examples below, we will have a simple stack with a bunch or strings.  

### Removing from a Stack:
To remove from a stack we will use the pop() method that is built into python.  In the code block below we have a simple block of code with a stack caled 'version_stack'.  Inside the stack we put in strings to represent different 'versions' of a file.  We then have input from the user say which version he wants back.  Now we could make a full blown working code, but with the code down below we wanted to make sure it was easy to see how removing from a stack works.  To see the code run in real time, feel free to copy and paste it in a code editor of your choice.

``` python
    def main():

        version_stack = ['Version 1', 'Version 2', 'Version 3', 'Version 4', 'Version 5']

        #Example 1: Shows how to remove something from a stack.
        user_input = int(input(f'Which version of the file would you like?: Enter a number between 1 and {len(version_stack)}: '))

        #This loop removes the different 'versions' from th estack until the desired version is found.  
        # We then display it to the user accessing the last element of the stack.
        for i in range(user_input, len(version_stack)):
            version_stack.pop()
        
        
        print(f'File: {version_stack[-1]}.') #Result should be something like "File: Version 3" if you put in 3.
        #Note that we did not access the item in the stack directly.  We had to remove th eother versions to get to th eone we wanted.

        print(version_stack) #See the finished Stack

    main()
```

### Adding a Stack:
To add to a stack, we can use the append() funtion built into python.  If you notce the funtion below, we are asking the user if he wants his 'version' of a file saved.  If the user wants to, we will append the fil to the end of the stack.  For teaching purposes, we will also use the size of the stack to help label the version file.

 Now we could make a full blown working code, but with the code down below we wanted to make sure it was easy to see how removing from a stack works.  To see the code run in real time, feel free to copy and paste it in a code editor of your choice.

``` python
    def main():

        version_stack = ['Version 1', 'Version 2', 'Version 3', 'Version 4', 'Version 5']

        #EXAMPLE 2: Shows how easy it is to add something onto a stack.
        #This example will show us how we can simply add to the stack:
        user_input = input('Would you like to save your file?: Y/N?: ')

        if user_input.lower() == 'y':

            #We need to figure out which number the version will be labeled so we will use the size of the stack.
            version_count = len(version_stack)

            version_stack.append(f'Version {version_count +1}')

            print(version_stack) #See the finished Stack
        else:
            print('No file added to stack.')
    main()
```




##  Practice Problems: 

Now it is time for you to try using stacks for yourself!  First, download the [Stack Problem](stack_problem.py) file. Next, follow the intructions down below to solve each problem.

### Problem 1:
You will be coding the reverse_string() function for this problem.  If you look at the function parameters, you have an empty stack and a string passed in.  Your job is to add each letter of the string to the stack.  For example, 'Hello world' will be [d,l,r,o,w, , o,l,l,e,H].  
You are allowed to use the reversed function if you wish. Make sure to use the append() method to add to the stack.  
Make sure to return the stack at the end of the funciton.

### Problem 2:
You will be coding the print_string_from_stack() function for this problem.  If you look at the function parameters, you have an empty stack passed in.  Your job is to take each letter from the stack and make it into a readable string again. For this problem, 
    you are NOT allowed to use the reversed function.

When you are finished with the code or get stuck, please review the solution code:  [Stack Problem Solution](stack_problem_solution.py)


[Back to Welcome Page](0-welcome.md)