from tkinter import ttk
from googletrans import LANGUAGES
from tkinter import *

def setup_interface(root, translate_now, label_change):

    language_names = list(LANGUAGES.values())

    combo1 = ttk.Combobox(root, values=language_names, font="Roboto 14", state="readonly")
    combo1.place(x=110, y=20)
    combo1.set("English")

    label1 = Label(root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
    label1.place(x=10, y=50)

    combo2 = ttk.Combobox(root, values=language_names, font="Roboto 14", state="readonly")
    combo2.place(x=730, y=20)
    combo2.set("Spanish")

    label2 = Label(root, text="Spanish", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
    label2.place(x=620, y=50)

    frame = Frame(root, bg="Black", bd=10)
    frame.place(x=10, y=118, width=440, height=210)

    text1 = Text(frame, font="Roboto 20", bg="white", relief=RAISED, wrap=WORD, bd=20)
    text1.place(x=0, y=0, width=430, height=200)

    scrollbar1 = Scrollbar(frame)
    scrollbar1.pack(side="right", fill="y")

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)

    frame1 = Frame(root, bg="Black", bd=10)
    frame1.place(x=620, y=118, width=440, height=210)

    text2 = Text(frame1, font="Roboto 20", bg="white", relief=RAISED, wrap=WORD, bd=20)
    text2.place(x=0, y=0, width=430, height=200)

    scrollbar2 = Scrollbar(frame1)
    scrollbar2.pack(side="right", fill="y")

    scrollbar2.configure(command=text2.yview)
    text2.configure(yscrollcommand=scrollbar2.set)

    translate = Button(root, text="Translate", font=("Roboto", 15), cursor="hand2", 
                       bd=5, width=10, height=2, bg="black", fg="white", 
                       command=lambda: translate_now(text1, text2, combo1, combo2))

    translate.place(x=476, y=250)

    label_change(combo1, combo2, label1, label2, root)