# python has five standard data types
basic_salary = 500


# Numbers, String, List, Tuple, Dictionary
counter = 100
miles = 100.50
name = "Sophanna M."

a = b = c = 1
b = 2
c = 3
A, B, C = 1, 2, "Sophanna M."

# List
lists = [a, b, c, "Last List"]

# Delete the element at index 1 using the del statement
# if 1 in lists
# del lists[1]
# else :
# statement
# Delete elements in the range [2:3] using the del statement with slicing
# del lists[2:3]

if 2 in lists and 3 in lists:
    lists.insert(2, 3)
else:
    print("IndexError: list index out of range")

# Dic
Dic = []
# put integer values
Dic = {1: "Supervised Learning", 2: "UnSupervised Learning", 3: "Reinforcement Learning"}

# Tup
tup = ("Supervised Learning", "UnSupervised Learning", "Reinforcement Learning")

# Set

mySet = set(["Supervised Learning", "UnSupervised Learning", "Reinforcement Learning"])

print(counter)
print(miles)
print(name)
print("A, B, C", a, b, c)
print("List:", lists)
print("Dic:", Dic)
print("Tup:", tup)
print("Set:", mySet)
