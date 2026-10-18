# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
try:
    with open("records.txt") as f:
        (f.read())
# the file 'records.txt' was not found.
# we have to use the try... except function and remove 'print'
except FileNotFoundError:
    print ("File 'records.txt' was not found")