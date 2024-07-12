#Conditional
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

#Comparison Operators
if x == 5:
    print('Equals 5')
if x <= 5:
    print('Lower or equals 5')
if x >= 5:
    print("Higher or equals 5")
if x != 5:
    print("Not equals 5")

#Nested Decisions
if x > 5:
    if x < 10:
        print(x)

print('x: ',x)

#Two-way Decisions
if x > 5 :
    print('Bigger')
else :
    print('Smaller')

#Multi-way
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')

#try...except
age = 0
while age==0:
    try:
        age = int(input("Edad: "))
    except:
        age = 0
        print('Age should be a number')
print(age)
