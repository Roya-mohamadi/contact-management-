from tkinter import *
from tkinter import  messagebox
import databas
db=databas("e:/cantact/mysql.db")

win=Tk()
win.geometry("800x600")
win.title("MY CANTACT")
win.configure(background="#856d8d")
win.resizable(0,0)
#_____________fun
def exit():
    result=messagebox.askokcancel("ERORE","are you sure to exit?")
    if result=="yes":
        databas.con.close()
        win.destroy()
    return
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_phon.delete(0,END)
    ent_adres.delete(0,END)
    ent_srech.delete(0,END)

def insert():
    if ent_fname=="" or ent_lname=="" or ent_phon=="" or ent_adres=="" or ent_srech=="":
        messagebox.showerror("ERORE","fild are empty")
        return
    databas.insert




















#_____________weg

lbl_name=Label(win,text="fname",font="ariyal 20 bold",width=10)
lbl_name.place(x=50,y=50)

lbl_lame=Label(win,text="lname",font="ariyal 20 bold",width=10)
lbl_lame.place(x=50,y=100)

lbl_phon=Label(win,text="phon",font="ariyal 20 bold",width=10)
lbl_phon.place(x=50,y=150)

lbl_adres=Label(win,text="adress",font="ariyal 20 bold",width=10)
lbl_adres.place(x=50,y=200)

ent_fname=Entry(win,font="ariyal 20 bold",width=15)
ent_fname.place(x=250,y=50)

ent_lname=Entry(win,font="ariyal 20 bold",width=15)
ent_lname.place(x=250,y=100)

ent_phon=Entry(win,font="ariyal 20 bold",width=15)
ent_phon.place(x=250,y=150)

ent_adres=Entry(win,font="ariyal 20 bold",width=15)
ent_adres.place(x=250,y=200)

ent_srech=Entry(win,font="ariyal 20 bold",width=15)
ent_srech.place(x=250,y=250)

btn_insert=Button(win,text="insert",font="ariyal 20 bold",width=5)
btn_insert.place(x=50,y=400)

btn_updata=Button(win,text="updata",font="ariyal 20 bold",width=5)
btn_updata.place(x=160,y=400)

btn_delete=Button(win,text="delete",font="ariyal 20 bold",width=5)
btn_delete.place(x=270,y=400)

btn_clear=Button(win,text="clear",font="ariyal 20 bold",width=5,command=clear)
btn_clear.place(x=380,y=400)

btn_exit=Button(win,text="exit",font="ariyal 20 bold",width=40,command=exit)
btn_exit.place(x=50,y=500)

btn_shoelist=Button(win,text="showlistbox",font="ariyal 20 bold",width=13)
btn_shoelist.place(x=500,y=400)

btn_srech=Button(win,text="srech in\nlistbox",font="ariyal 20 bold",width=10)
btn_srech.place(x=50,y=250)

lst_box=Listbox(win,width=38,height=20)
lst_box.place(x=500,y=50)




win.mainloop()
