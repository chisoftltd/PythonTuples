thistuple = ("ben", "joy", "emma", "joy", "emma")
print(thistuple)
print(len(thistuple))


thistuple2 = ("ben",)
print(type(thistuple2))


thistuple2 = ("ben")
print(type(thistuple2))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple4 = ("abd", 34, True, 40, "male")
print(tuple4)
print(type(tuple4))

thistuple1 = tuple(("apple", "banana", "cherry","apple", "banana", "cherry")) # note the double round-brackets
print(thistuple1)
print(thistuple1[1])
print(thistuple1[2])
print(thistuple1[-1])
print(thistuple1[-2])
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","ben", "joy", "emma")
print(thistuple2[1:4])
print(thistuple2[2:])
print(thistuple2[:4])
print(thistuple2[-5:-2])
print(thistuple2)


thistuple3 = ("apple", "banana", "cherry")
if "cherry" in thistuple3:
  print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
print(y)
y.append("orange")
y.remove("banana")
print(y)
y[1] = "kiwi"
x = tuple(y)
print(x)
k = x
del x
print(k)
#print(x)

print(y)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for t in fruits:
    print(t)

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

for i in range(len(fruits)):
    print(fruits[i])
    print(i)

z = 0
while z < len(fruits):
    print(fruits[z])
    z = z + 1

xFruits = thistuple3 + fruits
print(xFruits)
xFruits = xFruits * 2
print(xFruits)
print(xFruits.count("apple"))
print(xFruits.index("banana"))