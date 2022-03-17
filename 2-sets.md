# Sets
## Introduction
In this module, we will have the opportunity to learn about sets.  We will go over what sets exactly are, how efficent they are, and show example of how it looks in the Python programming language.  At the end of this section, we will have an example problem of how to add/remove from sets and reinforce key concepts that are unique to sets.

##  What are Sets

The set data structure is a tool that every programmer should be familiar with.  Sets are special becuase you are not allowed to have any duplicate vaules in the set.  Only unique values will show up in the set.  Unlike lists, the order of the set does not matter and can be in any order.

Another feature of sets that we should mention is how you can have different kinds of values in the set.  So in one set you can have strings, integers, booleans, etc.

Example 1:

``` python

set1 = {'String', 1, True, [1,2,3]}

```

## How to impliment sets

So what do sets look like?  Well, a set in Python can be implimented in two different ways.  The first way is the built in set() function.  It looks like this in code:

Example 2:

``` python

set2 = set(('apple','orange','grape'))

```

This built in function will allow a list of values to be put into a set and changed into an object.  

Now what if we do not want to use the function?  Well, we can simply just declare a set like we do a python list.  Notice how we will simply use curly braces to make a set.   Lets look at how this looks in code:

Example 3:
``` python

set3 = {1,2,3,4}

```


##  How to Manipulate Sets and Efficeny of Sets
Sets can sometimes be interesting to manipulate.  For example, you cannot replace a specifc value directly in a set like you could a list.  Instead, you would have to remove the specific item, then add it in.  So lets take a look at how to manipluate sets in different ways in the table below:

Set Operation   |   Code Syntax      | Effincency
----------------|--------------------|-----------
add( )          | set1.add(value)    | O(1)
remove( )       | set1.remove(value) | O(1)
size( )         | len(set1)          | O(1)
member( )       | if value in set1:  | O(1)


You can also use the union() and intersection() functions in python on sets.  The union() funciton will simply join two sets together.  The intersection() function will make a new set showing the values that are found in both sets.  Examples of these and more will be given below.



###  Example: add to a set, remove, no duplicates
Now lets take a look at an example problem that use what we talked about from up above.  We will take two sets of numbers and manipulate them in the different ways we discussed.  The code down below show each of the differet ways we can manipulate a set.  Feel free to copy and paste the code to see it run in real time.

```python
def main():

    #Notice set1 and set2 have the 4 and the 5 in common right now.
    set1 = {'Bill', 'Lucy', 'Keith', 'Mike'}
    set2 = {'Bob', 'Bill', 'Zach', 'Chris', 'Lucy'}


    #Code Example 1: Add to a set
    set1.add('Alyssa')
    print(f'\nAdding Alyssa to set: {set1}\n') 
    #Result: {'Lucy', 'Keith', 'Alyssa', 'Mike','Bill'}



    #Code Example 2: Remove from a set
    set1.remove('Keith')
    print(f'Removing Keith from set: {set1}\n') 
    #Result will be {'Lucy', 'Alyssa', 'Mike', 'Bill'}



    #Code Example 3: Combining two sets with a union.
    set3 = set1.union(set1, set2)
    print(f'Joing two sets together: {set3}\n') 
    #Result will be {'Lucy', 'Bob', 'Zach', 'Alyssa', 'Mike', 'Bill', 'Chris'}



    #Example 4: Seeing the same values in both sets using intersection.
    set4 = set1.intersection(set2)
    print(f'See which values are in both sets: {set4}\n') #Result will be {'Bill', 'Lucy'}



    #Example 5: Putting values of one set into another set.  Note that the unique values were automatically taken out.
    set1.update(set2)
    print(f'Putting one set into another: {set1}\n') 
    #Result will be {'Lucy', 'Bob', 'Zach', 'Alyssa', 'Mike', 'Bill', 'Chris'}


main()
 ```

##  Practice Problem: Verify Email

Now its time for you to try out sets!  First, download this [sets_problem](stack_problem.py) file.  When you open the file, notice two functions you have to code.  

### Problem 1:
The first function you will write is email_in_set.  Your goal is to check the set to see if a given email is in the set.  If it is in the set, simply let the user know the email is there.  If the email is not in the set, add the email and return the set.  Assume the email is valid.

### Problem 2:
The second problem you will have to face is writing the remove_emails() function.  First you will have to check if emails ending with @yahoo.com are in the set.  Then you will have to remove all the emails that you find that end with @yahoo.com.  Possible Hints: Make a second set to help keep track of emails that need to be removed.  Also, feel free to use the find() function to check substrings.  

When you are finished, feel free to compare your solution with my own solution.  Please do not look at the solution unless your really stuck or are finished.  

   [Set Problem Solution](stack_problem_solution.py)

[Back to Welcome Page](0-welcome.md)