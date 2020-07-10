print(100*"=")
print(37*'=',"program penerapan graph",38*"=")
print(100*"=")

print('''
Nama = Ahmad Bujai Rimi
NIM = 20190801217
UNIVERSITAS ESA UNGGUL\n''')

print('''graph dapat di implementasikan menjadi 2 yaitu: 
1. Adjacency list
2. Adjacency matrix\n''')

print(60*"*")

print("kali ini saya akan membuat program yaitu mengimplementasikan\n\t\tgraph dengan menggunakan Adjacency list")

print(60*"*")

def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

# tambahkan edge antara vertex v1 dan v2 dengan edge weight
def add_edge(v1, v2, e):
  global graph
  # memeriksa apakah vertex v1 merupakan vertex yang valid
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # memeriksa apakah vertex v2 adalah vertex yang valid
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # karena kode ini tidak terbatas pada yang diarahkan atau
    # grafik tidak terarah, keunggulan antara v1 v2 tidak
    # menyiratkan bahwa ada tepi antara v2 dan v1
    temp = [v2, e]
    graph[v1].append(temp)

# mencetak grafiknya
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

# kode driver
graph = {}
# menyimpan jumlah vertices ke dalam grafik
vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# menambahkan edge di antara vertices
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()

print ("Internal representation: ", graph)