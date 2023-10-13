from tkinter import *
from src.translator import translate_now
from src.interfaz import setup_interface

def label_change(combo1, combo2, label1, label2, root):
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change, combo1, combo2, label1, label2, root)


if __name__ == "__main__":
    root = Tk()
    root.title("Translator")
    root.geometry("1080x400")
    root.resizable(False, False)
    root.configure(background="white")

    arrow_image = PhotoImage(file="img/arrow.png")
    image_label = Label(root, image=arrow_image, width=150)
    image_label.place(x=460, y=110)

    image_icon = PhotoImage(file="img/icono.png")
    root.iconphoto(False, image_icon)

    setup_interface(root, translate_now, label_change)
    root.mainloop()