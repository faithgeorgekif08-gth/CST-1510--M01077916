"""
RECORD CHECK  -  my version
===========================

Name  :Faith George
Lane  :  AI
Date  :17/10/2026

Run it:   python template.py


"""

# =================================================================== FUNCTIONS

# define the variables
def check (label, value, limit): 
    difference = limit - value 
    percent = (value/limit)*100
    if percent>=100:
        status = ("OVER LIMIT")
    
    elif percent >=90:
        status = ("WARNING")
   
    else:
        status =("OK")
        
    return difference, percent ,status

# print the report by defining
def print_report(label, value, limit, difference, percent, status):
    """Prints the report"""
    print ("Username:",label)
    print ("Value:", value)
    print ("Limit:",limit)
    print ("Difference:",difference)
    print ("Percentage:",percent)
    print ("Status:", status)
    print ()
    print ("="*40)
    print ()

# ====================================================================== STORE
#storing your data
records = [
    {"label": "R-001", "value": "64", "limit": "100"},
    {"label": "R-002", "value": "50", "limit": "100"},
    {"label": "R-003", "value": "120", "limit": "100"}
]   

# opening a text file
with open ("records.txt", "w") as l:
    l.write("R-001, 64, 100\n")
    l.write ("R-002, 50, 100\n")
    l.write ("R-003, 120, 100\n")



# =============================================================== PROCESS + OUTPUT

# counting the over limits
over_limit = 0
with open ("records.txt", "r") as l:
    for one in l:
        label, value, limit = one.split(",")
        value = float(value)
        limit = float(limit)

        result = check (label, value, limit)
        difference = result[0]
        percent = result[1]
        status = result[2]

        print_report(label, value, limit, difference, percent, status)


        if status == "OVER LIMIT":
            over_limit =+ 1    

print ("Total over limit counts: ",over_limit) 

