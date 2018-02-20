from room import Room
from item import Item
from helpMe import HelpMe
from character import Enemy
from character import Friend

myhelp = HelpMe()
myhelp.helpMe()

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I am a a zomilator")
dave.set_weakness("cheese")

mary = Friend("Mary", "A nice person")
mary.set_conversation("I like hugs")
#dave.set_weakness("cheese")

# create rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.set_character(mary)

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
#put an enemy in the room
dining_hall.set_character(dave)

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# these two do the same thing 
# print(kitchen.get_description())
# kitchen.describe()

#link the rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")



# create an item
knife = Item('knife')
knife.set_item_name('kitchen knife')
knife.set_item_description('Looks like a kitchen carving knife')

cup = Item('cup')
knife.set_item_name('coffee cup')
knife.set_item_description('A coffee cup spilled over with coffee emptied out')

# add room items
kitchen.add_room_item('knife')
kitchen.add_room_item('cup')

# list roomd and their links
#kitchen.get_details()
#dining_hall.get_details()
#ballroom.get_details()

#start game
current_room = kitchen          

while True:		
    print("-----------------------------------------------------\n")         
    print ("you are in the "+current_room.get_name()+".  What do you want to do?")
    #current_room.get_details()
    command = input("> ")
    command_list = command.split(',')

    #print('command was: '+str(len(command_list)))

    if len(command_list) == 0:
        # descrive the error here
        myhelp.prompt(command_list[0])
    elif len(command_list) == 1:
        #handle singe word commands here
        if command_list[0] == 'help':
            myhelp.helpMe()
        elif command_list[0] == 'describe':
            current_room.get_details()
        elif command_list[0] == 'hug':
            if current_room.get_character() is not None:
                print(current_room.get_character().hug_me())
            else:
                print("There is no one to hug")
        elif command_list[0] == 'gift':
            if current_room.get_character() is not None:
                print(current_room.get_character().gift_me())
            else:
                print("There is no one to give a gift to")
        elif command_list[0] == 'fight':
            if current_room.get_character() is not None:
                fight_with = input("What will you fight with? ")
                result = current_room.get_character().fight(fight_with)
                if result:
                    current_room.set_character(None)
                else:
                    print("Sadly you have been off'ed by "+current_room.get_character().name+" which ends the game")
                    break
            else:
                print("There is nobody in this room to fight with")
        else:
            myhelp.prompt(command_list[0])
    elif len(command_list) == 2:
        #handle two word commands here
        if command_list[0] == 'move':
            current_room = current_room.move(command_list[1])
        elif command_list[0] == 'talk':
            if command_list[1] == 'dave':
                dave.describe()
                dave.talk()
            else:
                print("There is no body here by that name.")
        else:
            myhelp.prompt(command_list[0])
    else:
        myhelp.prompt(command_list[0])
        
    #current_room = current_room.move(command)
    

