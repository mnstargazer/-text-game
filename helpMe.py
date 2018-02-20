class HelpMe():
    def __init__(self):
        print("Help menu")

    def helpMe(self):
        print("Available commands and format:")
        print("help - prints this message")
        print("move,direction - moves your character from the current room in the direction specifed.  Available directions are north, south, east and west")
        print("describe - \t\t describes the current room")
        print("chat,person_name) - chats to a person in the room") 
        print("commands are not case sensitive, for ecample East is the same as east")
        print("For commands with more than one parameter (eg move,east) you must include the comma")

    def prompt(self,command):
        print("I did not understand that command: "+ command+" \nFor a list of available commands type 'help'")
