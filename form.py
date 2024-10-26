from tkinter import *
from tkinter import ttk

root=Tk()
root.title("formulaire")
root.geometry("470x470")

#title
title=Label(root,text="Data Formulaire",font="Arial 20 bold")
title.grid(row=0, column=0, pady=10, padx=10, columnspan=4)

#first name
firstname_label=Label(root,text="First name")
firstname_label.grid(row=1,column=0, padx=10 ,sticky="w")

firstname_entry=Entry(root,width=40)
firstname_entry.grid(row=1,column=1,columnspan=2  ,sticky="ew")

#last name
lastname_label=Label(root,text="Last name")
lastname_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

lastname_entry=Entry(root,width=40)
lastname_entry.grid(row=2,column=1,columnspan=2 ,sticky="ew")

#birth date
birth_label=Label(root,text="birth date")
birth_label.grid(row=3,column=0,padx=10,sticky="w")

birth_entry=Entry(root,width=40)
birth_entry.grid(row=3,column=1,columnspan=2 ,pady=10 , sticky="ew")

#gender
gender=StringVar()
gender.set("none")

gender_label=Label(root, text="Gender")
gender_label.grid(row=4, column=0,padx=10,sticky="w")

male=Radiobutton(root, text="Male", variable=gender , value="male")
male.grid(row=4, column=1 , sticky="w")

female=Radiobutton(root, text="Female", variable=gender , value="female")
female.grid(row=4, column=2 , sticky="w")

#country
country_label=Label(root,text="Country")
country_label.grid(row=5,column=0, padx=10 ,pady=10 ,sticky="w")

country_choises=ttk.Combobox(root, width=40 , values=["morroco","french","egypt","usa","spain"])
country_choises.grid(row=5,column=1,columnspan=2  ,sticky="ew")

#adress
adress_label=Label(root,text="Adress")
adress_label.grid(row=6,column=0, padx=10 ,sticky="nw")

adress_entry=Text(root,width=40,height=5)
adress_entry.grid(row=6,column=1,columnspan=2  ,sticky="ew")

#buttons

def record():
    firstname=firstname_entry.get()
    lastname=lastname_entry.get()
    birthdate=birth_entry.get()
    gender_=gender.get()
    country=country_choises.get()
    adress=adress_entry.get("1.0","end-1c")
    text= firstname + ";" + lastname + ";" + birthdate + ";" + gender_ + ";" + country +  ";" + adress + "\n"

    with open(r"C:\Users\user\Desktop\PYTHON\POO\formPython\file_form.csv","a") as file:
        file.write(text)
    clear_all()



def clear_all():
    firstname_entry.delete(0,"end")
    lastname_entry.delete(0,"end")
    birth_entry.delete(0,"end")
    gender.set("none")
    country_choises.delete(0,"end")
    adress_entry.delete("1.0","end")
    firstname_entry.focus_set()
    



save=Button(root,text="Save", command=record)
save.grid(row=7 , column=1 , pady=10,padx=10,ipadx=10, sticky="e")

clear=Button(root,text="Clear", command=clear_all)
clear.grid(row=7 , column=2,pady=10,padx=10,ipadx=10, sticky="w")


root.mainloop()