print(100*"=")
print(22*'=',"jumlah maksimum matriks dalam dynamic programming",21*"=")
print(100*"=")

print('''
Nama = Ahmad Bujai Rimi
NIM = 20190801217
UNIVERSITAS ESA UNGGUL\n''')

# fungsi untuk menemukan jumlah maksimum sub-matriks
def findMaxSumSubMatrix(mat, k):

	# matrix M X N
	(M, N) = (len(mat), len(mat[0]))

	# proses inputan matriks sehingga jumlah [i][j] disimpan
	# jumlah elemen dalam matriks dari (0, 0) hingga (i, j)
	sum = [[0 for x in range(N)] for y in range(M)]
	sum[0][0] = mat[0][0]

	# proses baris pertama
	for j in range(1, N):
		sum[0][j] = mat[0][j] + sum[0][j - 1]

	# proses kolom pertama
	for i in range(1, M):
		sum[i][0] = mat[i][0] + sum[i - 1][0]

	# sisa proses dari matriks
	for i in range(1, M):
		for j in range(1, N):
			sum[i][j] = mat[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

	max = float('-inf')

	# menemukan jumlah maksimum sub-matriks

	# ukuran sub matriks K x K
	for i in range(k - 1, M):
		for j in range(k - 1, N):

			# catatan (i, j) merupakan kooordinat sudut kanan bawah
			# sub matriks ukuran k

			total = sum[i][j]
			if i - k >= 0:
				total = total - sum[i - k][j]

			if j - k >= 0:
				total = total - sum[i][j - k]

			if i - k >= 0 and j - k >= 0:
				total = total + sum[i - k][j - k]

			if total > max:
				max = total
				p = (i, j)

	# mengembalikan koordinat sudut kanan bawah sub matriks
	return p


if __name__ == '__main__':

	# matriks 5 x 5
	mat = [
		[3, -4, 6, -5, 1],
		[1, -2, 8, -4, -2],
		[3, -8, 9, 3, 1],
		[-7, 3, 4, 2, 7],
		[-3, 7, -5, 7, -6]
	]

	# ukuran sub matriks
	k = 3

	# p berisi koordinat sudut kanan bawah dari sub sub matriks
	(x, y) = findMaxSumSubMatrix(mat, k)

	# mencetak jumlah maksimum sub matriks
	for i in range(k):
		for j in range(k):
			print(mat[i + x - k + 1][j + y - k + 1], end=' ')
		print()
