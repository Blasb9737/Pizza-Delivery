#J.C. La Grange
#18/04/2024
#this program is used to make orders for a pizza shop called dream pizzas

import csv

#a list used for all the names of the pizza
pizza = {1:"plain",2:"peperoni",3:"hawaiian",4:"vegetarian",5:"meatlovers",6:"butter chicken", 7:"ham and cheese",8:"mega meatlovers",9:"chicken",10:"cheesy garlic",11:"vegan",12:"peri peri"}
#a list to kepp trackof what the user has ordered
order = []

#customer information
address = ""
name = input("what is your name?\n")
delivery = input("would you like your pizza to be delivered to your house (yes)/(no)\n")
if delivery.lower() == "yes" or delivery.lower() == "y":
  address = input("where would you like your pizza to be delivered to?\n")

#function used for adding pizza to the order list
def addPizza(pizza,order):
  add = 1
  #loop ends when the user enters an invalid number
  while add in [1,2,3,4,5,6,7,8,9,10,11,12] and len(order) <=5:
    print(order,"\n",pizza,"\n")
    add = int(input("what pizza would you like to add to your order? [end selection[0]]\n"))
    if add not in [1,2,3,4,5,6,7,8,9,10,11,12]:
        break
    order.append(pizza[add])
  orderEdit(pizza,order)

#function use dto remove items from ther order
def removePizza(pizza,order):
  remove=0
  while remove != 1 and len(order) <=5:
    print(order,"\n",pizza,"\n")
    remove = int(input("what pizza would you like to remove from your order? [end selection[9]]\n"))
    if remove not in order:
        break
    order.pop(remove)
  orderEdit(pizza, order)

#function used to act as the bridge between remoing items from the order and adding items to the order
def orderEdit(pizza,order):
  action = input("would you like to \n[1] add an item to your order\n[2] remove an item to your order\n[3] submit your order\n")
  #add pizza
  if action in ["1","add","ADD"]:
    addPizza(pizza,order)
  #remove pizza
  elif action in ["2","remove","REMOVE"]:
    removePizza(pizza,order)
  #create reciept
  else:
    cost = 0
    #calculate total cost
    for i in range(len(order)):
      if order[i] in ["mega meatlovers","chicken","cheesy garlic","vegan","peri peri"]:
        cost+=8.5
      else:
        cost+=5
      if address != "":
        cost+=3
    print("Total Cost:",cost,"\n",order)
    #create reciept
    with open('reciept.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # table headings
        writer.writerow(["Name:","Order:","Total Cost","Address:"])
        #customer entries
        writer.writerow([name, order, cost, address])


orderEdit(pizza,order)
