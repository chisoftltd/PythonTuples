set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

print(type(set1))
print(type(set2))
print(type(set3))

#Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
print()

#Python - Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
thisset.add("okwa")

print(thisset)

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Python - Remove Set Items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Discard
#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#pop()
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#claer()
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#del
thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset)

#Python - Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Python - Join Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set3.union(set2)
print(set4)

#update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)