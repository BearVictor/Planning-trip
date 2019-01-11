from tkinter import *
import tkinter.messagebox as box



window=Tk()
window.title("Trip Planning")
img=PhotoImage(file='img.pgm')
img=PhotoImage.subsample(img, x=4, y=4)
window.resizable( 0, 0 )
window.configure( bg = 'SpringGreen' )
v1 = DoubleVar()
v2 = StringVar()
v3 = DoubleVar()
v4 = DoubleVar()
v5 = DoubleVar()
v6 = DoubleVar()


imgLb1=Label(window,image=img)
label1 = Label( window,bg="MediumSpringGreen",font=14 )
label2 = Label( window,bg="MediumSpringGreen", relief = 'groove',font=14 )
label3 = Label( window,bg="MediumSpringGreen", relief = 'groove',font=14  )
label4 = Label( window,bg="MediumSpringGreen", relief = 'groove', font=14 )
label5 = Label( window,bg="MediumSpringGreen", relief = 'groove', font=14 )
entry1=Entry(window,width=10,textvariable=v1)
entry2=Entry(window,textvariable=v2)
entry3=Entry(window,textvariable=v3)
entry4=Entry(window,textvariable=v4)
entry5=Entry(window,textvariable=v5)
entry6=Entry(window,textvariable=v6)
btn=Button(window,bg="Lime")
btn2=Button(window,bg="Lime",width=5)
radio1 = Label( window,bg="MediumSpringGreen",font=14 )




imgLb1.grid(row=1,column=1,rowspan=8)
label1.grid(row=2,column=2,columnspan=3)
label2.grid(row=4,column=2)
label3.grid(row=5,column=2)
label4.grid(row=6,column=2)
label5.grid(row=7,column=2)
entry1.grid(row=1,column=3)
entry2.grid(row=3,column=2,columnspan=3,padx=10)
entry3.grid(row=4,column=4,padx=10)
entry4.grid(row=5,column=4,padx=10)
entry5.grid(row=6,column=4,padx=10)
entry6.grid(row=7,column=4,padx=10)
btn.grid(row=8,column=2,columnspan=3)
btn2.grid(row=1,column=4,)
radio1.grid(row=1,column=2,padx=10)



btn.configure( text = 'How much i spend')
btn2.configure( text = 'Help')
label1.configure(text="File name:")
label2.configure(text="Transport:")
label3.configure(text="House")
label4.configure(text="Food:")
label5.configure(text="Car:")
radio1.configure(text="What  exchange rate:")





def Kalkul(moneyyy):
    if moneyyy.find("+")!= -1:
         pb=float(moneyyy[:moneyyy.find("+")])
         pn = float(moneyyy[moneyyy.find("+")+1:])
         return float(pb + pn)
    elif moneyyy.find("-")!= -1:
        pb = float(moneyyy[:moneyyy.find("-")])
        pn = float(moneyyy[moneyyy.find("-") + 1:])
        return float(pb - pn)
    elif moneyyy.find("*") != -1:
        pb = float(moneyyy[:moneyyy.find("*")])
        pn = float(moneyyy[moneyyy.find("*") + 1:])
        return float(pb * pn)
    elif moneyyy.find("/") != -1:
        pb = float(moneyyy[:moneyyy.find("/")])
        pn = float(moneyyy[moneyyy.find("/") + 1:])
        return float(pb / pn)

def IfDollars(money):
    if money.find("$") != -1:
        return float(money.rstrip("$")) * float(entry1.get())
    elif money.find("+")!= -1 or money.find("-")!= -1 or money.find("*")!= -1 or money.find("/")!= -1:
        return Kalkul(money)
    else:
        return float(money)

def InUSD(moneyy):
    return moneyy/(float(entry1.get())+0.000000001)

def InFile(strr,money,file):
    if strr == "\nTransport":
        file.write(strr + " :" + "\t")

    else:
        file.write(strr + " :" + "\t" * 2)

    file.write("%.2f" % IfDollars(money) + " UAH\t\t" + "%.2f" % InUSD(IfDollars(money)) + " USD" + "\n")
def StrintResult(sum):
    str="\nTransport"+" :" + ""+"%.2f" %IfDollars(entry3.get())+" UAH\t\t"+"%.2f" %InUSD(IfDollars(entry3.get()))+" USD"+"\n"
    str+="House"+" :" + "\t"+"%.2f" %IfDollars(entry4.get())+" UAH\t\t"+"%.2f" %InUSD(IfDollars(entry4.get()))+" USD"+"\n"
    str+="Food" + " :" + "\t" + "%.2f" % IfDollars(entry5.get()) + " UAH\t\t" + "%.2f" % InUSD(IfDollars(entry5.get())) + " USD" + "\n"
    str += "Car" + " :" + "\t" + "%.2f" % IfDollars(entry6.get()) + " UAH\t\t" + "%.2f" % InUSD(IfDollars(entry6.get())) + " USD" + "\n"
    str+="\nSumma \t" + "%.2f" % sum + " UAH\t" + "%.2f" % InUSD(sum) + " USD\n" + "*" * 50 + "\n"
    return str

def Input():
    sum=0
    sum += IfDollars(entry3.get())
    sum += IfDollars(entry4.get())
    sum += IfDollars(entry5.get())
    sum += IfDollars(entry6.get())
    file = open((entry2.get()) + ".txt", "a")

    file.write("\n" + "*" * 50)
    InFile("\nTransport",entry3.get(),file)
    InFile("House",entry4.get(),file)
    InFile("Food",entry5.get(),file)
    InFile("Car",entry6.get(),file)
    file.write("\nSumma \t" + "%.2f" % sum + " UAH\t" + "%.2f" % InUSD(sum) + " USD\n" + "*" * 50 + "\n")

    box.showinfo("RESULT",StrintResult(sum))
    file.close()

def Help():
    box.showinfo("RESULT", "If price in USD use $\n Use {+ ; - ; / ; *} for match\nFile will be save in directory\nBut u can use C: \n Author: Viktor Mykhailov")


btn.configure(command=Input)
btn2.configure(command=Help)


window.mainloop()
