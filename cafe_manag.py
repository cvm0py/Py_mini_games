from tkinter import *
import tkinter
import random
import datetime
import time
from tkinter import messagebox

root = Tk()
root.geometry('13x150+0+0')
root.title("Cafe Management System")
root.configure(background = "black")
Tops = Frame(root,width=1350,height=100,bd=14,relief="raise")
Tops.pack()
f1 = Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)
f1a = Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1,width=900,height=320,bd=8,relief="raise")
f2a.pack(side=TOP)
ft2 = Frame(f2,width=440,height=600,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2,width=440,height=50,bd=16,relief="raise")
fb2.pack(side=TOP)

f1aa = Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a,width=400,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background="black")
f1.config(background="black")
f2.config(bg="black")

lblinfo = Label(Tops, font=('arial',70,'bold'), text = "CAFE MANAGEMENT SYSTEM",bd=10)
lblinfo.grid(row=0,column=0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
ReceiptRef = StringVar()
Paidtax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latta = StringVar()
E_Expresso = StringVar()
E_FlatWhite = StringVar()
E_Cappuccino = StringVar()
E_Affogato = StringVar()
E_HotChoc = StringVar()
E_Irrish = StringVar()
E_African = StringVar()

E_CoffeeCake = StringVar()
E_RedVelvetCake = StringVar()
E_BlackForrest = StringVar()
E_BostomCreamCake = StringVar()
E_LagosChocoCake = StringVar()
E_KillburnCake = StringVar()
E_CarltonChocoCake = StringVar()
E_QueenParkCake = StringVar()

Randomref = StringVar()
Randomref.set('0')
E_Latta.set("0")
E_Expresso.set('0')
E_FlatWhite.set('0')
E_Cappuccino.set('0')
E_Affogato.set('0')
E_HotChoc.set('0')
E_Irrish.set('0')
E_African.set('0')

E_CoffeeCake.set("0")
E_RedVelvetCake.set("0")
E_BlackForrest.set("0")
E_BostomCreamCake.set("0")
E_LagosChocoCake.set('0')
E_KillburnCake.set('0')
E_CarltonChocoCake.set('0')
E_QueenParkCake.set('0')

var1.set('0')
var2.set('0')
var3.set('0')
var4.set('0')
var5.set('0')
var6.set('0')
var7.set('0')
var8.set('0')
var9.set('0')
var10.set('0')
var11.set('0')
var12.set('0')
var13.set('0')
var14.set('0')
var15.set('0')
var16.set('0')

DateofOrder.set(time.strftime("%d%m%Y"))
#############################Drinks#########################

Latta = Checkbutton(f1aa,text="Latta",variable = var1,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=0,sticky=W)
Espresso = Checkbutton(f1aa,text="Espresso",variable = var2,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=1,sticky=W)
FlatWhite = Checkbutton(f1aa,text="Flat White",variable = var3,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=2,sticky=W)
Cappuccino = Checkbutton(f1aa,text="Cappuccino",variable = var4,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=3,sticky=W)
Affogato = Checkbutton(f1aa,text="Affogato",variable = var5,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=4,sticky=W)
HotChoc = Checkbutton(f1aa,text="Hot chocolate",variable = var6,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=5,sticky=W)
Irrish = Checkbutton(f1aa,text="Irrish coffee",variable = var7,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=6,sticky=W)
African = Checkbutton(f1aa,text="African coffee",variable = var8,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=7,sticky=W)

###############################cakes###################################

CoffeCake = Checkbutton(f1ab,text="Coffe Cake",variable = var9,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=0,sticky=W)
RedvalvetCake = Checkbutton(f1ab,text="Redvalvet Cake",variable = var10,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=1,sticky=W)
BlackForrestCake= Checkbutton(f1ab,text="Black Forrest Cake",variable = var11,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=2,sticky=W)
BostomCreamCake = Checkbutton(f1ab,text="Bostom Cream Cake",variable = var12,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=3,sticky=W)
LagosChocoCake = Checkbutton(f1ab,text="Lagos Choco Cake",variable = var13,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=4,sticky=W)
KillburnChocoCake = Checkbutton(f1ab,text="Killburn Choco Cake",variable = var14,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=5,sticky=W)
CarltonChocoCake = Checkbutton(f1ab,text="Carlton Choco Cake",variable = var15,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=6,sticky=W)
QueenParkCake = Checkbutton(f1ab,text="Queen Park Cake",variable = var16,onvalue = 1,offvalue=0,font=('arial',18,'bold')).grid(row=7,sticky=W)

######create widgets option for drinks
txtLatta = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Latta)
txtLatta.grid(row=0,column=1)
txtExpresso = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Expresso)
txtExpresso.grid(row=1,column=1)
txtFlatWhite = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_FlatWhite)
txtFlatWhite.grid(row=2,column=1)
txtCappuccino = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Cappuccino)
txtCappuccino.grid(row=3,column=1)
txtAffogato = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Affogato)
txtAffogato.grid(row=4,column=1)
txtHotChoc = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_HotChoc)
txtHotChoc.grid(row=5,column=1)
txtIrrish = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_Irrish)
txtIrrish.grid(row=6,column=1)
txtAfrican = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_African)
txtAfrican.grid(row=7,column=1)

