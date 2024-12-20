cat_attributes = {
    "intelligence": 50, #percentage 
    "energy": 50, #percentage 
    "weight": 3.50, #in kg
    }

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter your cat's name:")
colour = input("Enter the colour of your cat:")
print("-------------------------------------------------------")

alive=True

while alive==True:
    print("1. Play with your cat (+5 intelligence, -5 energy, -0.5 weight)")
    print("2. Train your cat (+10 intelligence, -10 energy, -0.25 weight)")
    print("3.Feed your cat (+5 energy, +0.5 weight)")
    print("4. Put your cat to sleep (+10 energy)")
    print("5. See stats")
    option = input("What would you like to do?(Type in the number of the task you would like to complete)")
    print("-------------------------------------------------------")
    if option == "1":
        cat_attributes["intellignce"]=int(cat_attributes["intelligence"])+5
        cat_attributes["energy"]=int(cat_attributes["energy"])-5
        cat_attributes["weight"]= float(cat_attributes["weight"])-0.5
        if cat_attributes["energy"]==20:
            print(name,"has too little energy. Please put",name,"to sleep(+10 energy). If",name,"'s energy level reaches 10%, it will die of exhaustion.")
        elif cat_attributes["energy"]==10:
            alive=False
            print(name,"has died of fatigue. *TIP: Never have children*")
        if cat_attributes["weight"] <2.5:
                alive=False
                print(name,"has died of starvation. Starving your cat is a crime punishable by death. You have been warned...")
        elif cat_attributes["weight"] <3:
            print(name,"weighs too little, please feed",name,"(+o.5kg). If",name,"'s weight goes below 2.5kg, it will die.")
        if cat_attributes["weight"] >4.5:
            alive=False
            print(name,"has died of obesity. *TIP: Get parenting classes.Now.*")
        elif cat_attributes["weight"]> 4:
            print(name,"weighs too much, please play with it (-o.5kg) or train it(-0.25kg). If",name,"'s weight exceeds 4.5kg, it will die.")
        else:
            print(name,"had a great time playing with you. It's intelligence has increased by 5%, and weight has decreased by 0.5kg.")

    elif option == "2":
        cat_attributes["intelligence"]=int(cat_attributes["intelligence"])+10
        cat_attributes["energy"]=int(cat_attributes["energy"])-10
        cat_attributes["weight"]=float(cat_attributes["weight"])-0.25
        if cat_attributes["energy"]==20:
            print(name,"has too little energy. Please put",name,"to sleep(+10 energy). If",name,"'s energy level reaches 10%, it will die.")
        elif cat_attributes["energy"]==10:
            alive=False
            print(name,"has died of exhaustion. *TIP: Never have children*")
        if cat_attributes["weight"] <2.5:
            alive=False
            print(name,"has died of starvation. Starving your cat is a crime punishable by death. You have been warned...")
        elif cat_attributes["weight"] <3:
            print(name,"weighs too little, please feed",name,"(+o.5kg). If",name,"'s weight goes below 2.5kg, it will die.")
        else:
            print(name,"has learned a new trick. It's intelligence has increased by 10%, and weight has decreased by 0.25kg.")
            
    elif option == "3":
        cat_attributes["energy"]=int(cat_attributes["energy"])+5
        cat_attributes["weight"]=float(cat_attributes["weight"])+0.5
        if cat_attributes["weight"] >4.5:
            alive=False
            print(name,"has died of obesity. *TIP: Get parenting classes.Now.*")
        elif cat_attributes["weight"]> 4:
            print(name,"weighs too much, please play with it (-o.5kg) or train it(-0.25kg). If",name,"'s weight exceeds 4.5kg, it will die.")
        else:
            print(name,"loved the food! It's energy has increased by 5%, and it's weight has increased by 0.5kg.") 

    elif option== "4":
        print(name,"had a great nap. It's energy has increased by 10%.")
        cat_attributes["energy"]=int(cat_attributes["energy"])+10
    else:
        print(cat_attributes)

#ENERGY IS ALSO AFFECTED BY TRAINING AND PLAYING

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
    print("RIP", name, cat_attributes)

    #IF I HAVE TIME I'LL ENSURE I CHANGE THE PROGRAMME SO ONLY THE DEATH MESSAGE APPEARS INSTEAD OF THE WARNING TOO