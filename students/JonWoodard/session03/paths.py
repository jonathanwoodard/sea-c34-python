def paths():
    """
    Define a question about paths.
    Question 1:
        Can you print the current working directory within a function?
    """
    from pathlib import Path
    print(Path.cwd())
