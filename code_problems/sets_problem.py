import re

def main():
    """This function will control the main email list.  It will perform the function calls for you. """

    email_set = {'kevin234@gmail.com', 'chris123@yahoo.com', 'sarah4567@gmail.com','downmich03@gmail.com', 'tate@icloud.com','sierradowns@yahoo.com'}
    #TEST CASES

    #------------------------PROBLEM 1 TEST CASES---------------------------

    #Test Case 1: Not in set
    email_set = email_in_set(email_set, 'notinset@gmail.com')
    print(f'notinset@gmail.com is not in the set so it is added in: {email_set}\n')
    #Results:{'kevin234@gmail.com', 'chris123@yahoo.com', 'sarah4567@gmail.com','downmich03@gmail.com', 
    # 'tate@icloud.com','sierradowns@yahoo.com'}

    #Test Case 2: Email is in set already. Set does not change
    email_set = email_in_set(email_set, 'kevin234@gmail.com')
    print(email_set)
    #Results: {'sierradowns@yahoo.com', 'chris123@yahoo.com', 'tate@icloud.com', 
    # 'sarah4567@gmail.com', 'notinset@gmail.com', 'downmich03@gmail.com', 'kevin234@gmail.com'}


    #-------------------------PROBLEM 2 TEST CASES --------------------------------------

    #Test Case 1: Nothing to remove
    test_set_1 = {'kevin234@gmail.com', 'sarah4567@gmail.com'}
    remove_emails(test_set_1) #Results Should be {'kevin234@gmail.com', 'sarah4567@gmail.com'}

    #Test Case 2: remove all of the Yahoo Emails
    test_set_2 = {'sierradowns@yahoo.com','kevin234@gmail.com', 'sarah4567@gmail.com','chris123@yahoo.com'}
    remove_emails(test_set_2) #Results Should be {'kevin234@gmail.com', 'sarah4567@gmail.com'}

#-------------------------------------------------------------------------------------------

def email_in_set(email_set, email):
    '''This function you will write will determine if the set with all the emails has the entered email.  
    If it does, simply let the user know and make sure the set is returned unaltered.  If it does not have the email, 
 add it to the set return the new set '''

    #PROBLEM 1: ENTER YOUR CODE BELOW
    pass


def remove_emails(email_set):
    """In this problem, we will want to remove certain types of emails.  For example, if
    we wanted to get rid of all the emails that end with @gmail.com, we would find them in the set and remove them.
    Hints for this problem: Use another empty set to help keep track of the emails you want to remove from the orginal set.  Also, 
    feel free to use the find() function in python to check each email in the set. 
    Your goal in this problem is to remove all the emails that end with  @yahoo.com"""

    #PROBLEM 2: ENTER YOUR CODE BELOW
    pass


main()
