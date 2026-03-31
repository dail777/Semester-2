my_list = [10, 1, 8 , 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0] 
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) - 1 - i] = my_list[len(my_list) - 1 - i], my_list[i]

print("for looping :", my_list)

for i in range(100 // 2):
    my_list[i], my_list[len(my_list) - 1 - i] = my_list[len(my_list) - 1 - i], my_list[i]

print("for looping 2 :", my_list)