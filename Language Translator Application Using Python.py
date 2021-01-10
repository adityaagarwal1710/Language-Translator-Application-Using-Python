from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
root=Tk()
root.title("Language Translator")
root.geometry("1030x500")
#root.maxsize(530,500)
#root.minsize(530,500)
photo = PhotoImage(file ="image.png")
Label(root,image = photo).place(x=430,y=60)
Label(root,text="Translator Application",font=('verdana',20,'bold','underline')).place(x=330,y=5)
a=tk.StringVar()
auto_detect=ttk.Combobox(root,width=40,textvariable=a,state='readonly',font=('verdana',10,'bold'),)
auto_detect['values']=('Auto Detect',)
auto_detect.place(x=30,y=70)
auto_detect.current(0)
l=tk.StringVar()
choose_language=ttk.Combobox(root,width=40,textvariable=l,state='readonly',font=('verdana',10,'bold'))
choose_language['values']=('Arabic','Armenian','history','Chinese (Simplified)','Chinese (Traditional)','Danish','Dutch','English','French','German','Gujarati','Hindi'
                           ,'Italian','Japanese','Kannada','Korean','Latin','Malayalam','Marathi','Punjabi','Russian','Urdu',)
choose_language.place(x=550,y=70)
choose_language.current(0)
t1=Text(root,width=45,height=20,borderwidth=5,relief=RIDGE)
t1.place(x=30,y=100)
t2=Text(root,width=45,height=20,borderwidth=5,relief=RIDGE)
t2.place(x=550,y=100)

def translate_button():
    language_1=t1.get("1.0","end-1c")
    print(language_1)
    cl=choose_language.get()
    if(language_1==""):
        messagebox.showerror('Language Translator',"You Can Not Leave The Text Field Empty")
    else:
        t2.delete(1.0,'end')
        translator=Translator(service_urls=['translate.googleapis.com'])
        output=translator.translate(language_1,dest=cl)
        t2.insert('end',output.text)
def clear():
    t1.delete(1.0,'end')
    t2.delete(1.0,'end')
tr=Button(root,text="Translate",relief=RIDGE,borderwidth=3,command=lambda:translate_button(),font=('verdana',10,'bold'))
tr.place(x=380,y=450)
clear_Button=Button(root,text="Clear",command=lambda:clear(),relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'))
clear_Button.place(x=500,y=450)
root.mainloop()




