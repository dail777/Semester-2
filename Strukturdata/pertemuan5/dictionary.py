userLogin = {"name": "John Doe", "age": 30, "role": "admin",}
print(f"nama : {userLogin['name']}")  # Output: John Doe
print(f"umur : {userLogin['age']}")   # Output: 30
print(f"peran : {userLogin['role']}")  # Output: admin
print(f"tipe data : {type(userLogin)}")  # Output: <class 'dict'>

# Menambahkan elemen baru ke dalam dictionary
userLogin["email"] = "john.doe@example.com"
print(f"email : {userLogin['email']}")  # Output: john.doe@example.com

#update value
userLogin["age"] = 31
print(f"umur : {userLogin['age']}")   # Output: 31

#menghapus elemen dari dictionary
del userLogin["email"]
print(f"setelah menghapus email: {userLogin}")  # Output: {'name': 'John Doe', 'age': 31, 'role': 'admin'}

#menghapus semua data
# userLogin.clear()
# print(f"setelah menghapus semua data: {userLogin}")  # Output:
print(" ----------------------------- ")
#nested dictionary
tableLogins = {
    "user1": {"name": "Alice", "age": 28, "role": "user"},
    "user2": {"name": "Bob", "age": 35, "role": "admin"},
    "user3": {"name": "Charlie", "age": 22, "role": "user"},
}

print(tableLogins)
print(" ----------------------------- ")    
print(f"nama user1 : {tableLogins['user1']['name']}")  # Output: Alice  
print(f"umur user1 : {tableLogins['user1']['age']}")   # Output: 28
print(f"peran user1 : {tableLogins['user1']['role']}")  # Output: user
print(" ----------------------------- ")
print(f"nama user2 : {tableLogins['user2']['name']}")  # Output: Bob
print(f"umur user2 : {tableLogins['user2']['age']}")
print(f"peran user2 : {tableLogins['user2']['role']}")  # Output: admin
print(" ----------------------------- ")
print(f"nama user3 : {tableLogins['user3']['name']}")
print(f"umur user3 : {tableLogins['user3']['age']}")
print(f"peran user3 : {tableLogins['user3']['role']}")  # Output: user
print(" ----------------------------- ")
