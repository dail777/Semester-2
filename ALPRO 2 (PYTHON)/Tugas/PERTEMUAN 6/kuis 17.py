kataInput = str(input("Masukan kata : "))
user_word = kataInput.upper()

for kata in range(len(user_word)):
    kata = user_word[kata]
    if kata == "A" or kata == "I" or kata == "U" or kata == "E" or kata == "O":
        continue
    print(kata)
