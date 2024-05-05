# J.C. La Grange
# 18/04/2024
# this program is used to make orders for a pizza shop called dream pizzas

# needed for the reciept
import csv
# nneded for the display
from tkinter import *
# needed for the algorithm used to display the grid formation of the buttons
import math

# the window used to display the screen
window = Tk()
# a list used for all the names of the pizza
pizza = {1: "plain", 2: "peperoni", 3: "hawaiian", 4: "vegetarian", 5: "meatlovers", 6: "butter chicken",
         7: "ham and cheese", 8: "mega meatlovers", 9: "chicken", 10: "cheesy garlic", 11: "vegan", 12: "peri peri"}
# a list to kepp trackof what the user has ordered
order = []

# customer information
address = ""
name = ""

#a list keeping track of the users details
details = []

# the image used as a placeholder for the images
pizzaImage = PhotoImage(file="image.PNG")


# function that removes the pizza from the order list
def delete(pos, pizza, order, rvmPizza):
    # if the user wants to return
    if pos == 0:
        window.after(10, addPizza(order, pizza))
    else:
        # remove pizza from order list
        order.pop(pos)
        # update screen
        rvmPizza[pos].destroy()


# remove a pizza from the order
def removePizza(order, pizza):
    # clear screen
    for widget in window.winfo_children():
        widget.destroy()
        # display the order buttons + return button
    rvmPizza = [[] for j in range(len(order) + 1)]
    for i in range(len(order) + 1):
        rvmPizza[i] = Button(window, image=pizzaImage, height=100, width=100,
                             command=lambda pos=i: delete(pos, pizza, order, rvmPizza))
        # USED TO CALCULATE THE FORMATIONS OF THE BUTTONS, EG. 4x4 square formation
        x = math.floor(i // 4)
        y = i % 4 + 1
        # display buttons in grid format
        rvmPizza[i].grid(row=x, column=y)
        # display the order
        # all tiles are what ur order is while the first tile is to return


# submit the users order (craete the csv screen and display the cost)
def submitOrder(order, pizza, details):
    print(details)
    # claer screen
    for widget in window.winfo_children():
        widget.destroy()
    # calculate the total cost
    cost = 0
    # calculate total cost
    for i in range(len(order)):
        if order[i] in ["mega meatlovers", "chicken", "cheesy garlic", "vegan", "peri peri"]:
            cost += 8.5
        else:
            cost += 5
        if address != "":
            cost += 3
    # text
    totalCostText = "Total Cost: ", cost
    nameText = "Name: ",details[0]
    try:
        if details[1] != "":
            addressText = "Address: ",details[1]
    except:
        #do nothing
        print()
        # display details
    nameLabel = Label(window, text = nameText).pack()
    try:
        addressLabel = Label(window, text = addressText).pack()
    except:
        #do nothing
        print()
    costLabel = Label(window, text=totalCostText).pack()
    # loop that displayes each item individually
    displayOrderList = [[] for f in range(len(order))]
    for x in range(len(order)):
        # display pizza
        displayOrderList[x] = Label(window, text=order[x]).pack()
        #create reciept
        with open('reciept.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # table headings
            writer.writerow(["Name:","Order:","Total Cost","Address:"])
            #customer entries
            writer.writerow([name, order, cost, address])



# see what the user selected
def click(pos, pizza, order):
    # if the user selects 0-11 then add a pizza
    # if the user selects 12 then remove a pizza
    # if the user selects 15 then submit the order
    # if the user adds a pizza
    if pos + 1 in pizza and len(order) <= 4:
        # add pizza to the order
        order.append(pizza[pos + 1])
    # remove a pizza
    elif pos == 12:
        window.after(10, removePizza(order, pizza))
    elif pos == 15:
        window.after(10, submitOrder(order, pizza,details))


# function used to add pizza to the users order
def addPizza(order, pizza):
    global pizzaImage
    # clearing the screen
    for widget in window.winfo_children():
        widget.destroy()
    # display 16 buttons with the first 12 being to by pizzas
    choose = [[] for j in range(16)]
    for i in range(16):
        choose[i] = Button(window, image=pizzaImage, height=100, width=100,
                           command=lambda pos=i: click(pos, pizza, order))
        # USED TO CALCULATE THE FORMATIONS OF THE BUTTONS, EG. 4x4 square formation
        x = math.floor(i // 4)
        y = i % 4 + 1
        # display buttons in grid format
        choose[i].grid(row=x, column=y)


# function used to see whether the user can move on to the adding pizzas to their menu
def submitUser():
    global details
    # store the users name and address
    name = entryName.get()
    details.append(name)
    # an error would occur if the user did not enter a address
    try:
        address = addressEntry.get()
        details.append(address)
    except:
        # do nothing
        print()
    # now that the user has entered ther information its time to add the pizza. call the pizza add function
    window.after(10, addPizza(order, pizza))


# function used to see whether the user should add their address or not
def delivery():
    global location
    global addressLabel
    global addressEntry
    global submitBtn
    # remove submit buttopn so that it can be placed at the bottom
    submitBtn.pack_forget()
    # check whether address required or not
    if location == False:
        # adds address
        addressLabel.pack()
        addressEntry.pack()
        location = True
    elif location == True:
        # removes address
        addressLabel.pack_forget()
        addressEntry.pack_forget()
        location = False
    # recraete the submit button
    submitBtn.pack()


# this will be used to recieve the users input such as the name addres and delivery status
# clear screen
for widget in window.winfo_children():
    widget.destroy()
# lable used to make it clear what each input does
nameLabel = Label(window, text="Name:")
nameLabel.pack()
# the name of the user
entryName = Entry(window)
# display name input
entryName.pack()
# delevery button that decided whether the addres of the user is needed
# label for delivery button)
location = False
# address label
addressLabel = Label(window, text="Address:")
# address input
addressEntry = Entry(window)
deliveryLabel = Label(window, text="Delivery?")
deliveryLabel.pack()
deliveryBtn = Button(window, command=delivery)
# display button
deliveryBtn.pack()
# button used to submit the customer information
submitBtn = Button(window, text="Submit:", command=submitUser)
submitBtn.pack()

window.mainloop()
