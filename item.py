class Item():
    def __init__(self, item_name):
        self.name=item_name
        self.description = None
        self.contents = None

    def set_item_name(self, item_name):
        self.description = item_name
        
    def set_item_description(self, item_description):
        self.description = item_description

    def set_item_contents(self, item_contents):
        self.contents = item_contents

    def get_item_name(self):
        return self.name
    
    def get_item_description(self):
        return self.description

    def get_item_contents(self):
        return self.contents

    def describe(self): 
        print( self.description )

    def get_details(self):
        print('=====================')
        print(self.name)
        print(self.description)
        print('----------------------')
