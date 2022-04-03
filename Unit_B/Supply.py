# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: kd5eyn
# Collaborators:
# Sources: Introduction to Algorithms, Cormen, https://www.w3schools.com/python/ref_string_isnumeric.asp
#################################

class Edge:

    def __init__(self, origin, dest, weight):
        self.origin = origin
        self.dest = dest
        self.weight = weight

class DisjointSet:

    def __init__(self, n):
        self.set = []
        for i in range(n):
            self.set.append(i)

    def find(self, v):
        if(self.set[v] == v):
            return v
        return self.find(self.set[v])
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.set[root_u] = root_v


class Supply:  

    def __init__(self):
        return

    #Ids should be a dictionary mapping an id to the vertex.
    def parse_list(self, lines, ids):
        graph = {}
        #skip the first line because 1 is the size
        num_v = 0
        num_e = 0
        
        for line in lines[1:]:
            #Split the line by spaces into an array
            line_arr = line.split()
            if len(line_arr) == 2:
                #Add another vertex to the adjacency list
                ids[line_arr[0]] = num_v
                graph[line_arr[0]] = []
                num_v += 1
            elif len(line_arr) == 3:
                #Adding an edge to the adjacency list
                graph[line_arr[0]].append(Edge(line_arr[0], line_arr[1], int(line_arr[2])))
                num_e += 1
        
        size = lines[0].split()
        if num_v != int(size[0]) or num_e != int(size[1]):
            print("Warning! Size of graph incorrect!")
        
        return graph


    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        edgeWeightSum = 0

        ids = {}
        # your function to compute the result should be called here
        graph = self.parse_list(file_data, ids)
        print(ids["p1"])
        start = "p1"
        print(f"Destination: {graph[start][0].dest} Weight: {graph[start][0].weight}")
        return edgeWeightSum