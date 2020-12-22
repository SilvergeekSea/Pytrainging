# LBYL - Look before you leap
# EAFP - Easier to ask forgiveness than permission (Pythonnic style)
"""
P = c:\temp\test.txt
try:
    process_file(f)
except OSError as e:
    print (f'Error: {e}')

"""

try:
    import msvcrt

    def getkey():
        return msvcrt.getch()
except ImportError:

    import sys
    import tty
    import termios

    def getkey():