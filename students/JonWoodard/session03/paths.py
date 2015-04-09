def paths(quest1):
    """
    Define a question about paths.
    Question 1:
        how do you change the path of a file?
    """
import pathlib
pth = pathlib.Path('./')
pth.is_dir()
True
pth.absolute()
PosixPath('/Users/Chris/PythonStuff/CodeFellowsClass/sea-f2-python-sept14/Examples/Session04')
for f in pth.iterdir():
    print(f)
junk2.txt
junkfile.txt
