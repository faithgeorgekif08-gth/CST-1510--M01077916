
label_name = input ("Please input your username (Type 'quit' if you want to stop):") 
value= int (input("Please enter the value:"))
limit = int (input("Please enter the limit:"))

difference = limit - value 
percent = (value/limit)*100


def check (value=value, limit=limit): 
    difference = limit - value 
    percent = (value/limit)*100
    return 'Difference', difference,"percent",percent

   
def status_of(percent=percent):
    percent = (value/limit)*100
    """Gives the status"""
    if percent>=100:
        status = ("OVER LIMIT")
        print ("The status is: ",status)
    elif percent >=90:
        status = ("WARNING")
        print ("The status is: ",status)
    else:
        status =("OK")
        print ("The status is: ",status)


def print_report():
    """Prints the report"""
    print ("Username:",label_name)
    print ("Value:", value)
    print ("Limit:",limit)
    status_of()
    print ("Difference:",difference)
    print ("Percentage:",percent)


print("=" * 34)
status_of()
print ("The difference is:",difference)
print ("The percentage is:",percent) 
print("=" * 34)

print (check())          

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label_name}")
print("=" * 34)
print ("Value=",value)
print ("Limit=",limit)
status_of()
print (f"Difference:{difference:>5.2f}")
print (f"Percentage:{percent:>5.2f}")
print ()
print("=" * 34)


print ()
print_report()

while True:    
    print ()
    print("=" * 34)
    label = input("Do you want to continue? (If yes write 'YES', If no write 'QUIT'):")
    if label=='quit':
        print ("You printed:",label)
        print ()
        print ("Here is your report:")
        print_report()
        break
    else:
        print ()
        value= int(input ("Please input your new value:"))
        limit =int(input ("Please input your new limit:"))
        status_of()
        check()




