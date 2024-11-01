cat_attributes = {
    "intelligence": 50, #percentage 
    "energy": 50, #percentage 
    "weight": 4.00, #in kg
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour = input("Enter colour:")

alive=True

if cat_attributes["intelligence"] < 20: 
    print(name,"'s intelligence is too low, please increase", name,"'s intelligence by playing with it (+5) or training it (+10). If", name,"'s intelligence goes below 10, it will die")
if cat_attributes["energy"] < 20:
    print(name," has too little energy, please increase",name,"'s energy level by feeding it (+5) or putting it to sleep (+10). If",name,"'s energy level goes below 10, it will die")
if cat_attributes["weight"] <3:
    print(name," weighs too little, please feed",name,"(+o.5kg). If",name,"'s weight goes below 2.5kg, it will die")
if cat_attributes["intelligence"]<10:
    print(name," has died of stupidity. Do better.")
    alive=False
if cat_attributes["energy"] <10:
    print(name," has died of fatigue. *TIP: Never have children*")
    alive=False
if cat_attributes["weight"] <2.5:
    print(name," has died of starvation. Starving your cat is a crime punishable by death. You have been warned...")
    alive=False 
if cat_attributes["weight"]> 4:
    print(name," weighs too much, please play with it (-o.5kg) or train it(-0.25kg)")
if cat_attributes["weight"] >4.5:
    print(name," has died of obesity. *TIP: Get parenting classes.Now.*")
    alive=False 

while alive==True:
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3.Feed your cat 4. Put your cat to sleep 4. See stats")
    print("-------------------------------------------------------")
    if option == "1":
        print(name,"had a great time playing with you. It's intelligence has increased by 5 and weight has decreased by 0.5kg")
        cat_attributes["intellignce"]=int(cat_attributes["intelligence"])+5
        cat_attributes["weight"]= float(cat_attributes["weight"])-0.5
    elif option == '2':
        print(name,"has learned a new trick. It's intelligence has increased by 5 and weight has decreased by 0.25kg")
        cat_attributes["intelligence"]=int(cat_attributes["intelligence"])+5
         cat_attributes["weight"]=float(cat_attributes["weight"])-0.25
    










    else:
     

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        pass
    # elif ...
