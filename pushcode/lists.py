####################################
# First Official Python            #
# Written by Kartavian Ornjr-Hjarte#
# Date written July 7, 2021        #
####################################
# Clear the terminal screen
import os
os.system('clear')

#####################################
# DATA TYPES
# Strings
# Numbers
# Lists
# Tuples
# Dictionaries
# Boolean
######################################

# Lists

# Test 1
names = ["Loren", "Bob", "Tina"]
print(names[0])

# Test 2
names = ["Loren", "Bob", "Tina"]
names[0] = "Wes"
print(names)
# Test 3
names = ["Loren", "Bob", "Tina"]
names.append("Wes")
print(names)

# Test 4
names = ["Loren", "Bob", "Tina"]
names.append("Wes")
print(names[3])

# Test 5
names = ["Loren", "Bob", "Tina", 38]

print(names[3])

# Test 6
names = ["Loren", "Bob", "Tina", 38]

print(names[3] + 10)

# Test 7
other_name = "Jean"
names = ["Loren", "Bob", "Tina", other_name]

print(names)
# Test 8
nums = [1, 2, 3, 4, 5]
names = ["Loren", "Bob", "Tina", nums]

print(names)
# Test 9
nums = [1, 2, 3, 4, 5]
names = ["Loren", "Bob", "Tina", nums]

print(names[3])
# Test 10
nums = [1, 2, 3, 4, 5]
names = ["Loren", "Bob", "Tina", nums]

print(names[3][2])
# Test 11
nums = [1, 2, 3, 4, 5]
names = ["Loren", "Bob", "Tina", nums]

print(names[3][2] + 10)
# Test 12
names = ["Loren", "Bob", "Tina"]
print(len(names))
# Test 13
names = ["Loren", "Bob", "Tina"]
print(names[len(names)-1])
# Test 14
# Test 15
