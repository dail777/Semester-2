userLogin = {"name": "John Doe", "age": 30, "role": "admin",}
print("sebelum update =", userLogin)

userLogin.update({"email": "joedoe@gmail.com", "phone" : "1234567890"})
print("sesudah update =", userLogin)
