"""
Author: Arionna Fellows
Date Written: 07/18/24
Assignment: Pizza Palace
Short Desc: The purpose of this assignment is to make a GUI program that lets the user order pizza.
"""
#import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton

#Tk class
root = Tk()
root.geometry("650x350")

#tittle of window
root.title("Pizza Palace")

#Pizza order function
def pizza_order():

    #total price
    total = 0

    if name.get() =="" or phone.get() =="":
    
        if size.get()=="" -1:
            messagebox.showerror("Select size")
        return
    else:
        selected_size = size_list[size.get()]
        size_price = size_dict[selected_size]
        
        #adding prices with sizes
        total = total + size_price

        if crust.get() == -1:
            messagebox.showerror("Select crust")
            return
        else:
            selected_crust = crust_list[crust.get()]
            crust_price = crust_dict[selected_crust]

            #adding crust with total
            total = total + crust_price

            #Adding topping with total price
            if sausage.get() == 1:
                total = total + toppings_price[0]
            if pineapples.get() == 1:
                total = total + toppings_price[1]
            if archovies.get() == 1:
                total = total + toppings_price[2]
            if pepperoni.get() == 1:
                total = total + toppings_price[3]

        message.showerror(f"Order Succesfully Placed""\nName-{name.get()}\n number-{number.get()}\n size-{selected_size}\n crust{selected_crust}\n Total-${total}")
                

            
#Select pizza Size
Label(root, text="Select Pizza Size", font= ("Ariel")).place(x=15, y =105)
Label(root, text = "Price", font=("Ariel")).place(x=15, y=135)
Label(root, text = "Topping", font = ("Ariel")).place(x=115, y=135)
size = IntVar()
size.set(-1)

#size_dict shows different sizes and prices
size_dict = {"Small": 10, "Medium": 15, "Large": 20, "XtraLarge": 25}
size_list=["Small", "Medium", "Large"]
size_price= [10, 15, 20, 25]

#Create Buttons and Labels for size
for i in range (0,len(size_list)):
    button = Button(root, text = size_list[i],  font=("Ariel", 14))
    Label(root, text = f"${size_price[i]}").place(x = 15, y= 167 + i * 25)
    button.place(x=95, y= 165 + i * 25)

#Crust
Label(root,text="Select Your Crust", font=("Ariel",20)).place(x=270, y=105)
Label(root,text="price",font =("Ariel", 15)).place(x=274, y=135)
Label(root,text="Type", font =("Ariel",15)).place(x=355,y=135)

crust= IntVar()
crust.set(-1)

#Crust dict shows different crust and prices
crust_dict = {"Thin":2, "Stuffed":4, "Deep Dish":6}
crust_list = {"Thin", "Stuffed", "Deep Dish"}
crust_price = {2, 4, 6}

#Buttons and label for crust
for i in range(0,len(crust_list)):
    button = Button(root, text = {crust_list}, font =("Ariel", 12))
    Label(root,text=f"${crust_price[i]}").place(x=520, y=105)
    button.place(x=355, y=165 + i * 25)

#Toppings
Label(root,text="Select Your Toppings", font=("Ariel", 15)).place(x=525 , y=105)
Label(root,text="Price", font=("Ariel", 12)).place(x=520 , y=135)
Label(root,text="Type", font=("Ariel", 12)).place(x=640 , y=135)

#price label for toppings
sausage = IntVar()
sausage_checkbutton = checkbutton(root, text="Sausage")
sausage_checkbutton.place(x=605, y=165)

pineapple= IntVar() 
pineapple_checkbutton = checkbutton(root, text="Pineapple")
Pepperoni_checkbutton.place(x=605, y=190)

archovies = IntVar()
archovies_checkbutton = checkbutton(root, text="Archovies")
archovies_checkbutton.place(x=605, y=215)

pepperoni = IntVar()
pepperoni_checkbutton = checkbutton(root, text="Pepperoni")
Pepperoni_checkbutton.place(x=605, y=240)

#order button
Button(root, text= "Place order", font=("Ariel", 13),width =45,command = place_order).place(x=15 , y=285)

#exit button
Button(root, text= "Exit", font=("Ariel", 13),width =20,command =quit).place(x=505 , y=285)

root.mainloop()

    


            
                    
                                
    
