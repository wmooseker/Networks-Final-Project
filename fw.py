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
	dist = list(map(lambda i : list(map(lambda j : j , i)) , graph))

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
				dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
	printSolution(dist)


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
	     [INF, 1, INF, 3,0,2,INF,4,INF],
	     [INF, INF, 9, INF,2,0,INF,INF,6],
	     [INF, INF, INF, 3,INF,INF,0,5,INF],
	     [INF, INF, INF, INF,4,INF,5,0,8],
	     [INF, INF, INF, INF,INF,6,INF,8,0]
        ]

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
dot.edge('E', 'H', label = '4')
dot.edge('E', 'F', label = '2')
dot.edge('H', 'G', label = '5')
dot.edge('H', 'I', label = '8')
dot.edge('F', 'I', label = '6')

dot.view()

r = Graph(comment = 'result')


# Print the solution
floydWarshall(graph);
