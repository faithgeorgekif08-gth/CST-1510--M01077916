"""
RECORD CHECK  -  my version
===========================

Name  : Faith George
Lane  :  AI 
Date  :08/11/2026

Run it:   python template.py

"""


# create parseline that cleans
def parseline (rawline):
    """Returns messy lines into a clean list/dictionary."""
    raw = rawline.strip()
    hostname, rest = raw.split(",",1)
    hostname = hostname.strip().lower()
# handle spacing and case


    Records = {}
    # put in a dict

    for each in rest.split(","):
        key, value = each.split("=")
        value = float(value.strip())
        key = key.strip()

        Records["hostname"]=hostname
        Records [key]= value
    return {"hostname": hostname, "rating": Records["rating"], "age": Records["age"]}  
# and prints into a dict


def status (rating,age):
    """Defines status"""
    percent = (rating/age)*100
    if percent >= 100:
        """Gives output if percent is greater than 100"""
        return ("OVERLIMIT")
    elif percent >= 90:
        """Output if percent is greater than 90 but less than 100"""
        return ("WARNING")
    else:
        """Output if percent is less than 90"""
        return ("OK")


# count your records and over limit status
record_count = 0
over_limit_count = 0

# read the file (messy) written
with open("raw_records.txt", "r") as rf:
        for rawline in rf:
            Records = parseline (rawline)
            #print (Records)
            result = status(Records["rating"], Records["age"])

            record_count += 1


            if result == "OVERLIMIT":
                 over_limit_count += 1


            print (Records)     
            print ("Status:",result)
""" printed hostname and the results."""

# print record count and over limit count
print ("The record count is:",record_count)
print ("The Over limit count is:", over_limit_count)

# ====================================================================================