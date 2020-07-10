print(100*"=")
print(29*'=',"program Breadth First Search(BFS)",28*"=")
print(100*"=")

print('''
Nama = Ahmad Bujai Rimi
NIM = 20190801217
UNIVERSITAS ESA UNGGUL\n''')

print("kali ini saya akan membuat program yaitu pada masalah\npasokan air dengan menggunakan breadth first search(BFS)\n")

'''
dalam permasalahan ini yaitu mengatur koneksi untuk pasokan air dalam sebuah kota dan 
mengetahui jumlah maksimum kota yang dapat pemasokan air
'''

# fungsi untuk melakukan BFS
def bfsUtil(v, vis, adj, src):
    # Tandai sumber saat ini dikunjungi
    vis[src] = True

    # Queue untuk BFS
    q = []

    # Dorong src ke queue
    q.append(src)

    count = 0
    while (len(q) != 0):
        p = q[0]

        for i in range(len(adj[p])):

            # Ketika kota yang berdekatan tidak dikunjungi dan
            # tidak di blokir, push city ke dalam queue.
            if (vis[adj[p][i]] == False and v[adj[p][i]] == 0):
                count += 1
                vis[adj[p][i]] = True
                q.push(adj[p][i])

            # ketika kota yang berdekatan tidak dikunjungi
            # tetapi diblokir sehingga kota yang diblokir adalah
            # tidak pushed kedalam queue
            elif (vis[adj[p][i]] == False and v[adj[p][i]] == 1):
                count += 1
        q.remove(q[0])

    return count + 1


# fungsi Utility ke perform BFS
def bfs(N, v, adj):
    vis = [0 for i in range(N + 1)]
    mx = 1

    # menandai dikunjungi array yang salah
    for i in range(1, N + 1, 1):
        vis[i] = False

    # Memperiksa setiap kota
    for i in range(1, N + 1, 1):

        # Memperiksa bahwa kota tidak diblokir
        # dan tidak dikunjungi
        if (v[i] == 0 and vis[i] == False):
            res = bfsUtil(v, vis, adj, i)
            if (res > mx):
                mx = res

    return mx


# Driver Code
if __name__ == '__main__':
    N = 4

    # Menunjukkan jumlah kota
    adj = [[] for i in range(N + 1)]
    v = [0 for i in range(N + 1)]

    # Fungsi dari Adjacency list untuk menunjukkan jalan
    # antara kota u dan v
    adj[1].append(2)
    adj[2].append(1)
    adj[2].append(3)
    adj[3].append(2)
    adj[3].append(4)
    adj[4].append(3)

    # array untuk menyimpan apakah
    # kota tersebut diblokir atau tidak
    v[1] = 0
    v[2] = 1
    v[3] = 1
    v[4] = 0

    print('maka hasil maksimum kota yang tidak diblokir untuk pemasokan air yaitu adalah')
    print(bfs(N, v, adj))

'''
kesimpulannya:
Jika kota 1 dipilih, maka air disuplai dari kota 1 ke 2. 
Jika kota 4 dipilih, maka air disuplai dari kota 4 hingga 3 
maka maksimum dari 2 kota dapat disuplai dengan air.
'''