#####create widgets optins for cakes
txtCoffeeCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_CoffeeCake)
txtCoffeeCake.grid(row=0,column=1)
txtRedVelvetCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_RedVelvetCake)
txtRedVelvetCake.grid(row=1,column=1)
txtBlackForrestCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_BlackForrest)
txtBlackForrestCake.grid(row=2,column=1)
txtBostomCreamCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_BostomCreamCake)
txtBostomCreamCake.grid(row=3,column=1)
txtLagosChocoCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_LagosChocoCake)
txtLagosChocoCake.grid(row=4,column=1)
txtKillburnCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_KillburnCake)
txtKillburnCake.grid(row=5,column=1)
txtCarltonChocoCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_CarltonChocoCake)
txtCarltonChocoCake.grid(row=6,column=1)
txtQueenParkCake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6, justify='left',textvariable=E_QueenParkCake)
txtQueenParkCake.grid(row=7,column=1)

##information

lblReceipt = Label(ft2,font=('arial',12,'bold'),text = "Reciept:",bd=2, anchor=W)
lblReceipt.grid(row=0,column=0,sticky=W)

txtReceipt = Text(ft2,width=59,height=22, bg ="White",bd=8, font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)

###cost item information
lblCostofDrinks = Label(f2aa,font=('arial',16,'bold'),text='Cost of Drinks',bd =8)
lblCostofDrinks.grid(row=0,column=0,sticky=W)

txtCostofDrinks = Entry(f2aa,font=('arial',16,'bold'),bd=8, justify='left',textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1,sticky=W)

lblCostofCakes = Label(f2aa,font=('arial',16,'bold'),text='Cost of Cakes',bd =8)
lblCostofCakes.grid(row=1,column=0,sticky=W)

txtCostofCakes = Entry(f2aa,font=('arial',16,'bold'),bd=8, justify='left',textvariable=CostofCakes)
txtCostofCakes.grid(row=1,column=1,sticky=W)

lblServiceCharge = Label(f2aa,font=('arial',16,'bold'),text='Service charge',bd =8)
lblServiceCharge.grid(row=2,column=0,sticky=W)

txtServiceCharge = Entry(f2aa,font=('arial',16,'bold'),bd=8, justify='left',textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1,sticky=W)

lblTax = Label(f2ab,font=('arial',16,'bold'),text='Tax',bd =8)
lblTax.grid(row=0,column=0,sticky=W)

txtTax= Entry(f2ab,font=('arial',16,'bold'),bd=8, justify='left',textvariable=Paidtax)
txtTax.grid(row=0,column=1,sticky=W)

lblSubTotal = Label(f2ab,font=('arial',16,'bold'),text='Sub Total',bd =8)
lblSubTotal.grid(row=1,column=0,sticky=W)

txtSubTotal= Entry(f2ab,font=('arial',16,'bold'),bd=8, justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=1,column=1,sticky=W)

lblTotalCost = Label(f2ab,font=('arial',16,'bold'),text='Total Cost',bd =8)
lblTotalCost.grid(row=2,column=0,sticky=W)

txtTotalCost= Entry(f2ab,font=('arial',16,'bold'),bd=8,text="ra",justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=2,column=1,sticky=W)


#####################method definations######################
def qExit():
    qExit = tkinter.messagebox.askyesno("Quit system","Do you want to Quit?")

    if qExit > 0:
        root.destroy()
        return

