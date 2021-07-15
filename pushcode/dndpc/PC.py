from tkinter import *
import subprocess


###############################
#   Player Character Program  #
#                             #
#  Created by Loren Stevenson #
#                             #
# Date Started: July 14, 2021 #
###############################
#####################################
# Creating a DnD 5th edition player #
#  character sheet in program form  #
#####################################

pc = Tk()
pc.title("Character Sheet")
pc.iconbitmap('E:/OC/pushcode/Python Resume files/face.ico')
pc.geometry("750x600")
pc.configure(bg='purple')



################################################
# check for character.txt file, if not created,#
# create by calling the Character Creation.exe #
################################################

p1 = subprocess.run(["cat", "character.dat"], capture_output=True, text=True)



######################################################################
# Section for variables we call gathered from Character Creation.exe #
######################################################################

###############
# Player Name #
###############

pnamef = str()
pnamel = str()
pname = (pnamef, pnamel)

##################
# Character Name #
##################

cnamef = str()
cnamel = str()
cname = (cnamef, cnamel)

##################
# Character Race #
##################

race = str() # call from race.py

###################
# Character Class #
###################

cclass = str()

#########
# Level #
#########

lvl = int()

##############################################
# include a way to input exp and an equation #
#    or table to know when to add level      #
##############################################

exp = int()

#*************
#* Abilities *
#*************

strength = int()
stmod = int((strength - 10) / 2)
dex = int()
dexmod = int((dex - 10) / 2)
con = int()
conmod = int((con - 10) / 2)
intel = int()
intmod = int((intel - 10) / 2)
wis = int()
wismod = int((wis - 10) / 2)
cha = int()
chamod = int((cha - 10) / 2)





# Continue to remain open
pc.mainloop()