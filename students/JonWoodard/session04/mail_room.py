#!/usr/bin/python
# create a dictionary, d = {}
d = {}
# donors
ls1 = ['Felix Hernandez', 'Hisashi Iwakuma', 'Taijuan Walker',
       'Mike Zunino', 'Robinson Cano', 'Brad Miller', 'Kyle Seager']
# amounts
ls2 = [[1700.00], [900.00], [1600.00], [150.00], [1100.00], [250.00], [750.00]]
d = dict(zip(ls1, ls2))
# donors = []
# amounts = []
# for key in d:
#     donors.append(key)
#     amounts.append(d[key])


# create a function to prompt user for data
def safe_input(prompt):

    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    Args:
        prompt = 'Prompt user for desired input'
    Returns:
        input or 'None'
    """
    try:
        usr_in = raw_input(prompt)
    except:
        EOFError or KeyboardInterrupt
        return "None"
    else:
        return usr_in


# create function to ask for donor name
def donor_name(name):
    """
    This function will check to see if a name is in the dictionary.
    If yes, prompt for donation amount.
    If no, add, then prompt for amount.
    """
    # prompt = u'Enter the Full Name of the Donor: ->'
    # name = safe_input(prompt)
    if name in d:
        pass
        # donation_amount(safe_input)
    else:
        d[name] = []


def donation_amount(name, amount):
    """
    This function will determine whether the value entered is a number
    If the value is a number, an email will be generated
    Otherwise it will return the user to the donation_amount function
    """
    # prompt = u'Please enter the donation amount: ->'
    # amount = safe_input(prompt)
    if amount is float or int:
        if amount in d[name]:
            pass
            # email_text()
        else:
            d[name].append
    else:
        print('That does not appear to be a valid number. Try again')
        donation_amount(name, amount)


def email_text(name, amount):
    """
    This function will take the user entered name and donation amount
    to generate a thank you email.
    Args:
        name: name entered in safe_input.
        amount: float entered in safe_input.
    Returns:
        msg
    """
    msg = (
        u"Dear {},\n"
        u"The Royal Society for Putting Things on top of Other \n"
        u"Things would like to sincerely thank you for your \n"
        u"generous donation of ${}. This kind donation will enable \n"
        u"us to put many more Things on top of Other Things in the \n"
        u"coming year. \n\n"
        ).format(amount, name)
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
        report_entry = (key, tot, n, average)
        report_list.append(report_entry)
    report_list.sort(key=lambda report_entry: report_entry[1], reverse=True)
    print(
        "{:22s} {:16s} {:20s} {:20s}\n".format(
            "Name", "Total Donations", "Number of Donations",
            "Average Donation"
        )
    )
    for i in report_list:
        print(
            "{:22s} {:<16,.2f} {:<20d} {:<20,.2f}".format(
                i[0], i[1], i[2], i[3]
            )
        )
    print("\n\n")


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
    while True:
        user_input = safe_input(
            u"\nPlease select from the following options:\n"
            u"To send a thank you, enter '1'\n"
            u"To Create a Report, enter '2'\n"
            u"To see a list of donors, press 'L'\n"
            u"To exit, press 'Q'\n"
        )
        if user_input.lower() == u'q':
                break
        elif user_input == '1':
            while True:
                name = safe_input(
                    u"\nEnter the Full Name of the Donor: \n ->"
                )
                if name.lower() == u"l":
                    for key in d:
                        print(key)
                elif name.lower() == u"q":
                    break
                else:
                    if name not in d:
                        d[name] = []
                        False
                    else:
                        amount = safe_input(
                            u"\nPlease enter the donation amount: \n"
                        )
                        False
        elif user_input == '2':
                report()
        elif user_input.lower() == 'l':
            for key in d:
                print(key)
        else:
            print(
                u"\nThat is not a valid entry\n"
                u"Please try again\n"
            )
            # return True


#            __name__ == '__main__'

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
