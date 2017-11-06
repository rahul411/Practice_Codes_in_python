#!/usr/bin/python
##  CSE6140 HW1
##  This assignment requires installation of networkx package if you want to make use of available graph data structures or you can write your own!!
##  Please feel free to modify this code or write your own
import networkx as nx
import time
import sys
import heapq
import itertools

class RunExperiments:
    
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count
    a = []
    heapq.heapify(pq)

    def add_task(self, task, priority, parent):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, parent, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, parent, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                priority, count, parent, task = self.entry_finder[task]
                del self.entry_finder[task]
                return task,priority,parent
    
    #This method is for reading the graph. It also initializes a list a and adds entries into priority queue.
    def read_graph(self, filename):
        G = nx.MultiGraph()
        with open(filename, 'r') as nodeData:
            nodes, edges = nodeData.readline().split(' ')
            for i in range(int(edges)):
                sourceNode, destinationNode, weight = nodeData.readline().split(' ')
                G.add_weighted_edges_from([(int(sourceNode), int(destinationNode), int(weight))])

        for i in range(int(nodes)):
            self.a.append(float('inf'))
            self.add_task(i, float('inf'), self.a[i])    
        return G


    def computeMST(self, G):
        mst = nx.MultiGraph()
        costFinal = 0
        while self.entry_finder:
            u, cost, parent = self.pop_task()
            if cost != float('inf'):
               costFinal = costFinal + cost
               #Creating a graph of the mst. This makes it easier for recomputing mst.
               mst.add_weighted_edges_from([(parent,u,cost)])
            for _, nodes, weight in G.edges(u, data ='weight'):
                if nodes not in mst.nodes() and weight < self.a[nodes]:
                    self.a[nodes] = weight
                    self.add_task(nodes, weight, u)
        
        return costFinal, mst

    #Since the mst is a graph, we consider 2 cases:
    # Case1: 2 nodes are immediate neighbours. So compare the edge weights and compute new MSTWeight
    # Case2: The 2 nodes are not neighbours. In this case, adding edge would create cycle. Find edge with largest weight and remove that edge.
    def recomputeMST(self, u, v, weight, mst, MSTweight):
        if mst.has_edge(u,v):
           edgeWeight = mst.get_edge_data(u,v)[0]['weight']    
           if edgeWeight > weight:
              mst.remove_edge(u,v)
              mst.add_weighted_edges_from([(u,v,weight)])
              MSTweight = MSTweight - edgeWeight + weight
        else :
              mst.add_weighted_edges_from([(u,v,weight)])
              cycle = nx.find_cycle(mst)
              maxEdgeWeight = -1
              maxEdgeStart = 0
              maxEdgeEnd = 1
              for startNode, endNode, _ in cycle:
                  edgeWeight = mst.get_edge_data(startNode,endNode)[0]['weight']
                  if maxEdgeWeight < edgeWeight:
                     maxEdgeWeight = edgeWeight
                     maxEdgeStart = startNode
                     maxEdgeEnd = endNode       
              mst.remove_edge(maxEdgeStart,maxEdgeEnd)
              MSTweight = MSTweight + weight - maxEdgeWeight
        return MSTweight, mst          


    def main(self):

        num_args = len(sys.argv)

        if num_args < 4:
            print ("error: not enough input arguments")
            exit(1)

        graph_file = sys.argv[1]
        change_file = sys.argv[2]
        output_file = sys.argv[3]

        #Construct graph
        G = self.read_graph(graph_file)
        start_MST = time.time() #time in seconds
        MSTweight, mst = self.computeMST(G) #call MST function to return total weight of MST
        total_time = (time.time() - start_MST) * 1000 #to convert to milliseconds

        #Write initial MST weight and time to file
        output = open(output_file, 'w')
        output.write(str(MSTweight) + " " + str(total_time) + "\n")


        #Changes file
        with open(change_file, 'r') as changes:
            num_changes = changes.readline()

            for line in changes:
                #parse edge and weight
                edge_data = list(map(lambda x: int(x), line.split()))
                assert(len(edge_data) == 3)

                u,v,weight = edge_data[0], edge_data[1], edge_data[2]
                #call recomputeMST function
                start_recompute = time.time()
                MSTweight, mst = self.recomputeMST(u, v, weight, mst, MSTweight)
                total_recompute = (time.time() - start_recompute) * 1000 # to convert to milliseconds
                #write new weight and time to output file
                output.write(str(MSTweight) + " " + str(total_recompute) + "\n")



if __name__ == '__main__':
    # run the experiments
    runexp = RunExperiments()
    runexp.main()
