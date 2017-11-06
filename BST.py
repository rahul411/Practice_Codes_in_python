import queue 
import copy

class Node:
	def __init__(self, val, label=0):
		self.val = val
		self.label = label
		self.left = None
		self.right = None 

def insert(root, node):
	if root == None:
		root = node
	if node.val < root.val:
		if root.left == None:
			root.left = node
		else:
			insert(root.left,node)
	else:
		if root.right == None:
			root.right = node
		else:
			insert(root.right,node)
def height(root):
	if root == None:
		return 0
	return max(height(root.left),height(root.right)) + 1	

def diameter(root):
	if root == None:
		# height = 0
		return 0, 0

	# lheight = height(root.left)
	# rheight = height(root.right)
	# lh=rh=1
	rdia, rh = diameter(root.right)
	ldia, lh = diameter(root.left)
	# ans = max(ldia + rdia + 1, ans)
	# print(lh,rh)
	return max(lh+rh+1,ldia,rdia), max(lh,rh)+1	

def inorder(root):
	if root == None:
		return	
	inorder(root.left)
	print(root.val)
	inorder(root.right)

def search(root, val):
	if root == None:
		return False
	if root.val == val:
		return True
	elif root.val > val:
		return search(root.left, val)
	else:
		return search(root.right,val)			

def minValueNode(root):
	current = root
	while current.left is not None:
		current = current.left
	return current	

def deleteNode(root, key):
	if root == None:
		return root
	if key < root.val:
		root.left = deleteNode(root.left, key)
	elif key > root.val:
		root.right = deleteNode(root.right, key)
	else:
		if root.left == None:
			temp = root.right
			root = None
			return temp
		elif root.right == None:
			temp == root.left
			root = None
			return temp
		else:
			temp = minValueNode(root.right)
			root.key = temp.key
			root.right = deleteNode(root.right,temp.key)	
	return root		


def BFSTravel(q):
	if q.empty():
		return 
	root = q.get()
	if root == None:
		return
	print(root.val)
	q.put(root.left)
	BFSTravel(q)
	q.put(root.right)
	BFSTravel(q)

def haspathSum(root,sumval):
	if root == None:
		return sumval == 0	
	else:
		sumval = sumval - root.val
		return haspathSum(root.left,sumval) or haspathSum(root.right,sumval)

def printPaths(root,path):
	if root == None:
		return 
	path.append(root.val)
	if root.left == None and root.right == None:
		print(path)
		path = []
	else:
		printPaths(root.left,copy.deepcopy(path))
		printPaths(root.right,copy.deepcopy(path))		

def mirror(root):
	if root == None:
		return 
	else:
		mirror(root.left)
		mirror(root.right)
		root.left, root.right = root.right, root.left
def doubleTree(root):
	if root == None:
		return
	doubleTree(root.left)
	doubleTree(root.right)
	temp = copy.deepcopy(root.left)
	root.left = Node(root.val)
	root.left.left = temp
	
def isSameTree(root1,root2):
	if root1 == None and root2 == None:
		return True
	elif root1==None or root2 == None:
		return False
	if root1.val != root2.val:
		return False		
	else:
		return isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)	

def maxPathUniLabel(root):
	if root == None:
		return 0,0
	rdia,rh = maxPathUniLabel(root.right)
	if not root.right or root.label != root.right.label:
		rh=0
	ldia,lh = maxPathUniLabel(root.left)
	if not root.left or root.label != root.left.label:
		lh = 0

	return max(lh+rh+1,ldia,rdia), max(lh,rh) + 1	


			
# r1 = Node(1)
# insert(r1,Node(2))
# insert(r1,Node(3))
# insert(r1,Node(4))
# insert(r1,Node(5))
# # insert(r1,Node(5))
# print(height(r1))
# # ans = -5
# print(diameter(r1))
# # print(ans)
# r2 = Node(3)
# insert(r2,Node(4))
# insert(r2,Node(2))
# insert(r2,Node(3))
# insert(r2,Node(4))
# insert(r2,Node(6))
# print(isSameTree(r1,r2))
# print(haspathSum(r,5))
# printPaths(r,[])
# doubleTree(r)
# mirror(r)
# print(search(r,10))
# r = deleteNode(r,5)
# print(inorder(r))
# q = queue.Queue()
# q.put(r)
# BFSTravel(q)


# A = [1,1,1,2,3,4,5,1,1,1,1,1]
# E = [1,2,1,3,2,4,2,5,3,6,3,7,4,8,4,9,9,10,9,11,10,12]

# nodes = [Node(i,A[i]) for i in range(len(A))]
# e = len(E)
# prev = -1
# for i in range(0,e,2):
# 	if E[i] == prev:
# 		nodes[E[i]-1].right = nodes[E[i+1]-1]
# 	else:
# 		nodes[E[i]-1].left = nodes[E[i+1]-1]
# 	prev = E[i]	
# dia,h = maxPathUniLabel(nodes[0])
# print(dia)
# inorder(nodes[0])