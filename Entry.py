from tkinter import *
import pymysql
import Entry2




def clear():
    name_field.delete(0,END)
    address_field.delete(0,END)
    number_field.delete(0,END)
    days_field.delete(0,END)

def insert():
    if(name_field.get()=='' and
       address_field.get()=='' and
       number_field.get()=='' and
       days_field.get()==''):
        print('Empty Input')

    else:

        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='db')
        cur=conn.cursor()
        sql='insert into guest values (%s,%s,%s,%s,%s,%s,%s)'
        
        cur.execute(sql,(name_field.get(),address_field.get(),number_field.get(),int(days_field.get()),Lb1.get(ACTIVE),Lb2.get(ACTIVE),rmno_field.get()))
        conn.commit()
        clear()
        print('Details Entered')
        
        cur.close()
        conn.close()
        
        
        
        
        

        

def focus1(event):
    name_field.focus_set()

def focus2(event):
    address_field.focus_set()

def focus3(event):
    number_field.focus_set()

def focus4(event):
    days_field.focus_set()

if __name__=='__main__':
    root=Tk()
    root.configure(background='grey')
    root.title('check in')
    root.geometry('500x400')

    

    heading=Label(root,text='Check In',bg='grey')
    name=Label(root,text='Enter Name:',bg='grey')
    address=Label(root,text='Enter Address:',bg='grey')
    number=Label(root,text='Enter mob number:',bg='grey')
    days=Label(root,text='Enter Duration:',bg='grey')
    typ=Label(root,text='Room Type',bg='grey')
    payment=Label(root,text='Payment Method',bg='grey')
    rm_no=Label(root,text='Room no',bg='grey')
    blk1=Label(root,bg='grey')
    blk2=Label(root,bg='grey')
    blk3=Label(root,bg='grey')

    heading.grid(row=0,column=2)
    name.grid(row=1,column=1)
    address.grid(row=2,column=1)
    number.grid(row=3,column=1)
    days.grid(row=4,column=1)
    blk1.grid(row=5,column=1)
    typ.grid(row=6,column=1)
    blk2.grid(row=7,column=1)
    payment.grid(row=8,column=1)
    blk3.grid(row=9,column=1)
    rm_no.grid(row=11,column=1)

    name_field=Entry(root)
    address_field=Entry(root)
    number_field=Entry(root)
    days_field=Entry(root)
    rmno_field=Entry(root)

    name_field.bind('<Return>',focus1)
    address_field.bind('<Return>',focus2)
    number_field.bind('<Return>',focus3)
    days_field.bind('<Return>',focus4)

    name_field.grid(row=1,column=2,ipadx='100')
    address_field.grid(row=2,column=2,ipadx='100')
    number_field.grid(row=3,column=2,ipadx='100')
    days_field.grid(row=4,column=2,ipadx='100')
    rmno_field.grid(row=11,column=2,ipadx='10')

    Lb1=Listbox(root,height=4,width=53)
    Lb1.insert(1,'Deluxe')
    Lb1.insert(2,'General')
    Lb1.insert(3,'Full Deluxe')
    Lb1.insert(4,'Joint')
    Lb1.grid(row=6,column=2)

    Lb2=Listbox(root,height=2,width=53)
    Lb2.insert(1,'Cash')
    Lb2.insert(2,'Card')
    Lb2.grid(row=8,column=2)

    

    enter=Button(root,text="Enter",bg='grey',command=insert)
    enter.grid(row=10,column=2)
    enter1=Button(root,text="Check room",bg='grey',command=lambda:Entry2.room_alloc(Lb1.get(ACTIVE),days_field.get()))
    enter1.grid(row=10,column=1)

    

    root.mainloop()
    
    
