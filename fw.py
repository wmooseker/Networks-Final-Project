# Python Program for Floyd Warshall Algorithm

from graphviz import Graph

# Number of vertices in the graph
V = 9

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other
INF  = 99999

# Solves all pair shortest path via Floyd Warshall Algorithm
def floydWarshall(graph):
	""" dist[][] will be the output matrix that will finally
		have the shortest distances between every pair of vertices """
	""" initializing the solution matrix same as input graph matrix
	OR we can say that the initial values of shortest distances
	are based on shortest paths considering no
	intermediate vertices """
	seq = list(map(lambda i : list(map(lambda j : j , i)) , graph))
	dist = list(map(lambda i : list(map(lambda j : j , i)) , graph))
	for i in range(V):
		for j in range(V):
			seq[i][j] = j
	""" Add all vertices one by one to the set of intermediate
	 vertices.
	 ---> Before start of an iteration, we have shortest distances
	 between all pairs of vertices such that the shortest
	 distances consider only the vertices in the set
	{0, 1, 2, .. k-1} as intermediate vertices.
	  ----> After the end of a iteration, vertex no. k is
	 added to the set of intermediate vertices and the
	set becomes {0, 1, 2, .. k}
	"""
	for k in range(V):

		# pick all vertices as source one by one
		for i in range(V):

			# Pick all vertices as destination for the
			# above picked source
			for j in range(V):

				# If vertex k is on the shortest path from
				# i to j, then update the value of dist[i][j]
				# dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
				# seq[i][j] = k
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
					seq[i][j] = seq[i][k]
	return seq
	# printSolution(seq)


# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances / between every pair of vertices")
    print("       A      B      C      D      E      F      G      H     I")
    print("")
    letterArray = ['A','B','C','D','E','F','G','H','I']
    for i in range(V):
        print(letterArray[i], end='')
        for j in range(V):
            if(dist[i][j] == INF):
                print ("%7s" %("INF"), end='')
            else:
                print ("%7d" %(dist[i][j]), end='')
            if j == V-1:
                print ("")

graph = [[0,2,INF,5,INF,INF,INF,INF,INF],
             [2,0,7,INF,1,INF,INF,INF,INF],
             [INF, 7, 0,INF,INF,9,INF,INF,INF],
             [5, INF, INF, 0, 3, INF,3,INF,INF],
	     [INF, 1, INF, 3,0,2,INF,30,INF],
	     [INF, INF, 9, INF,2,0,INF,INF,6],
	     [INF, INF, INF, 3,INF,INF,0,5,INF],
	     [INF, INF, INF, INF,4,INF,5,0,8],
	     [INF, INF, INF, INF,INF,6,INF,8,0]
        ]
def init_graph():
	dot = Graph(comment = 'Topology')
	dot.node('A')
	dot.node('B')
	dot.node('C')
	dot.node('D')
	dot.node('E')
	dot.node('F')
	dot.node('G')
	dot.node('H')
	dot.node('I')

	dot.edge('A', 'B', label = '2')
	dot.edge('A', 'D', label = '5')
	dot.edge('B', 'C', label = '7')
	dot.edge('B', 'E', label = '1')
	dot.edge('C', 'F', label = '9')
	dot.edge('D', 'E', label = '3')
	dot.edge('D', 'G', label = '3')
	dot.edge('E', 'H', label = '30')
	dot.edge('E', 'F', label = '2')
	dot.edge('H', 'G', label = '5')
	dot.edge('H', 'I', label = '8')
	dot.edge('F', 'I', label = '6')

	dot.view()

def gen_graph(arr):
	dot = Graph(comment = 'Topology')

	if 0 in arr:
		dot.node('A', color="red")
	else:
		dot.node('A')
	if 1 in arr:
		dot.node('B', color="red")
	else:
		dot.node('B')
	if 2 in arr:
		dot.node('C', color="red")
	else:
		dot.node('C')
	if 3 in arr:
		dot.node('D', color="red")
	else:
		dot.node('D')
	if 4 in arr:
		dot.node('E', color="red")
	else:
		dot.node('E')
	if 5 in arr:
		dot.node('F', color="red")
	else:
		dot.node('F')
	if 6 in arr:
		dot.node('G', color="red")
	else:
		dot.node('G')
	if 7 in arr:
		dot.node('H', color="red")
	else:
		dot.node('H')
	if 8 in arr:
		dot.node('I', color="red")
	else:
		dot.node('I')
	convert = ['A','B','C','D','E','F','G','H','I']

	for i in range(len(arr)-1):
		dot.edge(convert[arr[i]],convert[arr[i+1]], color="red")
	dot.edge('A', 'B', label = '2')
	dot.edge('A', 'D', label = '5')
	dot.edge('B', 'C', label = '7')
	dot.edge('B', 'E', label = '1')
	dot.edge('C', 'F', label = '9')
	dot.edge('D', 'E', label = '3')
	dot.edge('D', 'G', label = '3')
	dot.edge('E', 'H', label = '30')
	dot.edge('E', 'F', label = '2')
	dot.edge('H', 'G', label = '5')
	dot.edge('H', 'I', label = '8')
	dot.edge('F', 'I', label = '6')

	dot.view()

# def result_graph(node1, node2):
# 	r = Graph(comment = 'result')

seq = floydWarshall(graph)

def find_path(node1, node2):
	n1 = 0
	n2 = 0

	if node1 == "A" or node1 == "a":
		n1 = 0
	elif node1 == "B" or node1 == "b":
		n1 = 1
	elif node1 == "C" or node1 == "c":
		n1 = 2
	elif node1 == "D" or node1 == "d":
		n1 = 3
	elif node1 == "E" or node1 == "e":
		n1 = 4
	elif node1 == "F" or node1 == "f":
		n1 = 5
	elif node1 == "G" or node1 == "g":
		n1 = 6
	elif node1 == "H" or node1 == "h":
		n1 = 7
	elif node1 == "I" or node1 == "i":
		n1 = 8

	if node2 == "A" or node2 == "a":
		n2 = 0
	elif node2 == "B" or node2 == "b":
		n2 = 1
	elif node2 == "C" or node2 == "c":
		n2 = 2
	elif node2 == "D" or node2 == "d":
		n2 = 3
	elif node2 == "E" or node2 == "e":
		n2 = 4
	elif node2 == "F" or node2 == "f":
		n2 = 5
	elif node2 == "G" or node2 == "g":
		n2 = 6
	elif node2 == "H" or node2 == "h":
		n2 = 7
	elif node2 == "I" or node2 == "i":
		n2 = 8
	node = n1
	arr = [n1]
	while(node != n2):
		node = seq[node][n2]
		arr.append(node)
	gen_graph(arr)





# # Print the solution
# floydWarshall(graph);
