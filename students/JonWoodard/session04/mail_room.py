#!/usr/bin/python
# create a dictionary, d = {}
d = {}
# donors
ls1 = ['Felix Hernandez', 'Hisashi Iwakuma', 'Taijuan Walker',
       'Mike Zunino', 'Robinson Cano', 'Brad Miller', 'Kyle Seager']
# amounts
ls2 = [[1700], [900], [1600], [150], [1100], [250], [750]]
d = dict(zip(ls1, ls2))
donors = []
amounts = []
for key in d:
    donors.append(key)
    amounts.append(d[key])

# create a function to prompt user for data
def safe_input(prompt):

    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    """
    prompt = 'Prompt user for desired input'
    try:
        usr_in = raw_input(prompt)
    except:
        EOFError or KeyboardInterrupt
        return 'None'
    else:
        return usr_in


# create function to ask for donor name
def donor_name(name):
    """
    This function will take user input and create a thank you email
    """
    prompt = u'Enter the Full Name of the Donor: ->'
    name = safe_input(prompt)
    if name in d:
        donation_amount(name)
    else:
        d.update(name, ([]))


def donation_amount(name):
    """
    This function will determine whether the value entered is a number
    If the value is a number, an email will be generated
    Otherwise it will return the user to the donation_amount function
    """
    prompt = u'Please enter the donation amount: ->'
    amount = safe_input(prompt)
    if amount is float:
        if amount in d[name]:
            email_text()
    else:
        print('That does not appear to be a valid number. Try again')
        donation_amount()


def email_text(amount, name):
    """
    This function will take the user entered name and donation amount
    to generate a thank you email.

    """
    msg = u"Dear {**}, The Royal Society for Putting Things on top of" \
        "Other Things would like to sincerely thank you for your generous" \
        "donation of ${*}. This kind donation will enable us to put many" \
        "more Things on top of Other Things in the coming year."\
        .format(amount, name)
    print(msg)


def report():
    """
    This function will generate a report of donors and donations.
    The report will contain 'name', total of all donations, number
    of donations, and the average donation value.
    The report will be sorted by the donation total, and formatted so 
    that the values are neatly alligned in rows.
    """
    report_list = []
    for key in d:
        tot = sum(d[key])
        n = len(d[key])
        average = tot / n
        report_entry = (d[key], tot, n, average)
        report_list.append(report_entry)
    report_list.sort(2)
    print(report_list)


if __name__ == '__main__':
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
    print(u'Please select from the following options:')
    print(u'To send a thank you, enter "1"')
    print(u'To Create a Report, enter "2"')
    print(u'To see a list of donors, press "L"')
    print(u'To exit, press "Q"')
    user_input = safe_input(u'Please make your selection now: ->')
    if user_input == '1':
        donor_name(safe_input(u'Enter the Full Name of the Donor: ->'))
    elif user_input == '2':
        report()
    elif user_input.lower == 'l':
        print(donors)

#    elif user_input.lower == 'q':      This is giving me problems right now
#        break
    else:
        __name__ == '__main__'

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
