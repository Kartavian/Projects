		>>Source Format FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. COBOLtut.
AUTHOR. Loren Stevenson
DATE-WRITTEN. June 18th, 2021
ENVIRONMENT DIVISION.
		
DATA DIVISION.
FILE SECTION.
WORKING-STORAGE SECTION.
01 result	USAGE BINARY-LONG.
01 gtk-window	USAGE POINTER.
01 gtk-box	USAGE POINTER.
01 gtk-hello	USAGE POINTER.
01 gtk-textentry	USAGE POINTER.
01 gtk-goodbye	USAGE POINTER.
01 callback	USAGE PROCEDURE-POINTER.
01 params	USAGE POINTER.
01 UserName PIC X(30) VALUE "You".
01 Num1	PIC 999 VALUE ZEROS.
01 Num2 PIC 999 VALUE ZEROS.
01 Total PIC 9999 VALUE 0.

01 PIValue CONSTANT AS 3.14.

PROCEDURE DIVISION.
CALL "CBL_OC_INIT_CHECK" RETURNING result END-CALL
	DISPLAY "init: " result END-DISPLAY
	
CALL "CBL_OC_GTK_WINDOW_NEW" RETURNING gtk-window END-CALL
	DISPLAY "win: " gtk-window END-DISPLAY
CALL "CBL_OC_GTK_WIDGET_SET_TITLE"
	USING BY VALUE gtk-window
		BY REFERENCE "GnuCOBOL GTK+"
END-CALL
	DISPLAY "title: " gtk-window END-DISPLAY
CALL "CBL_OC_GTK_CONTAINER_SET_BORDER_WIDTH"
	USING BY VALUE gtk-window
		BY VALUE 5
END-CALL
	DISPLAY "border: " gtk-window END-DISPLAY
*> connect a window destroy, quit main loop handler
set callback to entry "CBL_OC_destroy"
CALL "CBL_OC_G_SIGNAL_CONNECT"
	using by value gtk-window
		by reference "delete_event" & x"00"
        by value callback
        by value params
END-CALL

      *> Create a vertically packed box
CALL "CBL_OC_GTK_VBOX_NEW"
	using by value 0
		by value 5
    returning gtk-box
END-CALL
	display "box: " gtk-box end-display

      *> Add the box to the window
CALL "CBL_OC_GTK_CONTAINER_ADD"
	using by value gtk-window
		by value gtk-box
END-CALL

      *> Create the hello button
CALL "CBL_OC_GTK_BUTTON_NEW_WITH_LABEL"
	using by reference "Hello from GnuCOBOL and GTK" & x"00"
		returning gtk-hello
END-CALL
	display "button: " gtk-hello end-display

      *> Connect the hello button to the hello code
	set callback to entry "CBL_OC_hello"
CALL "CBL_OC_G_SIGNAL_CONNECT"
       using by value gtk-hello
            by reference "clicked" & x"00"
			by value callback
            by value params
END-CALL

      *> Pack the button into the box, top to bottom
CALL "CBL_OC_GTK_BOX_PACK_START"
	using by value gtk-box
		by value gtk-hello
        by value 1
        by value 1
        by value 0
END-CALL

      *> button is ready to show
CALL "CBL_OC_GTK_WIDGET_SHOW"
	using by value gtk-hello
END-CALL

      *> Add a text entry field
CALL "CBL_OC_GTK_ENTRY_NEW"
	returning gtk-textentry
END-CALL

      *> Connect code to the text entry, passing the entry widget
set callback to entry "CBL_OC_activate"
CALL "CBL_OC_G_SIGNAL_CONNECT"
	using by value gtk-textentry
		by reference "activate" & x"00"
        by value callback
        by value gtk-textentry
END-CALL

      *> Pack the text field into the box, top to bottom
CALL "CBL_OC_GTK_BOX_PACK_START"
	using by value gtk-box
		by value gtk-textentry
        by value 1
		by value 1
        by value 0
END-CALL

      *> text field is ready to show
CALL "CBL_OC_GTK_WIDGET_SHOW"
	using by value gtk-textentry
END-CALL

      *> Create the bye button
CALL "CBL_OC_GTK_BUTTON_NEW_WITH_LABEL"
	using by reference "Goodbye from GnuCOBOL and GTK" & x"00"
		returning gtk-goodbye
END-CALL
	display "button: " gtk-goodbye end-display

      *> Connect the bye button to the bye code
set callback to entry "CBL_OC_destroy"
CALL "CBL_OC_G_SIGNAL_CONNECT"
	using by value gtk-goodbye
    by reference "clicked" & x"00"
    by value callback
    by value params
END-CALL

      *> Pack the button into the box, under hello
CALL "CBL_OC_GTK_BOX_PACK_START"
	using by value gtk-box
		by value gtk-goodbye
        by value 1
        by value 1
        by value 0
END-CALL
	display "pack: " gtk-box end-display

      *> button is ready to show
CALL "CBL_OC_GTK_WIDGET_SHOW"
	using by value gtk-goodbye
END-CALL

      *> box is ready to show
CALL "CBL_OC_GTK_WIDGET_SHOW"
	using by value gtk-box
END-CALL

      *> window is ready to show
CALL "CBL_OC_GTK_WIDGET_SHOW"
    using by value gtk-window
END-CALL

      *> Start up the event loop, control returned when GTK main exits
CALL "CBL_OC_GTK_MAIN" END-CALL

      *> Something terminated the GTK main loop, sys-close or bye or
display "ending..." end-display

goback.
end program COBOLtut.
