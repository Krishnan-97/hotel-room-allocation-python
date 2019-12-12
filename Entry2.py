
import Entry
def room_alloc(typp,dys):
    
    if typp=='Deluxe':
        f=open('C:/Users/user/Desktop/D.txt','r+')
        l=f.readline()
        a=[]
        st=''
        stt=''
        for i in range(len(l)):
            a.append(l[i])
        if 'a' in a:
            for k in a:
                stt=stt+k
            b=a.pop()
            for j in a:
                st=st+j
            q='D '+stt
            print('Room Allocated')
            print('Amount Raised:',(int(dys)*3000))
            print('Room No:','D '+stt)
            
        else:
            print('Room unavailable')
        f.truncate(0)
        f.seek(0)
        
        f.write(st)
        f.close()

    elif typp=='General':
        f=open('C:/Users/user/Desktop/G.txt','r+')
        l=f.readline()
        a=[]
        st=''
        stt=''
        for i in range(len(l)):
            a.append(l[i])
        if 'a' in a:
            for k in a:
                stt=stt+k
            b=a.pop()
            for j in a:
                st=st+j
            q='G '+stt
            print('Room Allocated')
            print('Amount Raised:',(int(dys)*1500))
            print('G '+stt)
            #Entry.insert(q)
        else:
            print('Room unavailable')
        f.truncate(0)
        f.seek(0)
        
        f.write(st)
        f.close()

    elif typp=='Full Deluxe':
        f=open('C:/Users/user/Desktop/FD.txt','r+')
        l=f.readline()
        a=[]
        st=''
        stt=''
        for i in range(len(l)):
            a.append(l[i])
        if 'a' in a:
            for k in a:
                stt=stt+k
            b=a.pop()
            for j in a:
                st=st+j
            q='FD '+stt
            print('Room Allocated')
            print('Amount Raised:',(int(dys)*4000))
            print('FD '+stt)
            #Entry.insert(q)
        else:
            print('Room unavailable')
        f.truncate(0)
        f.seek(0)
        
        f.write(st)
        f.close()

    elif typp=='Joint':
        f=open('C:/Users/user/Desktop/J.txt','r+')
        l=f.readline()
        a=[]
        st=''
        stt=''
        for i in range(len(l)):
            a.append(l[i])
        if 'a' in a:
            for k in a:
                stt=stt+k
            b=a.pop()
            for j in a:
                st=st+j
            q='J '+stt
            print('Room Allocated')
            print('Amount Raised:',(int(dys)*5000))
            print('J '+stt)
            #Entry.insert(q)
        else:
            print('Room unavailable')
        f.truncate(0)
        f.seek(0)
        
        f.write(st)
        f.close()


    
