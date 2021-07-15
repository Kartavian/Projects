		>>SOURCE FORMAT FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. calc.
AUTHOR. Loren Stevenson.
DATE-WRITTEN. July 15, 2021
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 Num1 PIC 9(2).
01 Num2 PIC 9(2).
01 Result PIC 9(4).

PROCEDURE DIVISION.

*> Request first number
DISPLAY "Choose first number: "
ACCEPT Num1

*> Request Second Number
DISPLAY "Choose second number: "
ACCEPT Num2

*> MULTIPLY numbers together
MULTIPLY Num1 BY Num2 GIVING Result
DISPLAY Num1 " Multiplied by " Num2 " Equals " Result

STOP RUN.
