import test
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
win=Tk()
win.geometry("800x500")
win.resizable(0,0)
db=test.Database('E:/database1.db')
#====================================
def insert():
    
    fname=ent_name.get()
    lname=ent_family.get()
    adress=ent_adres.get()
    phone=ent_phon.get()
    if fname=="" or lname=="" or adress==""or phone=="":
        messagebox.showerror('خطا','تمام فیلد ها وارد شود')
        return
    
    db.insert(fname, lname,adress, phone)
    clear()
    show()


def clear():
    ent_name.delete(0,END)
    ent_family.delete(0,END)
    ent_adres.delete(0,END)
    ent_phon.delete(0,END)
    ent_name.focus_set()


def show():
    lbl_list.delete(0,END)
    record=db.select()
    for rec in record:
     lbl_list.insert(END,rec) 

def select(event):
    global data
    clear()
    index=lbl_list.curselection()
    data=lbl_list.get(index)
    ent_name.insert(0,data[1])
    ent_family.insert(0,data[2])
    ent_adres.insert(0,data[3])
    ent_phon.insert(0,data[4])
 
def updat():
    
    fname=ent_name.get()
    lname=ent_family.get()
    adress=ent_adres.get()
    phone=ent_phon.get()
    global data
    db.updat(data[0],fname,lname,adress,phone)
    show()


def search():
    search_result=db.search(ent_search.get())
    lbl_list.delete(0, END)
    for row in search_result:
        lbl_list.insert(END, row)
    ent_search.delete(0,END)
def cancel():
    messagebox.showinfo("پیام","ایا اطمینان دارید")
    win.destroy()
    
    
    
def delete():
   messagebox.showinfo("پیام","ایا اطمینان دارید")
   db.delete(data[0])  
   clear()
   show()


#====================================
lbl_name=Label(win,text="name:",font='arial 18 bold')
lbl_name.place(x=20,y=20)

ent_name=Entry(win,font='arial 10 bold')
ent_name.place(x=100,y=25)

lbl_family=Label(win,text='family:',font='arial 18 bold')
lbl_family.place(x=250,y=20)

ent_family=Entry(win,font='arial 10 bold')
ent_family.place(x=340,y=25)

lbl_adres=Label(win,text='adres:',font='arial 18 bold')
lbl_adres.place(x=20,y=120)

ent_adres=Entry(win,font='arial 10 bold')
ent_adres.place(x=100,y=125)

lbl_phon=Label(win,text='phoon:',font='arial 18 bold')
lbl_phon.place(x=240,y=120)

ent_phon=Entry(win,font='arial 10 bold')
ent_phon.place(x=330,y=125)

lbl_serch=Label(win,text="search:",font='arial 16 bold')
lbl_serch.place(x=100,y=175)

ent_search=Entry(win,font='arial 10 bold')
ent_search.place(x=190,y=180)

lbl_list=Listbox(win,width=80,font='arial 12 bold')
lbl_list.place(x=50,y=230)

#====================================

btn_insert=Button(text="insert",font='arial 12 bold',width=7,command=insert)
btn_insert.place(x=520,y=30)

btn_delete=Button(text='delete',font='arial 12 bold',width=7,command=delete)
btn_delete.place(x=670,y=30)

btn_clear=Button(text="clear",font='arial 12 bold',width=7,command=clear)
btn_clear.place(x=520,y=100)

btn_update=Button(text='update',font='arial 12 bold',width=7,command=updat)
btn_update.place(x=670,y=100)

btn_show=Button(text="show",font='arial 12 bold',width=7,command=show)
btn_show.place(x=520,y=170)

btn_cancel=Button(text='cancel',font='arial 12 bold',width=7,command=cancel)
btn_cancel.place(x=670,y=170)

lbl_list.bind('<<ListboxSelect>>',select)










win.mainloop()