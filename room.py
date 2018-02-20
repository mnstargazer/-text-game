class Room():
    def __init__(self, room_name):
        self.name=room_name
        self.description = None
        self.linked_rooms = {}
        self.items = {}
        self.item_number = 0
        self.character = None
        
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description 

    def set_character(self, character_name):
        self.character = character_name

    def get_character(self):
        return self.character
    
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name 

    def describe(self): 
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def add_room_item(self,item_name):
        self.items[self.item_number] = item_name
        self.item_number += 1

    def list_items(self):
        for item in self.items:
            print (self.items[item])

    def get_details(self):
        print('=====================')
        print(self.name)
        print(self.description)
        print('contains '+str(self.item_number)+' items')
        print('----------------------')
        #self.describe()
        
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

        if(self.item_number>0):
            print('Items in room:')
            self.list_items()

        if(self.character == None):
            print("There are no others in this room")
        else:
            print(self.character.name+" is in the room with you")
            
    def print_dictionary(self):
        print('=========' + room.get_name() + '============')
        print (self.linked_rooms)
   
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

