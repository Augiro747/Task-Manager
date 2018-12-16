from tkinter import * 
import os
import time
def loading():#this function clears text windows and fills listbox
    listbox1.delete(0,'end')
    if os.path.exists(os.path.join(".","Plan.txt")):
        f=open("Plan.txt")
        s=f.read()
        while s!='':
            s1=s[0:s.find(";")]
            s=s[s.find(";")+1:len(s)]
            listbox1.insert(END,s1[0:17])
            listbox1.pack(side=LEFT,padx=15) 
        f.close()
    text1.delete(1.0, END)
    text2.delete(1.0, END)
    text3.delete(1.0, END)

def note(l):#this function used for showing in console what we have at file in the end of work
    k=[]
    while l!='':
        s1=l[0:l.find(";")]
        l=l[l.find(";")+1:len(l)]
        k.append(s1)
    return k

def button_zadacha():#function that load inputed data in file
    if os.path.exists(os.path.join(".","Plan.txt")):
        f=open("Plan.txt",'a')
        x=text1.get('1.0','end')
        y=text2.get('1.0','end')
        z=text3.get('1.0','end')
        f.write(y[0:len(y)-1]+' '+z[0:len(z)-1]+' '+x+';')
        f.close()
    else:
        f=open("Plan.txt",'w')
        x=text1.get('1.0','end')
        y=text2.get('1.0','end')
        z=text3.get('1.0','end')
        f.write(y[0:len(y)-1]+' '+z[0:len(z)-1]+' '+x+';')
        f.close()
    loading()

def timenow():#time function used for clocks
    label.after(200, timenow)
    label['text']=time.strftime('%H:%M:%S\n%A')

def button_delete(): #function that delete choosen data in file
        f=open("Plan.txt")
        s=f.read()
        x=s.find(listbox1.get(listbox1.curselection()))
        f.close()
        s=s[0:x]+s[x+s[x:len(s)].find(';')+1:len(s)]
        f=open("Plan.txt",'w')
        f.write(s)
        f.close()
        loading()

def button_show():#function that choose note with data taked from listbox
    f=open("Plan.txt")
    s=f.read()
    x=s.find(listbox1.get(listbox1.curselection()))
    text1.delete(1.0, END)
    text2.delete(1.0, END)
    text3.delete(1.0, END)
    text1.insert(END,s[x+18:x+s[x:len(s)].find(';')])
    text2.insert(END,s[x:x+8])
    text3.insert(END,s[x+9:x+17])
    f.close()

root = Tk() 
root.title("Задачник ") 
root.geometry('800x440+300+200') 
root.minsize(width="800",height="440") 
root.maxsize(width="800",height="440") 
text1=Text(root,height=14,width=57,font='Arial 14',wrap=WORD ) #inputed by user notes
text1.pack() 

text2=Text(root,height=1,width=8,font='Arial 14',wrap=WORD)#inputed by user data
text2.pack(side=LEFT)

text3=Text(root,height=1,width=8,font='Arial 14',wrap=WORD)#inputed by user time
text3.pack(side=LEFT)

button1 = Button(root, text="Создание задачи", command=button_zadacha) 
button1.pack(side=LEFT ,padx=2.5) 

button2 = Button(root, text="Удаление", command=button_delete,) 
button2.pack( side=LEFT,padx=2.5) 

button3 = Button(root, text="Показать задачу", command=button_show) 
button3.pack( side=LEFT,padx=2.5) 

label=Label(root,text=time.strftime('%H:%M:%S'),bg='grey',height=2,width=10)
label.pack( side=LEFT,padx=2.5)
label.after_idle(timenow)

listbox1=Listbox(root,height=4,width=29,borderwidth=5,selectmode=SINGLE) 
listbox1.pack(side=RIGHT)
loading()
text1.insert(END,'Input your note here')
text2.insert(END,'dd.mm.yy')
text3.insert(END,'hh:mm:ss')

root.mainloop()


f=open("Plan.txt")
line=f.read()
print (note(line))
f.close()
