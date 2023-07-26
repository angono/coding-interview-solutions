# Doubly Linked List Node
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

    def get_data(self):
        '''Return the self.data attribute'''
        return self.data

    def set_data(self, new_data):
        '''Replacing the existing value of the self.data 
        attribute with new_data paramenter'''
        self.data = new_data

    def get_next(self):
        '''Return the self.next attribute'''
        return self.next

    def set_next(self, new_next):
        '''Replacing the existing value of the self.next 
        attribute with new_next paramenter'''
        self.next = new_next

    def get_previous(self):
        '''Return the self.previous attribute'''
        return self.previous

    def set_previous(self, new_previous):
        '''Replacing the existing value of the self.previous 
        attribute with new_previous paramenter'''
        self.previous = new_previous
































