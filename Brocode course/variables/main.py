#variable =  a container
#you can check the data type with code (type)
#you should change the data type of variables sometime (str(jjj))

first_name = "Ozan"
last_name = "Bekar"
full_name = first_name+" "+last_name
print("Hello "+full_name)
#print(type(full_name))

age = 19
age += 1
print("Your age is "+str(age))
#print(type(age))

height = 181.6
print("Your height is "+str(height))
#print(type(height))

human = True
print("Are you a human "+str(human))
#print(type(human))
print()
print()
#Multiple assigment = allows us to assign multiple variables at the same time in one line of code

#name = "Akif"
#age = 15
#kucuk = True

name,age,kucuk = "Akif", 15,True

print(name)
print(age)
print(kucuk)

print()
print()

#vize1 = 30
#vize2 = 30
#final = 30

vize1 = vize2 = final = 30

print(vize1)
print(vize2)
print(final)