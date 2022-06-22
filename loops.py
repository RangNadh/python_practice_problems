#1
#for i in {"Forrest", "Jenny", "Mama", "Bubba"}:
#    print("Hello " + i)

#2
#word = "flop"
#counter = int(input("Enter number of iterations:"))
#for i in range(counter):
#    if (word == "flop"):
#        word = "flip"
#    else:
#        word = "flop"
#    print(str(i) + " " + word)

#----------------another method
#word = "flop"
#counter = int(input("Enter number of iterations:"))
#for i in range(counter):
#    if ((i % 2) == 0):
#        word = "flip"
#    else:
#        word = "flop"
#    print(str(i) + " " + word)

#3
#for i in "alpha", "beta", "gamma":
#    for j in "dev", "test", "prod":
#        if (j == "prod"):
#            loop_size = 4
#        else:
#            loop_size = 1
#        for k in range(loop_size):
#            print(i + "-" + j + "-0" + str(k + 1), end=" ")
#    print("\n")

#4
#count = int(input("Enter number of iterations: "))
#for i in range(1,count+1):
#    print(str(i), end=" ")
#for i in range(count-1,0,-1):
#    print(str(i), end=" ")

#5
#s = int(input("Enter number of iterations:"))
#for i in range(s):
#    print("*" * (i + 1))
#for i in range(s-1,0,-1):
#    print("*" * i)

#6
#lower = 5
#upper = 12
#loop = True
#while (loop):
#    num = int(input("Enter number between " + str(lower) + " and " + str(upper) + ":"))
#    if (lower < num < upper):
#        loop = False
#    else:
#        print("That number is outside of the boundary")
#print("The number fits")

#7
#password_length = 8
#loop = True
#while (loop):
#    p = input("Enter new password: ")
#    #p_upp = p.upper()
#    #p_low = p.lower()
#    #p_count = len(p)
#    if ((p == p.lower()) or (p == p.upper()) or (len(p) < password_length)):
#        print("Bad password. Please try another")
#    else:
#        loop = False
#        print("New Password Accepted")

#8
width = int(input("Enter width:"))
height = int(input("Enter height:"))
fill = input("Enter fill:")

if fill == "Y" or fill == "y":
    fill = True
else:
    fill = False
print("*" * width)
for i in range(height - 2):
    if (fill):
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")
print("*" * width)