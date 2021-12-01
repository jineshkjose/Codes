#https://www.onlinegdb.com/
term=20			#in year
term=term*365
intr=10			#yearly interest 
intr=(intr/100)/365
amtinit=100
amt=0

for number in range(term):
    amt=((amt+amtinit)*intr)+((amt+amtinit))



print("Invested Amount")
print(100*term)
print("Return")
print(amt)