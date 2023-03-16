import copy   # pour deep copying lists
class Node:
    def __init__(self, wRemaining, level, numBoxes, boxContents):
        # initialize a Node object avec les parameters
        self.wRemaining = wRemaining
        self.level = level
        self.numBoxes = numBoxes
        self.boxContents = boxContents # Content of each box at the end
    def getLevel(self):
        # return the level of the node
        return self.level
    def getNumberBoxes(self):
        # return the number of boxes in the node
        return self.numBoxes
    def getWRemainings(self):
        # return the list of remaining capacities of all bins
        return self.wRemaining
    def getWRemaining(self, i):
        # return the remaining capacity of the i-th bin
        return self.wRemaining[i]

def branchAndBound(n, c, w):
    # initialize the minimum number of boxes to n (on met each objet dans 1 box donc on aura n boxes au debut)
    minBoxes = n
    # create an empty list to store Node objects
    Nodes = []
    # create an empty list to store the contents of each box
    boxContents = [[] for _ in range(n)]
    # initialize the remaining capacity of each bin to c (we'll have n boxes of c capacity)
    wRemaining = [c] * n
    # initialize the number of boxes to 0
    numBoxes = 0
    # create a new Node object with the above parameters
    curN = Node(wRemaining, 0, numBoxes, boxContents)
    # add the current node to the list of nodes
    Nodes.append(curN)
    # loop until there are no more nodes left to explore
    while len(Nodes) > 0:
        # get the last node added to the list of nodes
        curN = Nodes.pop()
        # get the level of the current node
        curLevel = curN.getLevel()
        # if all objects have been assigned to boxes and the current solution is better than the current best solution
        if curLevel == n and curN.getNumberBoxes() < minBoxes:
            # update the minimum number of boxes
            minBoxes = curN.getNumberBoxes()
            # deep copy the box contents to store the current best solution
            boxContents = copy.deepcopy(curN.boxContents)
        else:
            # get the index of the next box to add an object to
            indNewBox = curN.getNumberBoxes()
            # only consider adding a new box if the current solution is still potentially better than the current best solution
            if indNewBox < minBoxes:
                # get the weight of the object at the current level
                wCurLevel = w[curLevel]
                # consider adding the object to each box
                for i in range(indNewBox + 1):
                    # only add the object to a box if there is enough remaining capacity in the box and there are more objects to assign
                    if curLevel < n and curN.getWRemaining(i) >= wCurLevel:
                        # create a new list of remaining capacities by copying the current list and subtracting the weight of the object from the appropriate bin
                        newWRemaining = curN.getWRemainings().copy()
                        newWRemaining[i] -= wCurLevel
                        # create a new list of box contents by copying the current list and appending the current object to the appropriate box
                        newBoxContents = copy.deepcopy(curN.boxContents)
                        newBoxContents[i].append(curLevel + 1)
                        # create a new Node object with the updated parameters
                        if i == indNewBox:
                            newNode = Node(newWRemaining, curLevel + 1, indNewBox + 1, newBoxContents)
                        else:
                            newNode = Node(newWRemaining, curLevel + 1, indNewBox, newBoxContents)
                        Nodes.append(newNode)
    return minBoxes, boxContents