from tkinter import *
import os.path
from tkinter import filedialog
from tkinter import messagebox
from turtle import width
from PIL import Image
import pytesseract
w=Tk()
#C:\Program Files (x86)\Tesseract-OCR
w.geometry('560x450')
w.title("from image to text app")
w.resizable(False,False)


def first():
    file=filedialog.askopenfile(mode='r',filetypes=[('PNG Files','*.png')])
    if file:
        filepath=os.path.abspath(file.name)
        e1.insert(0,filepath)
def sacend():
    pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    save=e2.get()
    file=e1.get()
    lang=e3.get()
    img=Image.open(file)
    text=pytesseract.image_to_string(img)
    with open(save,"w") as f:
        f.write(text)
    messagebox.showinfo("Done","I hope it makes you right")
     
f1=Frame(w,width=600,height=368,bg='black',bd=1)
f1.place(x=1,y=1)

text=Label(f1,text="PROGRAM : image to text ",font=("Asial",16))
text.place(x=1,y=4)

e1_text=Label(f1,text="image path : ",fg="white",bg="black",font=("Asial",13))
e1_text.place(x=10,y=51)


e1=Entry(f1,font=("Asial",16),width=30,bd=1)
e1.place(x=110,y=50)

b1=Button(f1,text="+",cursor="hand2",command=first)
b1.place(x=455,y=51)



e2_text=Label(f1,text="Save path : ",fg="white",bg="black",font=("Asial",13))
e2_text.place(x=10,y=100)


e2=Entry(f1,font=("Asial",16),width=30,bd=1)
e2.place(x=110,y=100)

e3_text=Label(f1,text="language : ",fg="white",bg="black",font=("Asial",13))
e3_text.place(x=10,y=150)


e3=Entry(f1,font=("Asial",16),width=30,bd=1)
e3.place(x=110,y=150)


b2=Button(f1,text="Convert",width=10,height=6,fg="white",bg="gold",command=sacend)
b2.place(x=480,y=49)

logo=PhotoImage(file="please2.png")
logo_label=Label(w,image=logo)
logo_label.place(x=1,y=200,width=560,height=250)
w.mainloop()