def reset():
    Paidtax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Latta.set("0")
    E_Expresso.set('0')
    E_FlatWhite.set('0')
    E_Cappuccino.set('0')
    E_Affogato.set('0')
    E_HotChoc.set('0')
    E_Irrish.set('0')
    E_African.set('0')

    E_CoffeeCake.set("0")
    E_RedVelvetCake.set("0")
    E_BlackForrest.set("0")
    E_BostomCreamCake.set("0")
    E_LagosChocoCake.set('0')
    E_KillburnCake.set('0')
    E_CarltonChocoCake.set('0')
    E_QueenParkCake.set('0')

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')

    txtLatta.configure(state= DISABLED)
    txtExpresso.configure(state= DISABLED)
    txtFlatWhite.configure(state= DISABLED)
    txtCappuccino.configure(state= DISABLED)
    txtAffogato.configure(state= DISABLED)
    txtHotChoc.configure(state= DISABLED)
    txtIrrish.configure(state= DISABLED)
    txtAfrican.configure(state= DISABLED)

    txtCoffeeCake.configure(state= DISABLED)
    txtRedVelvetCake.configure(state= DISABLED)
    txtBlackForrestCake.configure(state= DISABLED)
    txtKillburnCake.configure(state=DISABLED)
    txtBostomCreamCake.configure(state= DISABLED)
    txtLagosChocoCake.configure(state= DISABLED)
    txtCarltonChocoCake.configure(state= DISABLED)
    txtQueenParkCake.configure(state= DISABLED)


######################checkButtons#######################
def checkButton_value():
    if var1.get()==1:
        txtLatta.configure(state=NORMAL)
    elif var1.get()==0:
        # txtLatta.configure(state=DISABLED)
        E_Latta.set("0")

    if var2.get()==1:
        txtExpresso.configure(state=NORMAL)
    elif var2.get()==0:
        txtExpresso.configure(state=DISABLED)
        E_Expresso.set("0")

    if var3.get()==1:
        txtFlatWhite.configure(state=NORMAL)
    elif var3.get()==0:
        txtFlatWhite.configure(state=DISABLED)
        E_FlatWhite.set("0")

    if var4.get()==1:
        txtCappuccino.configure(state=NORMAL)
    elif var4.get()==0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")

    if var5.get() == 1:
        txtAffogato.configure(state=NORMAL)
    elif var5.get() == 0:
        txtAffogato.configure(state=DISABLED)
        E_Affogato.set("0")

    if var6.get() == 1:
        txtHotChoc.configure(state=NORMAL)
    elif var6.get() == 0:
        txtHotChoc.configure(state=DISABLED)
        E_HotChoc.set("0")

    if var7.get() == 1:
        txtIrrish.configure(state=NORMAL)
    elif var7.get() == 0:
        txtIrrish.configure(state=DISABLED)
        E_Irrish.set("0")

    if var8.get() == 1:
        txtAfrican.configure(state=NORMAL)
    elif var8.get() == 0:
        txtAfrican.configure(state=DISABLED)
        E_African.set("0")


    if var9.get()==1:
        txtCoffeeCake.configure(state=NORMAL)
    elif var9.get()==0:
        txtCoffeeCake.configure(state=DISABLED)
        E_CoffeeCake.set("0")


    if var10.get()==1:
        txtRedVelvetCake.configure(state=NORMAL)
    elif var10.get()==0:
        txtRedVelvetCake.configure(state=DISABLED)
        E_RedVelvetCake.set("0")

    if var11.get()==1:
        txtBlackForrestCake.configure(state=NORMAL)
    elif var11.get()==0:
        txtBlackForrestCake.configure(state=DISABLED)
        E_BlackForrest.set("0")

    if var12.get()==1:
        txtBostomCreamCake.configure(state=NORMAL)
    elif var12.get()==0:
        txtBostomCreamCake.configure(state=DISABLED)
        E_BostomCreamCake.set("0")

    if var13.get() == 1:
        txtLagosChocoCake.configure(state=NORMAL)
    elif var13.get() == 0:
        txtLagosChocoCake.configure(state=DISABLED)
        E_LagosChocoCake.set("0")

    if var14.get() == 1:
        txtKillburnCake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtKillburnCake.configure(state=DISABLED)
        E_KillburnCake.set("0")

    if var15.get() == 1:
        txtCarltonChocoCake.configure(state=NORMAL)
    elif var15.get() == 0:
        txtCarltonChocoCake.configure(state=DISABLED)
        E_CarltonChocoCake.set("0")

    if var16.get() == 1:
        txtQueenParkCake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtQueenParkCake.configure(state=DISABLED)
        E_QueenParkCake.set("0")


