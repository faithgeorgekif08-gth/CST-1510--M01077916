# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, value):   # this parameter should be self
       percent = (value/100)
       return percent

r = Record()
print(r.status(95))
