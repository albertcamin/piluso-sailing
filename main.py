from room import Room
from character import Enemy, Character, Friend
from item import Item


kitchen=Room ("kitchen")
kitchen.set_description ("A dank and dirty room buzzing with flies.")

dining_hall=Room ("dining_hall")
dining_hall.set_description ("A big and clean dining hall")

ballroom=Room ("ballroom")
ballroom.set_description ("An empty and huge ballroom")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room (ballroom, "east")
ballroom.link_room (kitchen,"north")

dave=Enemy ("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation ("What's up dude?")
dave.talk()

dave.set_weakness ("cheese")
print ("what will you fight with?")
fight_with=input()
dave.fight (fight_with)
dining_hall.set_character(dave)

greeny = Enemy ("Greeny", " A big messy worm")
greeny.set_conversation ("Ajj, I'm so ugly")
greeny.set_weakness ("teddy")
ballroom.set_character (greeny)

cheese = Item ("cheese")
cheese.set_description ("A big and smelly bloch of cheese")
ballroom.set_item ("cheese")

teddy= Item ("teddy")
teddy.set_description ("A beautiful sweet teddy")
dining_hall.set_character (teddy)

catrina = Character ("Catrina", "A friendly Skeleton")
catrina.set_conversation ("Why hello there")
ballroom.set_character (catrina)


current_room = dining_hall     
backpack = []

dead = False
while dead == False:
     
    print("\n")      
    current_room.get_details()     
    
    inhabitant= current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
    item= current_room.get_item()
    if item is not None:
        item.describe ()
        
    command = input("> ")    
    
    if command in ["north","south", "east", "west"]:
        current_room = current_room.move(command)  
    elif command == "talk":
        set_conversation= ("who are you? what do you want?")
        inhabitant.talk()
    elif command == "fight":
        print ("what will you fight with?")
        fight_with = input ()
    
    if fight_with in backpack:
        if inhabitant.fight (fight_with)==True:
            print ("I'm the one")
            if inhabitant.get_defeated==2:
                print ("Congratulations, you won!")
                dead=True
        else: 
            print ("You lost the battle, game is over")
            
    
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your 
backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
    else:
      print("There's nothing here to take!")

