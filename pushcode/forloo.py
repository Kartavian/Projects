####################################
# First Official Python            #
# Written by Kartavian Ornjr-Hjarte#
# Date written July 7, 2021        #
####################################
# Clear the terminal screen
import os
os.system('clear')

#####################################
# For Loops Practice
######################################

# For Loops

# Test 1 Displaying character by character
name = "Loren"

for x in name:
    print (x)
# Test 2 Displaying a list by name
names = ["Loren Stevenson", "Bob Hope", "Mary Marcus"]

for name in names:
    print (name)
# Test 3 adding Dictionaries
fav_pizza = {
    "Loren Stevenson" : "Pepperoni and Black Olives",
    "Bob Hope" : "Mushroom",
    "Mary Marcus" : "Cheese"
}

for key,val in fav_pizza.items():
    print (key, "likes", val, "pizza!")
# Test 4 combining lists and dictionaries to test understanding of differences
names = ["Loren Stevenson", "Kartavian Ornjr-Hjarte", "Violet Victoria"]

fav_pizza = {
    names[0] : "Pepperoni and Black Olives",
    names[1] : "Sausage and Pineapple",
    names[2] : "Banana Peppers and Green Olives"
}

for key, val in fav_pizza.items():
    print (key + " likes " + val + " pizza!")
# Test 5
# Test 6
# Test 7
# Test 8
# Test 9
# Test 10
# Test 11
# Test 12
# Test 13
# Test 14
# Test 15
