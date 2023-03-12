class BinPackingNode:
    def __init__(self,bins,items,index):
        self.bins=bins
        self.items = items
        self.index = index

    def cost(self):
        return len(self.bins)
    