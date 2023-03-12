from BinPackingNode import BinPackingNode
from Bin import Bin
from Item import Item

class BinPacking:
    #!the list of item and the capacity of each bin
    def __init__(self,items:list[Item],capacity):
        self.items = items
        self.capacity = capacity
    
    
    
    
    #!could be any for our case we chose first fit
    def find_solution(self):
        bin_list = []
        bin_list.append(Bin([],self.capacity))
        for item in self.items:
            
                
            fits = False
            #*for each bin try to insert the item in the first bin you can find
            for bin in bin_list:
                if bin.get_available_space() >= item.space :
                    bin.items.append(item)
                    fits = True
                    break
            
            #*if the item doesn't fit create a new 
            if fits == False:
                bin_list.append(Bin([item],self.capacity))
            
            
            
        return bin_list,len(bin_list)
    
    
    
    
    #!insert an item into a list
    def insert(self,bin_list:list[Bin], item:Item):
        fits = False
        #*define the list of bins that will be in return
        ret_bin = bin_list.copy()
        
        #*try to insert the bin in the first possible bin
        for bin in ret_bin:
            if bin.get_available_space() >= item.space:
                bin.items.append(item)
                fits =True
                break
        #*if it doesn't fit add a new bin to the list of bins
        if fits == False:
            ret_bin.append(Bin([item],self.capacity))
        #*returns list of bins
        return ret_bin
    
    
    
    
    
    #! verifying if the node is a leaf
    def isLeaf(self,active_node:BinPackingNode):
        if active_node.items == []:
            return True
        else:
            return False
        
        
        
        
    #! printing a node
    def print_active_node(self,active_node:BinPackingNode):
        print("bins :")
        for bin in active_node.bins:
            print(bin)
        print("items :")
        for item in active_node.items:
            print(item.space)
        print("index :")
        print(active_node.index)
        
        
        
    #!solve the problem using branch and bound method
    def solve(self):
        bin_list,bound = self.find_solution()
        print("BOUND IS : ",bound)
        initial_items = self.items.copy()
        
        #*init the root node
        stack_trace = [BinPackingNode([],initial_items,0)]
        
        
        while stack_trace != [] :
            active_node = stack_trace.pop(0)
            
            #?case of leaf node :
            if self.isLeaf(active_node):
                
                if bound > active_node.cost():
                    bound = active_node.cost()
                    bin_list = active_node.bins
                    

            #?case of normal node
            else:
                #*verify if it is worth to deepen the search
                if(active_node.cost() < bound):
                    #*or delay it (exclude the last option)
                    if (active_node.index != len(active_node.items) - 1):
                        bins = active_node.bins.copy()
                        items = active_node.items.copy()
                        stack_trace.insert(0,BinPackingNode(bins,items,active_node.index+1))
                    #*case if we choose to insert the item
                    bins = active_node.bins.copy()
                    items = active_node.items.copy()
                    item_to_insert = items.pop(active_node.index)
                    stack_trace.insert(0,BinPackingNode(self.insert(bins,item_to_insert),items,0))
                    
                    
                    
                    
                        
        return bin_list,bound
     
bp = BinPacking([Item(20),Item(34),Item(25),Item(46),Item(67),Item(23),Item(45),Item(12),Item(63)],100)
"""
Item(20),Item(34),Item(25),Item(46),Item(67),Item(23),Item(45),Item(12),Item(63)
"""
bins,bound = bp.solve()

for bin in bins:
    for item in bin.items:
        print (item.space,",")
    print("\n\n")