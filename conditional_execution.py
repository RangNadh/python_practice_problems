#1
add_extra = True
print("This is always printed")
if (add_extra == True):
    print("This is conditionally printed")

#2
num  = int(input("Enter an integer:"))
pt = 50
if num > 50:
    print("The number is over " + str(pt))
else:
    print("The number is less than " + str(pt))

#3
have_dog = False
print("Welcome to our bed and breakfast")
if (have_dog):
    print("Please visit our library")
    print("Come see our kitchen")
else:
    print("Your dog is welcome")
    print("Free dog treats available")
print("We hope you enjoy your stay")

#4
name = input("Enter Forrest or Bubba:")
if name == "Forrest":
    print("Have a nice day")
elif name == "Bubba":
    print("Shrimp is the fruit of the sea")
else:
    print("Invalid Entry")

#5
hour = int(input("Enter hour:"))
if (hour == 7 or hour == 13 or hour == 19):
    print("Time to feed the dog")
elif (hour < 24):
    print("Do something else")
else:
    print("Invalid Entry")

#6
name = input("Enter a string:")
if (name == name.lower()):
    print("That was all lower case letters!")
elif (name == name.upper()):
    print("That was all upper case letters!")
else:
    print("That had upper and lower case letters!")

#7
num = int(input("Enter an integer:"))
b_pt = 50
if (not num % 2 and num < b_pt):
    print("Less than " + str(b_pt) + " and even")
elif (not num % 2 and num > b_pt):
    print("More than " + str(b_pt) + " and even")
elif (num % 2 and num < b_pt):
    print("Less than " + str(b_pt) + " and odd")
elif (num % 2 and num > b_pt):
    print("More than " + str(b_pt) + " and odd")

#------------------another method

breaking = 50
even_state = "even"
over_state = "Less"

num = int(input("Enter an integer:"))
if(num % 2):
    even_state = "odd"
if(num > breaking):
    over_state = "More"
print(over_state + " than " + str(breaking) + " and " + even_state)

#8
num = int(input("Enter an integer:"))
div = 2
prime = True
if (not num % div):
    print("Number is evenly divisible by " + str(div))
    prime = False
div = 3
if (not num % div):
    print("Number is evenly divisible by " + str(div))
    prime = False
div = 4
if (not num % div):
    print("Number is evenly divisible by " + str(div))
    prime = False
div = 5
if (not num % div):
    print("Number is evenly divisible by " + str(div))
    prime = False
div = 6
if (not num % div):
    print("Number is evenly divisible by " + str(div))
    prime = False
if (prime):
    print("Kinda looks prime")

#9
year = True
song = True
fname = input("Enter the first name of a Beatle:")
if (fname == "John"):
    print("John Lennon")
    if (year): print("1965")
    if (song): print("Help")
elif (fname == "Paul"):
    print("Paul McCartney")
    if (year): print("1968")
    if (song): print("Blackbird")
elif (fname == "George"):
    print("George Harrison")
    if (year): print("1969")
    if (song): print("Here Comes the Sun")
elif (fname == "Ringo"):
    print("Ringo Starr")
    if (year): print("1966")
    if (song): print("Yellow Submarine")
else:
    print("Invalid Entry")

#10
num  = int(input("Enter an integer (1-5):"))
if (num == 1): print("Edit Name")
elif (num == 2): print("Edit Address")
elif (num == 3): print("Edit Passphrase")
elif (num == 4): print("Edit Payment Method")
elif (num == 5): print("Edit Default Language")
else: print("Invalid Entry")

#11
input_string = input("Enter an integer:")
try:
    input_int = int(input_string)
    input_int = abs(input_int)
    #if (input_int < 0):
    #   input_int = input_int * -1
    print("The absolute value is " + str(input_int))
except:
    print("That was not an integer")

#12
level1 = 5
level2 = 10
discount1 = .05
discount2 = .1

price = input("Enter unit price: ")
quantity = input("Enter quantity: ")

try:
    price = float(price)
    quantity = float(quantity)
    if (quantity <= 0 or price <= 0):
        print("No negative values")
    else:
        if (quantity <= level1):
            total = price * quantity
        if (level1 < quantity <= level2):
            total = (level1 * price) + ((quantity - level1) * price * (1 - discount1))
        if (quantity > level2):
            total = (level1 * price) + ((level2 - level1) * price * (1 - discount1)) + ((quantity - level2) * price * (1 - discount2))

        print("Total: " + "{:.2f}".format(total))
except:
    print("Invalid Input")
