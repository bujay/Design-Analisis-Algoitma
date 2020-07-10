print(100*"=")
print(29*'=',"program penerapan Depth-first search(DFS)",28*"=")
print(100*"=")

print('''
Nama = Ahmad Bujai Rimi
NIM = 20190801217
UNIVERSITAS ESA UNGGUL\n''')

print("ini adalah contoh program Depth-first search(DFS) dengan menggunakan representasi list adjency\n")

'''
catetan:
 Depth-first search(DFS) merupakan algoritma untuk melintasi atau mencari struktur data pohon atau grafik. 
 Algoritme dimulai pada simpul akar (memilih beberapa simpul sembarang sebagai simpul akar dalam kasus grafik) 
 dan mengeksplorasi sejauh mungkin di sepanjang setiap cabang sebelum mundur. Jadi untuk memulai dari root atau 
 sembarang node dan tandai node tersebut dan pindah ke node yang tidak bertanda yang berdekatan dan 
 lanjutkan loop ini sampai tidak ada node yang berdekatan yang tidak ditandai. Akhirnya cetak node di jalur.

algoritmanya:
1. membuat fungsi rekursif untuk mengambil indeks node dan array
2. melintasi semua simpul yang adjacent dan nodes memanggil fungsi rekursif dengan index adjacent node 
'''

# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited[v] = True
		print(v, end = ' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph)+1)

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

# Driver code

# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)