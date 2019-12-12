from tkinter import *
from subprocess import call


if __name__=='__main__':
    root=Tk()
    root.configure(background='grey')
    root.title('Registration')
    root.geometry('150x250')

    
    gap1=Label(root,bg='grey')
    gap2=Label(root,bg='grey')
    heading=Label(root,text='Hotel Front Desk',bg='grey')
    gap3=Label(root,bg='grey')
    gap4=Label(root,bg='grey')
    

    heading.grid(row=0,column=2)
    gap1.grid(row=1,column=2)
    
    gap2.grid(row=3,column=2)
    gap3.grid(row=5,column=2)
    gap4.grid(row=7,column=2)
    

    chin=Button(root,text="Check In",bg='grey',command=lambda:call(['python','Entry.py']))
    chin.grid(row=2,column=2)
    chot=Button(root,text="Check Out",bg='grey',command=lambda:call(['python','chek_out.py']))
    chot.grid(row=4,column=2)
    info=Button(root,text="Info",bg='grey',command=lambda:call(['python','info.py']))
    info.grid(row=8,column=2)
    ext=Button(root,text="Exit",bg='grey',command=lambda:root.quit)
    ext.grid(row=6,column=2)
    

    root.mainloop()
