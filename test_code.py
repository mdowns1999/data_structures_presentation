# import re

# def main():
#     """This function will control the main email list.  It will perform the function calls for you. """

#     #This loop will error check your input to make sure no invald formats enter the set.
#     valid = False
#     while not valid:
#         user_input = input('Enter an email address: ')

#         if is_valid_email(user_input):
#             valid = True
#         else:
#             print(f'Error.  Invalid format enter an email like example@gmail.com. You entered {user_input}')
#             valid = False

#     email_set = {'kevin234@gmail.com', 'chris123@yahoo.com', 'sarah4567@gmail.com','downmich03@gmail.com', 'tate@icloud.com','sierradowns@yahoo.com'}
#     #TEST CASES

#     #------------------------PROBLEM 1 TEST CASES---------------------------

#     #Test Case 1: Not in set
#     email_set = email_in_set(email_set, 'notinset@gmail.com')
#     print(f'notinset@gmail.com is not in the set so it is added in: {email_set}\n')
#     #Results:{'kevin234@gmail.com', 'chris123@yahoo.com', 'sarah4567@gmail.com','downmich03@gmail.com', 
#     # 'tate@icloud.com','sierradowns@yahoo.com'}

#     #Test Case 2: Email is in set already. Set does not change
#     email_set = email_in_set(email_set, 'kevin234@gmail.com')
#     print(email_set)
#     #Results: {'sierradowns@yahoo.com', 'chris123@yahoo.com', 'tate@icloud.com', 
#     # 'sarah4567@gmail.com', 'notinset@gmail.com', 'downmich03@gmail.com', 'kevin234@gmail.com'}


#     #-------------------------

# def is_valid_email(email):
#     """This function will validate if the user_input matches the standard email format be using the re libray. """
#     email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#     if re.fullmatch(email_format, email):
#         return True
#     else:
#         return False

# def email_in_set(email_set, email):
#     '''This function you will write will determine if the set with all the emails has the entered email.  
#     If it does, simply let the user know and make sure the set is returned unaltered.  If it does not have the email, 
#  add it to the set return the new set '''

#     #PROBLEM 1: ENTER YOUR CODE BELOW
#     if email in email_set:
#         print('Email is in the set.')
#     else:
#         # user_input = input('Would you like the email in the list?: Yes or No?: '  )
#         # if user_input.lower() == 'yes' or user_input.lower() == 'y':
#             email_set.add(email)

#     #Return the new set to user
#     return email_set


# def remove_emails(email_set):
#     """In this problem, we will want to remove certain types of emails.  For example, if
#     we wanted to get rid of all the emails that end with @gmail.com, we would find them in the set and remove them.
#     Hints for this problem: Use another empty set to help keep track of the emails you want to remove from the orginal set.  Also, 
#     feel free to use the find() function in python to check each email in the set. 
#     Your goal in this problem is to remove all the emails that end with  @yahoo.com"""
#     remove_set = set()

#     for email_address in email_set:
#         if email_address.find('@yahoo') != -1:
#             remove_set.add(email_address)

#     for email in remove_set:
#         if email in email_set:
#             email_set.remove(email)
    
#     return email_set

# main()


def main():

    version_stack = ['Version 1', 'Version 2', 'Version 3', 'Version 4', 'Version 5']

    #Example 1: Shows how to remove something from a stack.
    user_input = int(input(f'Which version of the file would you like?: Enter a number between 1 and {len(version_stack)}: '))

    #This loop removes the different 'versions' from th estack until the desired version is found.  
    # We then display it to the user accessing the last eement of the stack.
    for i in range(user_input, len(version_stack)):
        version_stack.pop()
    
    print(f'File: {version_stack[-1]}.') #Result should be something like "File: Version 3" if you put in 3.



    #EXAMPLE 2: Shows how easy it is to add something onto a stack.
    #This example will show us how we can simply add to the stack:
    user_input = input('Would you like to save your file?: Y/N?: ')

    if user_input.lower() == 'y':

        #We need to figure out which number the version will be labeled.
        version_count = len(version_stack)

        version_stack.append(f'Version {version_count +1}')

        print(version_stack) #Result should add another 'Version' on the stack with the next number.

main()
