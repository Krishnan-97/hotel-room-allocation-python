from tkinter import *
import pymysql

def ret():
    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='db')
    cur=conn.cursor()
    sql='select * from guest where room_no=(%s)'
    cur.execute(sql,(name_field.get()))
    for row in cur:
        print(row)
    cur.close()
    conn.close()

    
        

if __name__=='__main__':
    root=Tk()
    root.configure(background='grey')
    root.title('Info')
    root.geometry('300x150')

    heading=Label(root,text='Info',bg='grey')
    name=Label(root,text='Enter room no:',bg='grey')
    gap1=Label(root,bg='grey')
    gap2=Label(root,bg='grey')

    heading.grid(row=0,column=2)
    gap1.grid(row=1,column=2)
    name.grid(row=2,column=1)
    gap2.grid(row=3,column=2)

    name_field=Entry(root)
    name_field.grid(row=2,column=2,ipadx='10')

    enter=Button(root,text="Enter",bg='grey',command=lambda:ret())
    enter.grid(row=4,column=2)
    

    root.mainloop()
