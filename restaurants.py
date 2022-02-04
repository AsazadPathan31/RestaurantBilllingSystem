#---------------------------------------------------------- Restaurant Billing System ------------------------------------------------------------

from tkinter import *

from tkinter import messagebox

import rbadata

root=Tk()

root.title("Restaurants Billing")

root.geometry("1400x900")

topframe=Frame(root,bg="#47376b",width=1400,height=20,borderwidth=4,relief="solid")

topframe.pack(side=TOP,expand=True,fill="both")

leftframe=Frame(root,width=700,height=680,borderwidth=4,relief="solid",bg="#f7d7cb")

leftframe.pack(side=LEFT,expand=True,fill="both")

rightframe=Frame(root,width=700,height=630,borderwidth=4,relief="solid",bg="#a7e8cd")

rightframe.pack(side=LEFT,expand=True,fill="both")
         

#->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->-> Functions ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->


def exitt():
    
    res=messagebox.askquestion(message="Would You Like To Exit")
    
    if(res=="yes"):
        
        root.destroy()
        

def resett():
    
    ord.set("")
    
    fri.set("")
    
    bur.set("")
    
    dri.set("")
    
    piz.set("")
    
    sub.set("")
    
    tax.set("")
    
    ser.set("")
    
    tot.set("")

def tottal():
    frie=int(fri.get())
    
    burg=int(bur.get())
    
    drin=int(dri.get())
    
    pizz=int(piz.get())
    
    
    #cost Assign per Item
    
    onefr=frie*60
    
    onebu=burg*80
    
    onedr=drin*40
    
    onepi=pizz*90
    
    subtotal=onefr+onebu+onedr+onepi
    
    taxx=(onefr+onebu+onedr+onepi)*0.18
    
    serv=(onefr+onebu+onedr+onepi)/99
    
    sub.set(str(subtotal))
    
    tax.set(str(taxx))
    
    ser.set(str(serv))
    
    tot.set(str(subtotal+taxx+serv))
    
    
    
#=================================================================== Conversion ============================================================
    

ord=StringVar()

fri=StringVar()

bur=StringVar()

dri=StringVar()

piz=StringVar()

sub=StringVar()

tax=StringVar()

ser=StringVar()

tot=StringVar()


# --------------------------------------------------------- labeling ------------------------------------------------------------------------

lbtitle=Label(topframe,text="RESTAURANTS BILLING SYSTEM",bg="#47376b",fg="#d47161",font=("arial",35,"bold")).pack()


