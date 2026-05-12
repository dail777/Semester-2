tuple1 = (5, 4, 3, 2)
print("tuple sebelum dimodifikasi =", tuple1)

list1 = list(tuple1) 
list1.append(1) 
tuple1 = tuple(list1)
print("tuple setelah dimodifikasi =", tuple1)

list1.remove(4)
print("tuple setelah dimodifikasi =", tuple1)