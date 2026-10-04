
# ==================================================================== INPUT

label = input("Please enter your names here: ")      
first = float(input("Please enter your first number here:" ))  
second = float(input("Please enter your second number here: "))   


# ================================================================== PROCESS

difference = (second-first)  
percent = (first/second)* 100      


# =================================================================== OUTPUT

print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print (f"Name: {label:>10}")
print (f"First number:  {first:>10}")
print (f"Second number: {second:>10}")  
print("=" * 34)

diff_01 = f"The difference between the first and the second:{difference:>+10.2f}"
perc_01 = f"The percentage of the first to the second is:{percent:>+13.2f}%"
print (diff_01)
print (perc_01)
print("=" * 34)

# ==========================================================================

