from googletrans import Translator
from tkinter import *

def translate_now(text1, text2, combo1, combo2):
    text = text1.get(1.0, END)
    t1 = Translator()
    
    src_lang = combo1.get()
    dest_lang = combo2.get()
    
    trans_text = t1.translate(text, src=src_lang, dest=dest_lang)
    trans_text = trans_text.text
    text2.delete(1.0, END)
    text2.insert(END, trans_text)