#############################COST of ITEMS##########################3
def CostofItems():
    Item1 = float(E_Latta.get())
    Item2 = float(E_Expresso.get())
    Item3 = float(E_FlatWhite.get())
    Item4 = float(E_Cappuccino.get())
    Item5 = float(E_Affogato.get())
    Item6 = float(E_HotChoc.get())
    Item7 = float(E_Irrish.get())
    Item8 = float(E_African.get())

    Item9 = float(E_CoffeeCake.get())
    Item10 = float(E_RedVelvetCake.get())
    Item11 = float(E_BlackForrest.get())
    Item12 = float(E_BostomCreamCake.get())
    Item13 = float(E_LagosChocoCake.get())
    Item14 = float(E_KillburnCake.get())
    Item15 = float(E_CarltonChocoCake.get())
    Item16 = float(E_QueenParkCake.get())

    PriceofDrinks = (Item1 * 60) + (Item2 * 70) + (Item3 * 80) + (Item4 * 90) + (Item5 * 50) + (Item6 * 60) + (Item7 * 40) + (Item1 * 70)
    PriceofCakes = (Item9 * 600) + (Item10 * 540) + (Item11 * 400) + (Item12 * 670) + (Item13 * 575) + (Item14 * 600) + (Item15 * 1000) + (Item16 * 500)

    DrinksPrice = "Rs " ,str('%2f'%(PriceofDrinks))
    CakesPrice = "Rs ", str('%2f'%(PriceofCakes))

    CostofDrinks.set(DrinksPrice)
    CostofCakes.set(CakesPrice)

    SC = "Rs ",str('%2f'%(30))
    ServiceCharge.set(SC)

    SubTotalofItems= "Rs ",str('%2f'%(PriceofDrinks + PriceofCakes + 30))
    SubTotal.set(SubTotalofItems)

    Tax = "Rs ", str('%2f'%(PriceofDrinks + PriceofCakes + 30 * 0.15))
    Paidtax.set(Tax)

    TT = ((PriceofDrinks + PriceofCakes + 30)* 0.15)
    TC = "Rs ",str('%2f'%(PriceofDrinks + PriceofCakes + 30 +TT))
    TotalCost.set(TC)



########################

def receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(100098,654321)
    randomref = str(x)
    ReceiptRef.set("BILL    "+randomref)

    txtReceipt.insert(END,"Receipt Ref : \t\t\t "+ ReceiptRef.get()+ '\t\t' + DateofOrder.get() + '\n')

    txtReceipt.insert(END,'Items \t\t\t\t' + "Cost of Items\n\n")

    txtReceipt.insert(END, 'Latta\t\t\t\t\t' + E_Latta.get()+'\n')
    txtReceipt.insert(END, 'Expresso\t\t\t\t\t' + E_Expresso.get() + '\n')
    txtReceipt.insert(END, 'FlatWhite\t\t\t\t\t' + E_FlatWhite.get() + '\n')
    txtReceipt.insert(END, 'Cappuccino\t\t\t\t\t' + E_Cappuccino.get() + '\n')
    txtReceipt.insert(END, 'Affogato\t\t\t\t\t' + E_Affogato.get() + '\n')
    txtReceipt.insert(END, 'HotChoc\t\t\t\t\t' + E_HotChoc.get() + '\n')
    txtReceipt.insert(END, 'Irrish\t\t\t\t\t' + E_Irrish.get() + '\n')
    txtReceipt.insert(END, 'African\t\t\t\t\t' + E_African.get() + '\n')


    txtReceipt.insert(END, 'CoffeeCake\t\t\t\t\t' + E_CoffeeCake.get()+'\n')
    txtReceipt.insert(END, 'RedVelvetCake\t\t\t\t\t' + E_RedVelvetCake.get() + '\n')
    txtReceipt.insert(END, 'BlackForrest\t\t\t\t\t' + E_BlackForrest.get() + '\n')
    txtReceipt.insert(END, 'BostomCreamCake\t\t\t\t\t' + E_BostomCreamCake.get() + '\n')
    txtReceipt.insert(END, 'LagosChocoCake\t\t\t\t\t' + E_LagosChocoCake.get() + '\n')
    txtReceipt.insert(END, 'KillburnCake\t\t\t\t\t' + E_KillburnCake.get() + '\n')
    txtReceipt.insert(END, 'CarltonChocoCake\t\t\t\t\t' + E_CarltonChocoCake.get() + '\n')
    txtReceipt.insert(END, 'QueenParkCake\t\t\t\t\t' + E_QueenParkCake.get() + '\n')

    txtReceipt.insert(END,"Cost of Drinks :\t" + CostofDrinks.get() + '\tSub Total\t' + SubTotal.get() +"\n")
    txtReceipt.insert(END, "Cost of Cakes :\t" + CostofCakes.get() + '\tSub Total\t' + SubTotal.get() + "\n")

    txtReceipt.insert(END,'Service Charge :\t'+ ServiceCharge.get() + 'Total Cost\t' + TotalCost.get() +'\n')

 ##########################Buttons##################
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="Total",
                      command=CostofItems).grid(row=0, column=0)
btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                        text="Receipt",command=receipt).grid(row=0, column=1)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="Reset",
                      command=reset).grid(row=0, column=2)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="Exit",
                     command=qExit).grid(row=0, column=3)
root.mainloop()

