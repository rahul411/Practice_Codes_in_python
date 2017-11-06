from collections import defaultdict

class MinHeap:
	def __init__(self):
		self.array = []
		self.size = 0
		self.pos = []

	def heapify(self,index):
		smallest = index
		left = 2*index + 1
		right = 2*index + 2
		if left<self.size and self.array[smallest][1]>self.array[left][1]:
			smallest = left
		if right < self.size and self.array[smallest][1]>self.array[right][1]:
			smallest = right
		if smallest != index:
			self.pos[self.array[smallest][0]],self.pos[self.array[index][0]] = self.pos[self.array[index][0]],self.pos[self.array[smallest][0]]
			self.array[smallest], self.array[index] = self.array[index], self.array[smallest]
			self.heapify(smallest)		

	def decreaseKey(self, v, w):
		position = self.pos[v]
		self.array[position][1] = w
		while position>0 and self.array[position]<self.array[position//2]:
			self.pos[self.array[position][0]] = position//2
			self.pos[self.array[position//2][0]] = position
			self.array[position], self.array[position//2] = self.array[position//2], self.array[position]
			position=position//2

	def extractMin(self):
		if self.size == 0:
			return None
		minElement = self.array[0]
		self.pos[self.array[0][0]] = self.size-1
		self.pos[self.array[self.size-1][0]] = 0
		self.array[0] = self.array[self.size-1]
		self.size-=1
		self.heapify(0)
		return minElement		


class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, u, v, w):
		self.graph[u].insert(0,[v,w])
		self.graph[v].insert(0,[u,w])

	def dijsktra(self, src):
		dist = []
		minHeap = MinHeap()
		minHeap.size = self.V
		for i in range(self.V):
			dist.append(99999)
			minHeap.array.append([i,dist[i]])
			minHeap.pos.append(i)
		minHeap.pos[src] = src
		dist[src] = src
		minHeap.decreaseKey(src,0)
		while minHeap.size != 0:
			[u,w] = minHeap.extractMin()
			for node in self.graph[u]:
				v=node[0]
				w=node[1]
				if minHeap.pos[v] < minHeap.size and dist[v]>dist[u] + w:
					dist[v] =  dist[u] + w
					minHeap.decreaseKey(v,dist[v])
		print(dist)			

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijsktra(0)
