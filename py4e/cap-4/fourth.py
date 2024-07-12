#while loop
n = 5
while n > 0:
    print(n)
    n = n - 1
    #break           #Breaks the loop
    #continue        #Jumps into next loop
print('Blastoff')
print(n)

#Definite Loops
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

friends = ['Joseph', 'Gleen', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')

#Loop Idioms

#Looping through a Set
print('Before')
higher = 0;
for thing in [9, 41, 12, 3, 74, 15]:
    #print(thing)
    if (higher < thing):
        higher = thing
print('Higher:', higher)

#More loops pattern

#summing in a loop
zork = 0
print('Before', zork)
for think in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

#
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print('Now', count, sum)
print('After', count, sum)
