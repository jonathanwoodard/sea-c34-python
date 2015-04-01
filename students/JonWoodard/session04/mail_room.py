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
d = {}
# donors
ls1 = ['Felix Hernandez', 'Hisashi Iwakuma', 'Taijuan Walker', 'Mike Zunino', 'Robinson Cano', 'Brad Miller', 'Kyle Seager']
ls2 = [1700, 900, 1600, 150, 1100, 250, 750] # amounts
d = dict(zip(ls1, ls2))
keys = d.keys
values = d.values


def safe_input():

    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    """

    raw_input('% ->')
    try:
        return (raw_input())
    except:
        EOFError or KeyboardInterrupt
        return 'None'


def thank_you():
    """
    This function will take user input and create a thank you email
    """
    safe_input(u'Enter the Full Name of the Donor: ->')
    if raw_input in d[keys]:
        donation_amount()
    else:
        d.update[keys]
        donation_amount()



def donation_amount():
    """
    This function will take user input for donation amount and add it to d
    """
    safe_input(u'Please enter the donation amount: ->')


def number_input():
    """
    This function will determine whether the value entered is a number
    If the value is a number, an email will be generated
    Otherwise it will return the user to the donation_amount function
    """
    if donation_amount.raw_input() is float:
        email_text()
    else:
        donation_amount()



def email_text():
    """
    This function will take the user entered name and donation amount
    to generate a thank you email.

    """
    print(u"Dear %, The Royal Society for Putting Things on top of Other Things")
    print(u"would like to sincerely thank you for your generous donation of %.")
    print(u"This kind donation will enable us to put many more Things on top of ")
    print(u"Other Things in the coming year.")


def report():
    """
    This function will generate a report of donors and donations.
    The report will contain 'name', total of all donations, number
    of donations, and the average donation value.
    The report will be sorted by the donation total, and formatted so 
    that the values are neatly alligned in rows.
    """

    for key in d:
        tot = sum(d[values])
        n = len(d[values])
        average = tot / n
        report_entry = [d[key], tot, n, average]
        print(report_entry.sort(2))
        
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
