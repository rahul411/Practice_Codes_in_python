class TrieNode:
	def __init__(self):
		self.characters = [None]*26
		self.endOfKey = False
class TrieTree:
	def __init__(self):
		self.root = TrieNode()
	def getKey(self, char):
		return ord(char) - ord('a')

	def insert(self,key):
		# n = len(key)
		crawl = self.root
		for i in key:
			index = self.getKey(i)
			if not crawl.characters[index]:
				crawl.characters[index] = TrieNode()
			crawl = crawl.characters[index]
		crawl.endOfKey = True

	def search(self, key):
		crawl = self.root
		# n = len(key)
		for i in key:
			index = self.getKey(i)
			if not crawl.characters[index]:
				return False
			else:
				crawl = crawl.characters[index]
		return crawl != None

keys = ["wwwgooglecom","pqrcom"]
output = ["Not present in trie",
              "Present in tire"]
 
    # Trie object
t = TrieTree()
 
    # Construct trie
for key in keys:
    t.insert(key)
 
    # Search for different keys
print("{} ---- {}".format("the",output[t.search("com")]))
print("{} ---- {}".format("these",output[t.search("these")]))
print("{} ---- {}".format("their",output[t.search("their")]))
print("{} ---- {}".format("thaw",output[t.search("thaw")]))		