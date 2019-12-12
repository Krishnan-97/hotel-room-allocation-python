from tkinter import *


def read(rmno):
    ch=rmno[0]
    
    if(ch=='D'):
        f=open('C:/Users/user/Desktop/D.txt','r+')
        l=f.readline()
        f.write('a')
        f.close()
        print('Checked out')
    if(ch=='G'):
        f=open('C:/Users/user/Desktop/G.txt','r+')
        l=f.readline()
        f.write('a')
        f.close()
        print('Checked out')
    if(ch=='FD'):
        f=open('C:/Users/user/Desktop/FD.txt','r+')
        l=f.readline()
        f.write('a')
        f.close()
        print('Checked out')
    if(ch=='J'):
        f=open('C:/Users/user/Desktop/J.txt','r+')
        l=f.readline()
        f.write('a')
        f.close()
        print('Checked out')
        
    
        



if __name__=='__main__':
    root=Tk()
    root.configure(background='grey')
    root.title('Check out')
    root.geometry('300x150')

    heading=Label(root,text='Check Out',bg='grey')
    name=Label(root,text='Enter Room no:',bg='grey')
    gap1=Label(root,bg='grey')
    gap2=Label(root,bg='grey')
    

    heading.grid(row=0,column=2)
    gap1.grid(row=1,column=2)
    name.grid(row=2,column=1)
    gap2.grid(row=3,column=2)
    

    name_field=Entry(root)
    name_field.grid(row=2,column=2,ipadx='10')
    

    enter=Button(root,text="Enter",bg='grey',command=lambda:read(name_field.get()))
    enter.grid(row=4,column=2)
    

    root.mainloop()
