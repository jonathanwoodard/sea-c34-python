#!/usr/bin/python
def mail_room(user_input):
    """
    This will define a series of actions to be taken in the mail room.
    Args:
        user_input:
            user selects form three options:
                "Send a Thank You"
                "Create a Report"
                "list"
    Return:
        "Send a Thank You" generates formated text email
        "Create a Report" generates a formated list
        "list" prints a list of names and returns to original prompt
    """
# create a dictionary, d = {}
# create a second dictionary, v = {} from d, with key/value pairs reversed
# populate dictionary with name, timestamp keys, amount values
# if raw_input == 'q'
#   call function(prompt)
# def prompt(raw_input)
#   prompt for user input:"Send a Thank You" or "Create a Report"
#   if raw_input == "Send a Thank You":
#       if (name, timestamp) in d:
#           prompt for user input "amount"
#           while user input is not a number:
#               re-prompt
#           if amount not in v:
#               add key/value pair to d
#           create thank you email
#           call function(prompt)
#   elif raw_input =="list":
#       print(list of keys in d)
#       call function(prompt)
#   elif raw_input == "Create a Report":
#       create a new_list = []
#       for key in d:
#           create tuple('name', total_donated, donation_count, donation_ave)
#           new_list.append(tuple)
#       new_list.sort(total_donated)
#       format items in tuples as stings containing a set # of char
#       print(new_list)
#       call function(prompt)
#   elif raw_input == "q":
#       call function(prompt)
#   else:
#       break
