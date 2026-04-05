my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
   found = my_list [i] == to_find
   if found:
       break

if found:
    print(f"{to_find} ditemukan pada indeks {i}.")
else:
    print(f"{to_find} tidak ditemukan dalam list.")