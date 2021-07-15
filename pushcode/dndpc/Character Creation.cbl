		>>SOURCE FORMAT FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. character_creation.
AUTHOR. Loren Stevenson
DATE-WRITTEN. July 8, 2021
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
	SELECT CharacterFile ASSIGN TO "character.dat"
		ORGANIZATION IS LINE SEQUENTIAL
		ACCESS IS SEQUENTIAL.
DATA DIVISION.
FILE SECTION.
FD CharacterFile.
01 CharacterData.
	02 pname.
		03 pnamef	PIC x(7).
		03 pnamel	PIC x(10).
	02 cname.
		03 cnamef	PIC x(10).
		03 cnamel	PIC x(12).
	
	02 cls PIC x(10).
	02 race PIC x(10).

	02 abil.
		03 strenth	PIC 9(2).
		03 dex	PIC 9(2).
		03 con	PIC 9(2).
		03 wis	PIC 9(2).
		03 intel PIC 9(2).
		03 cha	PIC 9(2).
		03 strmod PIC 9(2).
		03 dexmod PIC 9(2).
		03 conmod PIC 9(2).
		03 wismod PIC 9(2).
		03 intmod PIC 9(2).
		03 chamod PIC 9(2).
	
	02 answer PIC X.


WORKING-STORAGE SECTION.
01 WSCharacter.
	02 wspname.
		03 wspnamef	PIC x(7).
		03 wspnamel	PIC x(10).
	02 wscname.
		03 wscnamef	PIC x(10).
		03 wscnamel	PIC x(12).
	
	02 wscls PIC x(10).
	02 wsrace PIC x(10).

	02 wsabil.
		03 wsstrenth	PIC 9(2).
		03 wsdex	PIC 9(2).
		03 wscon	PIC 9(2).
		03 wswis	PIC 9(2).
		03 wsintel PIC 9(2).
		03 wscha	PIC 9(2).
		03 wsstrmod PIC 9(2).
		03 wsdexmod PIC 9(2).
		03 wsconmod PIC 9(2).
		03 wswismod PIC 9(2).
		03 wsintmod PIC 9(2).
		03 wschamod PIC 9(2).
	
	02 wsanswer PIC X.

PROCEDURE DIVISION.
OPEN OUTPUT CharacterFile.
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
	ACCEPT intel
	DISPLAY "Your Intelligence is " intel ". What is you Charisma? " WITH NO ADVANCING
	ACCEPT cha
	WRITE CharacterData
	END-WRITE.
CLOSE CharacterFile.
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
