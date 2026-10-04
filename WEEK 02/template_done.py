
# ==================================================================== INPUT

label = input("Please insert your hostname: ")      
value = float(input("Please input the value: "))     
limit = float(input("Please input your limit: "))    


# ================================================================== PROCESS


difference = (limit - value)   
percent = (value/limit)*100  


if percent >= 100:
    result = "OVER LIMIT"
elif percent >= 90:
    result = "WARNING"
else:
    result = "OK" 


# =================================================================== OUTPUT


print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 50)     

print(f"Hostname:{label:>7}")
print (f"Value:{value:>10}")
print (f"Limit:{limit:>10}")
print (f"Status:{result:>7}")
print("=" * 50)
print (f"The difference between the value and limit is:{difference:>10.2f}")
print (f"The percentage of value over limit is:{percent:>18.2f}%")
print("=" * 50)


# ==========================================================================

