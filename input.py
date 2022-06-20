#1
#name = input("What is your name? ")
#type(name)
#print("Hello " + name)

#2
#num = int(input("Enter a number: "))
#print("Your number plus one is " + str(num+1))

#3
#far = float(input("Enter the temperature in Fahrenheit"))
#cel = (far - 32) * (5/9)
#print("{:,.2f}".format(cel) + " degrees Celcius")

#4
#name = input("Enter something \"interesting\": ")
#print("Hello " + name)

#5
#name = input("Enter name: ")
#num = int(input("Enter number: "))
#print((name + " ") * num)

#6
#minutes = 45
#name = input("Enter a show that you would watch for " + str(minutes) +" minutes:")
#print(name + " must be pretty good.")

#7
#rate = float(input("Enter hourly rate:"))
#hours = float(input("Enter number of hours:"))
#total = rate * hours
#print("You earned " + str(total) + " and were taxed " + "{:.2f}".format(total * .3) + " and your final pay amount is " + str(total - total * .3))

#8
#name = input("Enter a string:")
#count = name.count("") - name.count(" ")
#print(name.upper())
#print(name.casefold())
#print(count - 1)

#9
#price = float(input("Enter a price: "))
#quantity = float(input("Enter a quantity: "))
#total = quantity * price
#d1 = .1
#d2 = .15
#d3 = .2
#d4 = .25
#d5 = .3

#print(str(int((d1*100))) + "%:${:.2f}".format(total*d1), end="\t")
#print(str(int((d2*100))) + "%:${:.2f}".format(total*d2), end="\t")
#print(str(int((d3*100))) + "%:${:.2f}".format(total*d3), end="\t")
#print(str(int((d4*100))) + "%:${:.2f}".format(total*d4), end="\t")
#print(str(int((d5*100))) + "%:${:.2f}".format(total*d5), end="\t")

#10
#str1 = input("Enter a string: ")
#str2 = str1.replace("Fred", "Barney")
#count = str1.count("z") + str1.count("Z")
#str3 = str1.upper()
#count = str3.count("Z")
#print(str2)
#print("There are " + str(count) + " Z\'s in the string")

#11
#str1 = input("Enter a string: ")
#str2 = str1.upper()
#count = str2.count(" AND ") + str2.count(" BUT ") + str2.count(" OR ")
#print(count)

#12
amount = float(input("Enter an amount: "))
amount = amount * 100

quarters = int(amount / 25)
leftover = amount % 25
dimes = int(leftover / 10)
leftover = leftover % 10
nickels = int(leftover / 5)
leftover = int(leftover % 5)

print("Quaters: " + str(quarters) + " Dimes: " + str(dimes) + " Nickels: " + str(nickels) + " Pennies: " + str(leftover))
