print("hi welcome to the kit maker")
name = input("Please enter the name (including the /kit- bit) ")
varofmoney = str(input("Now enter the variable name(anything will work) "))
price = int(input("Now enter the price e.g. 500 "))
print("Below this will be the first bit of code, prior to the items.\n\n\n")
smolprice = price - 1
boo = True
print('case "'+ str(name) + '":')
print('int', varofmoney,'= player.m_inventory.GetItemAmountByType(254);')
print('if (' + str(varofmoney) + ' <= ' + str(smolprice) + ')')
print('{\nserver.SendMessageToPlayerLocal("Not Enough Gold!", player, msg);\n}')
print('else if (' + str(varofmoney) + ' >= ' + str(smolprice) + ')')
print('{\nint num = ' + str(price)+';')
print('num = Math.Min('+str(varofmoney)+', num);')
print('player.m_inventory.DeclineItemAmountByType(254, num);')
print('\n\n\n')
count = 1

while boo == True:
    
    itemid = int(input("Now enter your items id! "))
    amt = int(input("Now how much of this item do you want to give? "))
    dur = int(input("Finally, enter the durability(if ur item doesnt have a durability just type 111 and click enter) "))
    dur = str(dur)
    if dur != "111":
        dur = (', ' + str(dur))
    else:
        dur = ""
    print("This is item number", count, '\n')
    print('server.CreateFreeWorldItem('+ str(itemid)+', '+str(amt)+', player.GetPosition()'+ str(dur) + '); \n')
    count = count + 1
    loop = input("Would you like to add more items, if so type y otherwise type n ")
    if loop == "y":
        boo = True
    else:
        boo = False
        print ("Final bit of code below\n")
        print ('} \nbreak;')
print("Thank you for using kit creator for Immune! This was made by Charlie272 and inspired by ValidUser!")