class Heap:
	currentSize = 0
	heapList = [0]

	def percUp(self):
		i = self.currentSize
		while i//2:
			if self.heapList[i] < self.heapList[i//2]:
				self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
			i = i//2	

	def insert(self, data):
		self.heapList.append(data)
		self.currentSize+=1
		self.percUp()

	def minChild(self,i):
		if i*2+1>self.currentSize:
			return i*2
		if self.heapList[i]>self.heapList[i*2]:
			return i*2
		else:
		 	return i*2+1		

	def percDown(self,i):
		# i = 1
		while i*2 <= self.currentSize:
			mc = self.minChild(i)
			self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]
			i = mc


	def delMin(self):
		print(self.heapList[1])
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize-=1
		self.heapList.pop()
		self.percDown(1)	

	def delElement(self,data):
		index = self.heapList.index(data)
		self.heapList[index] = self.heapList[self.currentSize]
		self.currentSize-=1
		self.heapList.pop()
		self.percDown(index)



a = Heap()
a.insert(2)
a.insert(1)
print(a.heapList)
a.delElement(1)
print(a.heapList)	
