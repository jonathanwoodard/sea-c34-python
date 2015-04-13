def file_new():
    """
    Define a question about reading files.
    Create code to answer the question.
    Question 1:
        How do you create and write to a file within a function?
    """
    file_name = raw_input(u"File to write to:\n ->")
    with open(file_name, 'a') as file:
        file.write(u"This is some text to write to the file.\n")
        # This text will be appended every time the function is run
        file.close()


def file_read(file_name):
    """
    Define a question about writing files.
    Create code to answer the question.
    Question 2:
        How do you read from an existing file within a function?
    """
    file_name = raw_input(u"File to read from:\n ->")
    with open(file_name) as file:
        for line in file:
            print(line)
        file.close()
