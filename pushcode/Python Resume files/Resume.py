    # open window with 3 buttons
from tkinter import *

main = Tk()
main.title("Hire The Man!")
main.iconbitmap('E:/Python/Python Projects/face.ico')
main.geometry("750x600")
main.configure(bg='purple')
def cobClick():
    cob = Tk()
    cob.title("Source Code in COBOL")
    cob.iconbitmap('E:/Python/Python Projects/face.ico')
    cob.geometry("800x600")
    cob.configure(bg="lavender")
    myLabel = Label(cob, text="COBOL")
    myLabel.pack()
    myLabel.configure(bg='violet')
    file = open("E:\\Python\\Python Projects\\COBOLtut.txt", "r")

def cplusClick():
    cplus = Tk()
    cplus.title("Source Code in C++")
    cplus.iconbitmap('E:/Python/Python Projects/face.ico')
    cplus.geometry("800x600")
    cplus.configure(bg="lavender")
    myLabel = Label(cplus, text="C++")
    myLabel.pack()
def pyClick():
    py = Tk()
    py.title("Source Code in Python")
    py.iconbitmap('E:/Python/Python Projects/face.ico')
    py.geometry("800x600")
    py.configure(bg="pink")
    myLabel = Label(py, text="This is the Source Code for this Program in Python")
    myLabel.pack()
def resClick():
    res = Tk()
    res.title("My Resume")
    res.iconbitmap('E:/Python/Python Projects/face.ico')
    res.geometry("800x600")
    res.configure(bg="purple")
def aboutClick():
    about = Tk()
    about.title("Loren Alexander Stevenson")
    about.iconbitmap('E:/Python/Python Projects/face.ico')
    about.geometry("800x600")
    about.configure(bg="purple")

myLabel = Label(main, text="Hire Loren!")
myLabel.grid(row=0, column=1)
myLabel.configure(bg='purple')
        # 1 button with "COBOL"
cobol_img = PhotoImage(file="E:/Python/Python Projects/COBOL.png")

cobol_btn = Button(main, image=cobol_img, command=cobClick)
cobol_btn.grid(row=1, column=0)
cobol_btn.configure(width=200, height=100)

            # selecting Opens new window with Source Code for this program in COBOL
            # Button to save SC to COBOL.txt
        # 2 button with "C++"
cplus_img = PhotoImage(file="E:/Python/Python Projects/C++.png")

cplus_btn = Button(main, image=cplus_img, command=cplusClick)
cplus_btn.grid(row=2, column=1)
cplus_btn.configure(width=100, height=100)
            # selecting Opens new window with Source Code for this program in C++
            # Button to save SC to Cplus.txt
        #3 button with "Python"
py_img = PhotoImage(file="E:/Python/Python Projects/Python.png")

py_btn = Button(main, image=py_img, command=pyClick)
py_btn.grid(row=1, column=2)
py_btn.configure(width=200, height=119)
            # selecting opens ne window with Source Code for this prgoram in Python
midLabel = Label(main, text="These are examples of what I can program,")
midLabel.grid(row=4, column=1)

midLabel2 = Label(main, text="I am hoping to use this as an example of my creativity")
midLabel2.grid(row=5, column=1)

midLabel3 = Label(main, text="Below is my resume and the Test Programs used during coding")
midLabel3.grid(row=6, column=1)

res = Button(main, text="My Resume", command=resClick)
res.grid(row=7, column=0)
res.configure(fg="lime")
res.configure(bg="violet")

about = Button(main, text="About Me", command=aboutClick)
about.grid(row=7, column=2)
about.configure(fg="lime", bg="blue")

# I am hoping to use this as an example of my creativity
main.mainloop()