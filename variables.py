#1
print("Hello World")

#2   variables must follows the case-sensitive
name = "Wilbur"
Name = "Orville"
print("Hello " + Name)

#3
title = "Mr"
first = "Orville"
last = "Wright"
print("Hello " + " " + title + " " + first + " " + last)

#4               in this problem variable is multiplied with count which was given
var = "chicken"
print((var + " ") * 4)

#5
var = "chicken"
#var = "chicken\n"
print((var + "\n") * 3)

#6                 by using end=" " we can print the elements in the same line
title = "Mr"
first = "Orville"
last = "Wright"
print("Hello", end=" ")
print(title, end=" ")
print(first, end=" ")
print(last, end=" ")

#7
print("There are three \"chickens\" in the house")

#8
b = 4
print("The answer is:",b)    #or str(b) and add to that statement

#9
a = 4
b = 5
c = a + b
print(str(a) + "+" + str(b) + "=" + str(c))

#10
a = 3
b = 4
c = 5
print("(" + str(a) + "+" + str(b) + ")" + str(c) + "=" + str((a + b)* c))

#11
a = 3
b = 5
print(str(a) + " raised to the " + str(b) + " power is " + str(a ** b))

#12
a = 20
b = 3
print("The answer is " + str(a // b) + " with remainder of " + str(a % b)) #or str(int(a/b))

#13                  how many decimals we want we can print by using this technique
var1 = 10/3
print("The result is " + "{:,.2f}".format(var1))

#14
a=1
print("a=" + str(a) + "\ta+1=" + str(a + 1) + "\ta+2=" + str(a + 2) +  "\ta+3=" + str(a + 3))
a=4
print("a=" + str(a) + "\ta+1=" + str(a + 1) + "\ta+2=" + str(a + 2) +  "\ta+3=" + str(a + 3))
a=56
print("a=" + str(a) + "\ta+1=" + str(a + 1) + "\ta+2=" + str(a + 2) +  "\ta+3=" + str(a + 3))

#15
print((("happy " * 2) + ("joy " * 2)) * 2)
print((("happy " * 2) + ("joy " * 3)) * 3)
print(("happy " * 2) * 6)
print((("this " * 2) + ("that " * 2)) * 3)

#16
print("Jalepe\xf1o peppers are good on pizza")