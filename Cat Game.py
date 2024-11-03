cat_attributes = {
    "intelligence": 50, #percentage 
    "energy": 50, #percentage 
    "weight": 3.50, #in kg
    }

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter your cat's name:")
colour = input("Enter the colour of your cat:")

alive=True

while alive==True:
    print("1. Play with your cat")
    print("2. Train your cat")
    print("3.Feed your cat")
    print("4. Put your cat to sleep")
    print("5. See stats")
    option = input("What would you like to do?(Type in the number of the task you would like to complete)")
    print("-------------------------------------------------------")
    if option == "1":
        print(name,"had a great time playing with you. It's intelligence has increased by 5%, and weight has decreased by 0.5kg")
        cat_attributes["intellignce"]=int(cat_attributes["intelligence"])+5
        cat_attributes["weight"]= float(cat_attributes["weight"])-0.5
        if cat_attributes["weight"] <3:
            print(name," weighs too little, please feed",name,"(+o.5kg). If",name,"'s weight goes below 2.5kg, it will die")
        elif cat_attributes["weight"] <2.5:
            alive=False
            print(name," has died of starvation. Starving your cat is a crime punishable by death. You have been warned...")
        elif cat_attributes["weight"]> 4:
            print(name," weighs too much, please play with it (-o.5kg) or train it(-0.25kg). If",name,"'s weight exceeds 4.5kg, it will die")
        elif cat_attributes["weight"] >4.5:
            alive=False
            print(name," has died of obesity. *TIP: Get parenting classes.Now.*")
        else:
            print("Your cat is still alive")
    elif option == "2":
        print(name,"has learned a new trick. It's intelligence has increased by 10%, and weight has decreased by 0.25kg")
        cat_attributes["intelligence"]=int(cat_attributes["intelligence"])+5
        cat_attributes["weight"]=float(cat_attributes["weight"])-0.25




    elif option == "3":
        print(name,"loved the food! It's energy has increased by 5%, and it's weight has increased by 0.5kg")
        cat_attributes["energy"]=int(cat_attributes["energy"])+5
        cat_attributes["weight"]=float(cat_attributes["weight"])+0.5
    elif option== "4":
        print(name,"had a great nap. It's energy has increased by 10%")
        cat_attributes["energy"]=int(cat_attributes["energy"])+10
    else:
        print(cat_attributes)


        

    if cat_attributes["intelligence"] < 20: 
        print(name,"'s intelligence is too low, please increase", name,"'s intelligence by playing with it (+5) or training it (+10). If", name,"'s intelligence goes below 10, it will die")
    elif cat_attributes["energy"] < 20:
        print(name," has too little energy, please increase",name,"'s energy level by feeding it (+5) or putting it to sleep (+10). If",name,"'s energy level goes below 10, it will die")
    elif cat_attributes["weight"] <3:
        print(name," weighs too little, please feed",name,"(+o.5kg). If",name,"'s weight goes below 2.5kg, it will die")
    elif cat_attributes["weight"]> 4:
        print(name," weighs too much, please play with it (-o.5kg) or train it(-0.25kg). If",name,"'s weight exceeds 4.5kg, it will die")
    elif cat_attributes["intelligence"]<10 or cat_attributes["energy"] <10 or cat_attributes["weight"] <2.5 or cat_attributes["weight"] >4.5:
        alive=False
    else:
        print("Your cat is still alive")

#elif cat_attributes["intelligence"]<10:
        #alive=False
        #print(name," has died of stupidity. Do better.")
    #elif cat_attributes["energy"] <10:
        #alive=False
        #print(name," has died of fatigue. *TIP: Never have children*")
    #elif cat_attributes["weight"] <2.5:
        #alive=False
        #print(name," has died of starvation. Starving your cat is a crime punishable by death. You have been warned...")
    #elif cat_attributes["weight"]> 4:
        #print(name," weighs too much, please play with it (-o.5kg) or train it(-0.25kg). If",name,"'s weight exceeds 4.5kg, it will die")
    #elif cat_attributes["weight"] >4.5:
        #alive=False
        #print(name," has died of obesity. *TIP: Get parenting classes.Now.*")
    #else:
        #print("Your cat is still alive")
if alive==False:
    print(cat_attributes)