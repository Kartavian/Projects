GCobol IDENTIFICATION DIVISION.
       PROGRAM-ID.    tclgui.
       AUTHOR. Rildo Pragana.
      *> REMARKS.
      *>    Example tcl/tk GUI program for Cobol.
      *>
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *>
       WORKING-STORAGE SECTION.
       01 DATA-BLOCK.
          05 NAME           PIC X(40).
          05 W-ADDRESS      PIC X(50).
          05 PHONE          PIC X(15).
          05 END-PGM                PIC X.
                05 QUICK-RET      PIC X.
       01 SITE-INFO.
          05  TITLE       PIC X(20).
          05  URL         PIC X(50).
       77 GUI-01          PIC X(64) VALUE "formA.tcl".
       77 GUI-02          PIC X(64) VALUE "formB.tcl".
       77 END-OF-STRING   pic X value LOW-VALUES.
       77 T-SCRIPT                  PIC X(128).
       77 T-RESULT                  PIC X(80).
       01 dummy                  pic X value X"00".

       PROCEDURE DIVISION.

       CALL "initTcl"

      *> test for stcleval function
       string "expr 12 * 34" END-OF-STRING into T-SCRIPT
       call "stcleval" using T-SCRIPT T-RESULT
       display "eval by tcl: |" T-SCRIPT "| returned " T-RESULT

       MOVE "Your name here" to NAME
       MOVE "Your address" TO W-ADDRESS
       MOVE "Phone number" to PHONE
      *> this variable tells Cobol that the user required an exit
       MOVE "0" to END-PGM
       MOVE "1" to QUICK-RET
       MOVE "Afonso Pena" to NAME
      *> now we may have the script name as a variable, terminated by a space
       CALL "tcleval" USING DATA-BLOCK "./formA.tcl "
       MOVE "Deodoro da Fonseca" to NAME
       CALL "tcleval" USING DATA-BLOCK GUI-01
       MOVE "Rui Barbosa" to NAME
       CALL "tcleval" USING DATA-BLOCK GUI-01
       MOVE "Frei Caneca" to NAME
       CALL "tcleval" USING DATA-BLOCK GUI-01

       MOVE "0" to QUICK-RET
       MOVE "Your name here" to NAME.
       100-restart.
      *> call C wrapper, passing data block and size of data
       CALL "tcleval" USING DATA-BLOCK GUI-01

       DISPLAY "Returned data:"
       DISPLAY "NAME    [" NAME "]"
       DISPLAY "ADDRESS [" W-ADDRESS "]"
       DISPLAY "PHONE   [" PHONE "]"
      *> if not end of program required, loop
       if END-PGM = 0
           go to 100-restart.
      *> to start a new GUI (graphical interface), call this first
       call "newGui"
       MOVE "Title of the site" to TITLE
       MOVE "URL (http://..., ftp://..., etc)" to URL
      *> now we may draw other main window...
       CALL "tcleval" USING SITE-INFO GUI-02
       DISPLAY "Returned data:"
       DISPLAY "TITLE   [" TITLE "]"
       DISPLAY "URL     [" URL "]"

       STOP RUN.