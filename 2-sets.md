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

###UNION< INETERSECTION>



##  Example: add to a set, remove, no duplicates


##  Practice Problem: Verify Email


[Back to Welcome Page](0-welcome.md)