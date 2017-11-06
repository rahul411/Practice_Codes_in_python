import queue 

def dfs(graph,start, visited = []):
	visited += [start]
	for vertex in graph[start]:
		if vertex not in visited:
			dfs(graph,vertex,visited)
	return visited		

def dfs_stack(graph,start):

	visited,stack = [start],[start]
	while stack:
		vertex = stack.pop()
		# if vertex not in visited:
			# print(vertex)
			# visited.append(vertex)
			# print(graph[vertex])
		for vertices in graph[vertex]:	
			if vertices not in visited:
				visited.append(vertices)
				stack.append(vertices)

	return visited

def bfs(graph,start):
	visited,q = [],queue.Queue()
	q.put(start)
	while not q.empty():
		vertex = q.get()
		if vertex not in visited:
			visited.append(vertex)
			for vertices in graph[vertex]:
				q.put(vertices) 
	return visited			

def isCycle(graph,start):

	visited,stack = [],[start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			# print(vertex)
			visited.append(vertex)
			# print(graph[vertex])
			for vertices in graph[vertex]:	
				stack.append(vertices)
		else:
			return True		

	return False

def topologicalSortUtility(graph,current,visited=[], stack = []):
		visited.append(current)
		for i in graph[current]:
			if i not in visited:
				topologicalSortUtility(graph,i,visited,stack)
			
		stack.insert(0,current)

def topologicalSort(graph):
	visited = []
	stack = []
	for i in graph:
		if i not in visited:
			topologicalSortUtility(graph,i,visited,stack)
	print(stack)		
			
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['E'])}

graph1 = {0: [1, 3], 1: [3],
                    2: [1,4,5], 3: [2,4,5], 4: [5],
                    5: []}     
topologicalSort(graph1)                        
# print(dfs(graph,'A'))      
# print(dfs_stack(graph,'A')) 
# print(isCycle(graph,'A')) 	

# class Graph:

# 	graph = {}

# 	def addEdge(self,u,v):
# 		if u not in self.graph:
# 			self.graph[u] = [v]
# 		else:
# 			self.graph[u].append(v)
# 		if v not in self.graph:
# 			self.graph[v] = []	

# g = Graph()			
# g.addEdge(1,2)
# g.addEdge(1,3)
# g.addEdge(3,4)
# print(g.graph)
# print(isCycle(g.graph,1))