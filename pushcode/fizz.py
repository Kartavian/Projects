####################################
# First Official Python            #
# Written by Kartavian Ornjr-Hjarte#
# Date written July 7, 2021        #
####################################
# Clear the terminal screen
import os
os.system('clear')

#####################################
# FizzBuzz Practice
######################################

# FizzBuzz!

# Test 1 
num = 0

while (num <= 100):
    if (num % 3 == 0) and (num % 5 == 0):
        print(str(num) + ". FizzBuzz!")
    elif (num % 3 == 0):
        print(str(num) + ". Fizz!")
    elif (num % 5 == 0):
        print (str(num) + ". Buzz!")
    else:
        print(str(num) + ".")
    num += 1
# Test 2 
num = 0
# Create a while loop to count up to 100
while (num <= 100):
    # Create if statement to include 2, 3, 4 and 5
    if (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". JizzFizzWizzBuzz!")
    # Create elifs that remove 3
    elif (num % 2 == 0) and (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". JizzWizzBuzz!")
    # Create elifs that remove 3 and 4
    elif (num % 2 == 0) and (num % 5 == 0):
        print(str(num), ". JizzBuzz!")
    # Create elifs that remove 2
    elif (num % 3 == 0) and (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". FizzWizzBuzz!")
    # Create elifs that remove 2 and 4
    elif (num % 3 == 0) and (num % 5 == 0):
        print(str(num), ". FizzBuzz!")
    # Create elifs that remove 2 and 3
    elif (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". WizzBuzz!")
    # Create elifs that remove 5
    elif (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0):
        print(str(num), ". JizzFizzWizz!")
    # Create elifs that remove 4 and 5
    elif (num % 2 == 0) and (num % 3 == 0):
        print(str(num), ". JizzFizz!")
    # Create elifs that remove 3 and 5
    elif (num % 2 == 0) and (num % 4 == 0):
        print(str(num), ". JizzWizz!")
    # Create elifs that remove 3, 4 and 5
    elif (num % 2 == 0):
        print(str(num), ". Jizz!")
    # Create elifs that remove 2, 4 and 5
    elif (num % 3 == 0):
        print(str(num), ". Fizz!")
    # Create elifs that remove 2, 3 and 5
    elif (num % 4 == 0):
        print(str(num), ". Wizz!")
    # Create elifs that remove 2, 3, and 4
    elif (num % 5 == 0):
        print(str(num), ". Buzz!")
    # print all other numbers with "."
    else:
        print(str(num), ".")
    num += 1
# Test 3 
num = 0
jizzcount = 0
fizzcount = 0
wizzcount = 0
buzzcount = 0
jizzbuzzcount = 0
jizzfizzcount = 0
jizzwizzcount = 0
fizzwizzcount = 0
fizzbuzzcount = 0
wizzbuzzcount = 0
jizzfizzwizzcount = 0
jizzwizzbuzzcount = 0
jizzfizzbuzzcount = 0 
fizzwizzbuzzcount = 0
jizzfizzwizzbuzzcount = 0
# Create a while loop to count up to 100
while (num <= 100000):
    # Create if statement to include 2, 3, 4 and 5
    if (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". JizzFizzWizzBuzz!")
        jizzfizzwizzbuzzcount += 1
    # Create elifs that remove 3
    elif (num % 2 == 0) and (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". JizzWizzBuzz!")
        jizzwizzbuzzcount += 1
    # Create elifs that remove 3 and 4
    elif (num % 2 == 0) and (num % 5 == 0):
        print(str(num), ". JizzBuzz!")
        jizzbuzzcount += 1
    # Create elifs that remove 2
    elif (num % 3 == 0) and (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". FizzWizzBuzz!")
        fizzwizzbuzzcount += 1
    # Create elifs that remove 2 and 4
    elif (num % 3 == 0) and (num % 5 == 0):
        print(str(num), ". FizzBuzz!")
        fizzbuzzcount += 1
    # Create elifes that remove 2 and 5
    elif (num % 2 == 0) and (num % 5 == 0):
        print(str(num), ". FizzWizz!")
        fizzwizzcount += 1
    # Create elifs that remove 2 and 3
    elif (num % 4 == 0) and (num % 5 == 0):
        print(str(num), ". WizzBuzz!")
        wizzbuzzcount += 1
    # Create elifs that remove 5
    elif (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0):
        print(str(num), ". JizzFizzWizz!")
        jizzfizzwizzcount += 1
    # Create elifs that remove 4 and 5
    elif (num % 2 == 0) and (num % 3 == 0):
        print(str(num), ". JizzFizz!")
        jizzfizzcount += 1
    # Create elifs that remove 3 and 5
    elif (num % 2 == 0) and (num % 4 == 0):
        print(str(num), ". JizzWizz!")
        jizzwizzcount += 1
    # Create elifs that remove 3, 4 and 5
    elif (num % 2 == 0):
        print(str(num), ". Jizz!")
        jizzcount += 1
    # Create elifs that remove 2, 4 and 5
    elif (num % 3 == 0):
        print(str(num), ". Fizz!")
        fizzcount += 1
    # Create elifs that remove 2, 3 and 5
    elif (num % 4 == 0):
        print(str(num), ". Wizz!")
        wizzcount += 1
    # Create elifs that remove 2, 3, and 4
    elif (num % 5 == 0):
        print(str(num), ". Buzz!")
        buzzcount += 1
    # print all other numbers with "."
    else:
        print(str(num), ".")
    num += 1
    
# Display table with counts #
print("_____________________________________")
print("Jizz\tFizz\tWizz")
print(str("{:,}".format(jizzcount)) + "\t" + str("{:,}".format(fizzcount)) + "\t" + str("{:,}".format(wizzcount)))
print("Buzz\tJizzFizz\tJizzWizz")
print(str("{:,}".format(buzzcount)) + "\t\t" + str("{:,}".format(jizzfizzcount)) + "\t\t" + str("{:,}".format(jizzwizzcount)))
print("JizzBuzz\tFizzWizz\tFizzBuzz")
print(str("{:,}".format(jizzbuzzcount)) + "\t\t" + str("{:,}".format(fizzwizzcount)) + "\t\t" + str("{:,}".format(fizzbuzzcount)))
print("WizzBuzz\tJizzFizzWizz\tJizzFizzBuzz")
print(str("{:,}".format(wizzbuzzcount)) + "\t\t" + str("{:,}".format(jizzfizzwizzcount)) + "\t\t" + str("{:,}".format(jizzfizzbuzzcount)))
print("JizzWizzBuzz\tFizzWizzBuzz\tJizzFizzWizzBuzz")
print(str("{:,}".format(jizzwizzbuzzcount)) + "\t\t" + str("{:,}".format(fizzwizzbuzzcount)) + "\t\t" + str("{:,}".format(jizzfizzwizzbuzzcount)))
# Test 4 
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