lbor=Label(leftframe,text="Order Number",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lbor.grid(row=0,column=0)
enor=Entry(leftframe,font=("arial",16,"bold"),textvariable=ord,bg="#dfebe0",bd=5)
enor.grid(row=0,column=1,padx=20,pady=20,sticky=W)

lb1=Label(leftframe,text="Fries",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb1.grid(row=1,column=0)
en1=Entry(leftframe,font=("arial",16,"bold"),textvariable=fri,bg="#dfebe0",bd=5)
en1.grid(row=1,column=1,padx=20,pady=20,sticky=W)

lb2=Label(leftframe,text="Burger",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb2.grid(row=2,column=0)
en2=Entry(leftframe,font=("arial",16,"bold"),textvariable=bur,bg="#dfebe0",bd=5)
en2.grid(row=2,column=1,padx=20,pady=20,sticky=W)

lb3=Label(leftframe,text="Drinks",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb3.grid(row=3,column=0)
en3=Entry(leftframe,font=("arial",16,"bold"),textvariable=dri,bg="#dfebe0",bd=5)
en3.grid(row=3,column=1,padx=20,pady=20,sticky=W)

lb4=Label(leftframe,text="Pizza",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb4.grid(row=4,column=0)
en4=Entry(leftframe,font=("arial",16,"bold"),bg="#dfebe0",bd=5,textvariable=piz)
en4.grid(row=4,column=1,padx=20,pady=20,sticky=W)


lb6=Label(leftframe,text="Sub Total",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb6.grid(row=6,column=0)
en6=Entry(leftframe,font=("arial",16,"bold"),bg="#dfebe0",bd=5,textvariable=sub)
en6.grid(row=6,column=1,padx=20,pady=20,sticky=W)

lb7=Label(leftframe,text="Tax",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb7.grid(row=7,column=0)

en7=Entry(leftframe,font=("arial",16,"bold"),bg="#dfebe0",bd=5,textvariable=tax)
en7.grid(row=7,column=1,padx=20,pady=20,sticky=W)

lb8=Label(leftframe,text="Service",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb8.grid(row=8,column=0)

en8=Entry(leftframe,font=("arial",16,"bold"),bg="#dfebe0",bd=5,textvariable=ser)
en8.grid(row=8,column=1,padx=20,pady=20,sticky=W)

lb9=Label(leftframe,text="Total",font=("arial",18,"bold"),fg="#4673bd",bg="#f7d7cb")
lb9.grid(row=9,column=0)

en9=Entry(leftframe,font=("arial",16,"bold"),bg="#dfebe0",bd=5,textvariable=tot)
en9.grid(row=9,column=1,padx=20,pady=20,sticky=W)

#btntotal
btntotal = Button(leftframe,padx=2,pady=2,bd=10,font=("roboto",20,"bold"),text="Total",fg="#a33724",bg="#b86a8e",command=tottal)
btntotal.grid(row=10,column=1,sticky=NSEW,padx=6,pady=10)
#btnreset
btnreset = Button(leftframe,padx=2,pady=2,bd=10,font=("Times New Roman",20,"bold"),text="Reset",fg="Black",bg="#b09038",command=resett)
btnreset.grid(row=10,column=0,sticky=NSEW,padx=13,pady=10)

#============================================== Database Management ======================================================= 

def add():
    rbadata.insert(ord.get(),fri.get(),bur.get(),dri.get(),piz.get(),sub.get(),tax.get(),ser.get(),tot.get())
    messagebox.showinfo("RB","Successfull!!")





#add
btnadd = Button(leftframe,padx=4,pady=4,bd=8,font=("arial",20,"bold"),text="Add",fg="#335949",bg="#0c737a",command=add)
btnadd.grid(row=10,column=2,sticky=NSEW,padx=6,pady=10)


def RBARecord(event):
    global sd
    searchid=foodlist.curseselection()[0]
    
    sd=foodlist.get(searchid)
    
    txtord.insert(END,sd[1])
    
    txtfries.insert(END,sd[2])
    
    txtburger.insert(END,sd[3])
    
    txtdrinks.insert(END,sd[4])
    
    txtpizza.insert(END,sd[5])
    
    txtcost.insert(END,sd[6])
    
    txtsubtotal.insert(END,sd[7])
    
    txttax.insert(END,sd[8])
    
    txtservice.insert(END,sd[9])
    
    txttotal.insert(END,sd[10])

foodlist=Listbox(rightframe,width=50,height=10,bg="#aac8e3", font=("Times New Roman",10,"bold"))

foodlist.bind("<<ListboxSelect>>",RBARecord)

foodlist.pack(side=LEFT,expand=True,fill="both");

def show():
    
    for row in rbadata.display():
        
        foodlist.insert(END,row,str(""))
        
btndisplay=Button(rightframe,font=("Times New Roman",20,"bold"),text="DISPLAY",fg="#8fa178",bg="#c7c03e",command=show)

btndisplay.pack(side=BOTTOM)

#btnexit
btnexit = Button(leftframe,padx=4,pady=4,bd=8,font=("Times New Roman",20,"bold"),text="Exit",fg="Black",bg="#de664e",command=exitt)

btnexit.grid(row=10,column=3,sticky=NSEW,padx=6,pady=10)


root.mainloop()
