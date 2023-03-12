import Item

class Bin:
    def __init__(self,items,capacity):
        self.items = items
        self.capacity = capacity

    def get_available_space(self):
        return self.capacity - sum(item.space for item in self.items)
