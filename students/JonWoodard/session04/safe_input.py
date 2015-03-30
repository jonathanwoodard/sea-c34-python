def safe_input():
    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    """

    out = raw_input('Prompt for user input ->')
    while out == EOFError:
        return 'eof'
    while out == KeyboardInterrupt:
        return 'int'
    print(out)
