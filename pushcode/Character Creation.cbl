		>>SOURCE FORMAT FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. character_creation.
AUTHOR. Loren Stevenson
DATE-WRITTEN. July 8, 2021
ENVIRONMENT DIVISION.

DATA DIVISION.
FILE SECTION.
WORKING-STORAGE SECTION.

01 pname.
	02 pnamef	PIC x(7).
	02 pnamel	PIC x(10).
01 cname.
	02 cnamef	PIC x(10).
	02 cnamel	PIC x(12).
	
01 cls PIC x(10).
01 race PIC x(10).

01 abil.
	02 strenth	PIC 9(2).
	02 dex	PIC 9(2).
	02 con	PIC 9(2).
	02 wis	PIC 9(2).
	02 int	PIC 9(2).
	02 cha	PIC 9(2).
	02 strmod PIC 9(2).
	02 dexmod PIC 9(2).
	02 conmod PIC 9(2).
	02 wismod PIC 9(2).
	02 intmod PIC 9(2).
	02 chamod PIC 9(2).
	
01 answer PIC X.


PROCEDURE DIVISION.
DISPLAY "What is your first name? " WITH NO ADVANCING
ACCEPT pnamef
DISPLAY "Hello " pnamef "! What is you last name? " WITH NO ADVANCING
ACCEPT pnamel
DISPLAY "Okay, " pname "!  What is your new Character's first name? " WITH NO ADVANCING
ACCEPT cnamef
DISPLAY "Nice!  You will now be known as " cnamef "! What is your last name? " WITH NO ADVANCING
ACCEPT cnamel
DISPLAY "You are now, " cname ".  Now, What is your Class, " cnamef "? " WITH NO ADVANCING
ACCEPT cls
IF cls = "Druid" THEN
	DISPLAY "A Druid is a powerful force for Nature.  Respect the power nature has given you. "
END-IF
	
IF cls = "Fighter" THEN
	DISPLAY "Strong and courageous, a fighter is the cunning muscle of the party!"
END-IF

IF cls = "Barbarian" THEN
	DISPLAY "A Barbarian is a Sentient being that forsakes their Sentience to be a stronger fighter."
	DISPLAY	"Honor, Valor means nothing to you once the you have entered your Rage. "
END-IF
	
IF cls = "Cleric" THEN
	DISPLAY "A Cleric is a powerful force of the Divine.  Respect, Honor, Devotion. "
END-IF
	
IF cls = "Monk" THEN
	DISPLAY "So you wish to punch your enemies to death, " cnamef "?"
	DISPLAY "May your fists land true and strong, " cls ". "
END-IF
	
IF cls = "Paladin" THEN
	DISPLAY "Are you truly a warrior for both the Law AND Good, " cnamef "?"
	DISPLAY "May you not be tempted, " cls ". "
END-IF
	
IF cls = "Ranger" THEN
	DISPLAY "A life in the wilderness, " cnamef "?"
	DISPLAY "Hunting, tracking and sleeping under the stars, " cls ". "
END-IF
	
IF cls = "Rogue" THEN
	DISPLAY "A life theft and murder, " cnamef "?"
	DISPLAY "When you take life so lightly, you only have a short exciting life to look forward to, " cls ". "
END-IF
	
IF cls = "Sorcerer" THEN
	DISPLAY "The offspring of a magical creature, " cnamef "?"
	DISPLAY "Try not to blow yourself up, " cls ". "

END-IF
	
IF cls = "Warlock" THEN
	DISPLAY "Sold your soul, " cnamef "?"
	DISPLAY "Better not betray your master, " cls "! "

END-IF
	
IF cls = "Wizard" THEN
	DISPLAY "NEEEEEEERRRRRRRRD!!!! Are you a virgin " cnamef "?"
	DISPLAY "Guess you are not lonely enough in real life, " cls "!? "
END-IF
	

IF cls = "Bard" THEN
	DISPLAY "A Bard, want to lay dragons, slay them " cnamef "? "
	PERFORM UNTIL answer = "y" OR = "Y" OR = "n" OR = "N"
		DISPLAY "You are sure this is want?" WITH NO ADVANCING
		MOVE SPACE TO answer
		ACCEPT answer
	END-PERFORM.
		IF answer = "y" OR "Y"
		DISPLAY "If you are sure you are sure..."
		ELSE
			DISPLAY " "
		END-IF

DISPLAY "Oh... I almost forgot... What is your Race? "	
ACCEPT race
IF race = "Elf" OR "elf" THEN
	DISPLAY "Haughty and Proud..."
END-IF

IF race = "Human" OR "human" THEN
	DISPLAY "Because you are basic like that"
END-IF

IF race = "Dwarf" OR "dwarf" THEN
	DISPLAY "You need to find yourself a nice dwarven woman with a beard"
	DISPLAY	"YOU CAN GRAB ONTO!"
END-IF

IF race = "Halfling" OR "halfling" THEN
	DISPLAY "We had first breakfast, yes..."
	DISPLAY "But what about second breakfast?"
END-IF

IF race = "Tiefling" OR "tiefling" THEN
	DISPLAY "Probably a bard..."
END-IF

IF race = "Half-Elf" OR "half-elf" OR "halfelf" THEN
	DISPLAY "Hated by both..."
END-IF

IF race = "Dragonborn" OR "dragonborn" THEN
	DISPLAY "A truly terrifying creature..."
END-IF

IF race = "Aasimar" OR "aasimar" THEN
	DISPLAY "Kinda Avian..."
END-IF

IF race = "Kobold" OR "kobold" THEN
	DISPLAY "Can you even play them?"
END-IF

IF race = "Orc" OR "orc" THEN
	DISPLAY "Fantasy Klingons"
END-IF
DISPLAY "Now, how strong are you? " WITH NO ADVANCING
ACCEPT strenth
DISPLAY "Your Strength is " strenth ". What is your Dexterity? " WITH NO ADVANCING
ACCEPT dex
DISPLAY "Your Dexterity is " dex ". What is your Consitution? " WITH NO ADVANCING
ACCEPT con
DISPLAY "Your Constitution is " con ". What is your Wisdom? " WITH NO ADVANCING
ACCEPT wis
DISPLAY "Your Wisdom is " wis ". What is you Intelligence? " WITH NO ADVANCING
ACCEPT int
DISPLAY "Your Intelligence is " int ". What is you Charisma? " WITH NO ADVANCING
ACCEPT cha
DISPLAY "Your Charisma is " cha ". I think we have what we need"
DISPLAY pname
DISPLAY cname
DISPLAY race
DISPLAY cls
DISPLAY "stdxcowsinch"
DISPLAY abil
DISPLAY "Notice:  By having agreed to play Dungeons and Dragons,"
DISPLAY "you have already signed the hidden written agreement that"
DISPLAY "you will play your character to the absolute extreme of"
DISPLAY "that class's stereotype."
DISPLAY "Hey... I don't make the rules... I just enforce them!"
DISPLAY "BTW... Your soul now belongs to Kartavian... enjoy your game :)"

STOP RUN.
