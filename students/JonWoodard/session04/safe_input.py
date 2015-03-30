def safe_input():
    
    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    """

    raw_input('Prompt for user input ->')
    if EOFError is True:
        return 'None'
    if KeyboardInterrupt is True:
        return 'None'

