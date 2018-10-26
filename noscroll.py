from tkinter import*
from tkinter import messagebox
import tkinter as tk
def raise_frame(frame):
    frame.tkraise()

top=Tk()

top.geometry('3500x2000')
top.title("WELCOME")
home=Frame(top)
pageone=Frame(top)
pagetwo=Frame(top)
pagethree=Frame(top)
for frame in(home,pageone,pagetwo,pagethree):
    frame.grid(row=0,column=0,sticky="news")

Label(home,text="Welcome to Faculty Feedback Form !",font=("Courier",44)).pack()
B=Button(home,text="CLICK NEXT ",width=25,command=lambda:raise_frame(pageone))
B.place(relx=0.5,rely=0.5, anchor=CENTER)
B.pack()



Label(pageone,text="PLEASE FILL THE FACULTY FEEDBACK BELOW",font=("Courier",22)).pack()
Label(pageone,text="Motivation provided \n \n",font=("courier",11)).pack(side="top")
def sel():
    selection=" You rated the faculty as " +str(v.get())
    label.config(text=selection)

v=tk.StringVar()
Radiobutton(pageone,text='Very Good',variable=v,value="VERY GOOD",command=sel).pack(anchor=tk.W)
Radiobutton(pageone,text='Good',variable=v,value="GOOD",command=sel).pack(anchor=tk.W)
Radiobutton(pageone,text='Average',variable=v,value="AVERAGE",command=sel).pack(anchor=tk.W)
Radiobutton(pageone,text='Poor',variable=v,value="POOR",command=sel).pack(anchor=tk.W)
Radiobutton(pageone,text='Very Poor',variable=v,value="VERY POOR",command=sel).pack(anchor=tk.W)

label=Label(pageone)
label.pack()
B=Button(pageone,text="CLICK NEXT ",width=25,command=lambda:raise_frame(pagetwo))
B.place(relx=0.5,rely=0.5, anchor=CENTER)
B.pack()

Label(pagetwo,text="PLEASE FILL THE FACULTY FEEDBACK BELOW",font=("Courier",22)).pack()
Label(pagetwo,text="Teacher's Communication skills \n \n",font=("courier",11)).pack()
def sel():
    selection=" You rated the faculty as " +str(v1.get())
    label.config(text=selection)

v1=tk.StringVar()
Radiobutton(pagetwo,text='Very Good',variable=v1,value="VERY GOOD",command=sel).pack(anchor=tk.W)
Radiobutton(pagetwo,text='Good',variable=v1,value="GOOD",command=sel).pack(anchor=tk.W)
Radiobutton(pagetwo,text='Average',variable=v1,value="AVERAGE",command=sel).pack(anchor=tk.W)
Radiobutton(pagetwo,text='Poor',variable=v1,value="POOR",command=sel).pack(anchor=tk.W)
Radiobutton(pagetwo,text='Very Poor',variable=v1,value="VERY POOR",command=sel).pack(anchor=tk.W)

label=Label(pagetwo)
label.pack()
B=Button(pagetwo,text="CLICK NEXT ",width=25,command=lambda:raise_frame(pagethree))
B.place(relx=0.5,rely=0.5, anchor=CENTER)
B.pack()

Label(pagethree,text="PLEASE FILL THE FACULTY FEEDBACK BELOW",font=("Courier",22)).pack()
Label(pagethree,text="Teacher's Regularity and Punctuality\n \n",font=("courier",11)).pack()
def sel():
    selection=" You rated the faculty as " +str(v3.get())
    label.config(text=selection)

v3=tk.StringVar()
Radiobutton(pagethree,text='Very Good',variable=v3,value="VERY GOOD",command=sel).pack(anchor=tk.W)
Radiobutton(pagethree,text='Good',variable=v3,value="GOOD",command=sel).pack(anchor=tk.W)
Radiobutton(pagethree,text='Average',variable=v3,value="AVERAGE",command=sel).pack(anchor=tk.W)
Radiobutton(pagethree,text='Poor',variable=v3,value="POOR",command=sel).pack(anchor=tk.W)
Radiobutton(pagethree,text='Very Poor',variable=v3,value="VERY POOR",command=sel).pack(anchor=tk.W)

label=Label(pagethree)
label.pack()
B=Button(pagethree,text="SUBMIT ",width=25,command=lambda:messagebox.showinfo("Submitted","Your feedback has been submitted !"))
B.place(relx=0.5,rely=0.5, anchor=CENTER)
B.pack()

raise_frame(home)

top.mainloop()


