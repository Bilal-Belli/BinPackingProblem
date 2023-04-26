from testParameters import *
class Item:
	def __init__(self):
		self.weight = 0
		self.mark = False
	def getWeight(self):
		return	self.weight
	def getMark(self):
		return self.mark
	def setWeight(self, weight):
		self.weight = weight
	def setTrue(self):
		self.mark = True
	def setFalse(self):
		self.mark = False
	def __repr__(self):
		return str(self)
	def __str__(self):
		return "item weight: " + str(self.weight)
class Bin:
	def __init__(self):
	#Set B of items in the bin and cap is the capacity of the bin
		self.B = []
		self.cap = bin_size
	def getCapacity(self):
		return self.cap
	def getB(self):
		return self.B
	#packing function returns true or false to
	def pack(self, item3):
		if (self.cap - item3.getWeight()) < 0:
			print ("item cannot be packed\n")
		else:
			self.B.append(item3.getWeight())
			self.cap = self.cap - item3.getWeight()
	def __str__(self):
		strp = "Items in Bin: "
		for item5 in self.B:
			strp = strp  + str(item5) + ", "
		return  strp
	def __repr__(self):
		return str(self)
class BinPacking:
	def __init__(self, S, BinList):
		#Set S of items to be packed in Set of Bins BinList
		self.S = S
		self.BinList = [Bin()]
	def getBinList(self):
		return self.BinList
	def getS(self):
		return self.S
	def descending(self):
		intar = []
		for item in self.S:
			intar.append(item.getWeight())
		intar.sort(reverse = True)
		self.S = []
		for int in intar:
			item = Item()
			item.setWeight(int)
			self.S.append(item)
	def __str__(self):
		strp = "Weight of each bin: "
		for bin2 in self.BinList:
			strp = strp + str(bin_size - bin2.getCapacity()) + ", "
		return strp
	def __repr__(self):
		return str(self)
class NextFit (BinPacking):
	def packItems(self):
		binl = self.getBinList()
		bin = binl[0]
		for item in self.S:
			if item.getWeight() <= bin.getCapacity():
				bin.pack(item)
			else:
				newBin = Bin()
				binl.append(newBin)
				bin = newBin
				bin.pack(item)
	def returnNF(self):      
			boxContent=[]
			count = 0
			binl = self.getBinList()
			for bin in binl:
				newBoxContent=[]
				for item in bin.getB():
					# ici le contenu du bins
					newBoxContent.append(item)
				boxContent.append(newBoxContent)
				count = count + 1
			NB_bins = count
			return NB_bins,boxContent
	def NFdescending(self):
		self.descending()
		print(self.S)
		self.packItems()