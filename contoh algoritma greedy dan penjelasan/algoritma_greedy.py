print(100*"=")
print(25*'=',"Contoh program algoritma greedy dan penjelasannya",24*"=")
print(100*"=")

print('''
Nama = Ahmad Bujai Rimi
NIM = 20190801217
UNIVERSITAS ESA UNGGUL''')

"""Implementasi berikut mengasumsikan bahwa kegiatan
sudah diurutkan berdasarkan waktu selesai mereka"""

"""Mencetak serangkaian kegiatan maksimum yang dapat dilakukan oleh a
satu orang, satu per satu"""
# n --> Total jumlah kegiatan
# s[]-->  Array yang berisi waktu mulai semua aktivitas
# f[] --> Array yang berisi waktu selesai semua kegiatan

def printMaxActivities(s , f ):
	n = len(f)
	print ("\nKegiatan berikut dipilih")

	#  Aktivitas pertama selalu dipilih
	i = 0
	print (i)

	#  Pertimbangkan sisa kegiatan
	for j in range(n):

		# Jika kegiatan ini memiliki waktu mulai lebih besar dari
		# atau sama dengan waktu selesai sebelumnya
		# kegiatan yang dipilih, lalu pilih
		if s[j] >= f[i]:
			print (j)
			i = j

#  Program driver untuk menguji fungsi di atas
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)