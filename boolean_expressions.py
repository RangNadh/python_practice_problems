#1
a = True
b = False
print(a and b)

#2
a = False
b = False
print("The answer is " + str(a or b))

#3
a = True
print("The answer is " + str(not a))

#4
monday = True
tuesday = False
wednesday = True
thursday = False
var = (monday and wednesday) or (tuesday and thursday)
print("The answer is " + str(var))

#5
shirt = False
sweater = False
pants = False
shorts = False
var = (shirt or sweater) and (pants or shorts)
print("The answer is " + str(var))

#6
bacon = False
lettuce = False
tomato = False
corndog = False
pizza = True
var = (bacon and lettuce and tomato) or (corndog or pizza)
print("The answer is " + str(var))

#7
kill_switch = False
left_button = True
right_button = True
light  = (not kill_switch) and (left_button or right_button)
print("The light is " + str(light))

#8
gf_01 = False
gf_02 = False
happy = (gf_01 and not gf_02) or (not gf_01 and gf_02)
print("BF is happy - " + str(happy))

#9
age  = 66
wants_coffee = True
print("Free Coffee - " + str(wants_coffee and (age > 65)))

#10
hi_temp = 212
lo_temp = 32
curr_temp = 100
temp = (curr_temp < hi_temp) and (curr_temp > lo_temp)
print("Between hi and low - " + str(temp))

#11
num  = int(input("Enter an integer: "))
print("The number is even - " + str(num%2 == 0))  #or str(not num%2)

#12
user  = "fred"
password = "chicken"
u_user = input("Enter user name:")
u_password = input(("Enter password:"))
auth = (u_user == user) and (u_password == password)
print("This user/pass combination is good - " + str(auth))
