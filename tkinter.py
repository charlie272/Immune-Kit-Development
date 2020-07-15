from tkinter import *
boo = True
window = Tk()
#w = Text(window, height=1)
window.title("Welcome to The Kit Maker")
# this D; MY BRAIN SMOL LIK POTAT
window.geometry('350x200') #size
w = Text(window, height=1, borderwidth=0)
w.insert(1.0, "Hello, world!")

lbl = Label(window, text="Hello, enter kit name (including /kit-) --->") # label
lbl.grid(column=0, row=0) # where the will be
finish1 = Text(window, height=1)

finish1.grid(column=0, row=6)
finish2 = Text(window, height=1)
finish2.grid(column=0, row=7)
finish3 = Text(window, height=1)
finish3.grid(column=0, row=8)
finish4 = Text(window, height=1)
finish4.grid(column=0, row=9)
finish5 = Text(window, height=1)
finish5.grid(column=0, row=10)
finish6 = Text(window, height=1)
finish6.grid(column=0, row=11)
finish7 = Text(window, height=1)
finish7.grid(column=0, row=12)
finish8 = Text(window, height=1)
finish8.grid(column=0, row=13)

nametk = Entry(window,width=10) #where people put there crappy response D;

nametk.grid(column=1, row=0) # WHERE THIS IS ON THE GRID
lbl1 = Label(window, text="Now enter the variable --->")
lbl1.grid(column=0, row=1)
vartk = Entry(window, width=10)
vartk.grid(column=1, row=1)
lbl2 = Label(window, text="Now enter the price --->")
lbl2.grid(column=0, row=2)
pricetk = Entry(window, width=10)
pricetk.grid(column=1,row=2)


def clicked(): # CLICKED FUNCTION D::D:D::D: (not happy lol)

    name=nametk.get() #THEIR ENTRY
    varofmoney=vartk.get()
    price = pricetk.get()
 
    price=int(price)
    smolprice = price - 1
    
    line1 = ('case "'+ str(name) + '":')
    line2 = ('int', varofmoney,'= player.m_inventory.GetItemAmountByType(254);')
    line3 = ('if (' + str(varofmoney) + ' <= ' + str(smolprice) + ')')
    line4 = ('{\nserver.SendMessageToPlayerLocal("Not Enough Gold!", player, msg);\n}')
    line5 = ('else if (' + str(varofmoney) + ' >= ' + str(smolprice) + ')')
    line6 = ('{\nint num = ' + str(price)+';')
    line7 = ('num = Math.Min('+str(varofmoney)+', num);')
    line8 = ('player.m_inventory.DeclineItemAmountByType(254, num);')
    finish1.insert(1.0, line1)
    finish2.insert(1.0, line2)
    finish3.insert(1.0, line3)
    finish4.insert(1.0, line4)
    finish5.insert(1.0, line5)
    finish6.insert(1.0, line6)
    finish7.insert(1.0, line7)
    finish8.insert(1.0, line8)
   
    #lbl.configure(text= name) # WHAT THE LABEL IS

btn = Button(window, text="Click for price deduction!", command=clicked) # STOOPID BUTTON
btn.grid(column=0, row=25)
lbl3 = Label(window, text="Now enter the item id --->")
lbl3.grid(column=0, row=14)
itemidtk = Entry(window, width=10)
itemidtk.grid(column=1, row=14)
lbl4 = Label(window, text="Now enter the ammount of the item --->")
lbl4.grid(column=0, row=15)
amttk = Entry(window, width=10)
amttk.grid(column=1, row=15)
lbl5 = Label(window, text="Now enter the durability if your item is like fish (no durability) enter 111 --->")
lbl5.grid(column=0, row=16)

durtk = Entry(window, width=10)
durtk.grid(column=1, row=16)
itemtk = Text(window, height=1)
itemtk.grid(column=0, row=18)
itemtk2 = Text(window, height=1)
itemtk2.grid(column=0, row=19)
def item():
    dur = durtk.get() 
    itemid = itemidtk.get()
    amt = amttk.get()   
    dur = str(dur)
    

    if dur != "111":
        dur = (', ' + str(dur))
    else:
        dur = ""
    
    line9 = ('server.CreateFreeWorldItem('+ str(itemid)+', '+str(amt)+', player.GetPosition()'+ str(dur) + '); \n')
    itemtk.insert(1.0, line9)
    
    

btn1= Button(window, text="Click for item, BEWARE FOR ALL CODE MAY HAVE HIDDEN SO ctrl + a would be advised!", command=item)
btn1.grid(column=0, row=20)
line10 = ('} \nbreak;')
itemtk2.insert(1.0, line10)
window.mainloop() #FORGOT XD