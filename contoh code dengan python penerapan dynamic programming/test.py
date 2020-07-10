def coin_change_greedy(s,f):
  n = len(f)
  print("\nKegiatan berikut dipilih")

  i = 0
  i = i+1
  print(i)

  for j in range(n):
    if s[j] >= f[i]:
      print(j)
      i = j

s = [5 , 1 , 8 , 2 , 9 , 7]
f = [3 , 0 , 4 , 6 , 1 , 9]
coin_change_greedy(s,f)

