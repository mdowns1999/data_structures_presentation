
""" Example of how sets will not allow duplicates. """
list1 = [1,2,3,4,5,5]
set1 = {2,1,4,3,5,5}

print(list1)#Output: [1, 2, 3, 4, 5, 5]
print(set1) #Output: {1,2,3,4,5}

"""Examples of how to add or remove to set"""

set2 =set(('apple','banana','strawberry'))


print(set2) # Output:{'strawberry', 'banana', 'apple'}

set2.add('Orange')

print(set2) # Output:{'strawberry', 'banana', 'apple','Orange'}

set2.remove('apple')

print(set2) # Output:{'strawberry', 'banana','Orange'}

