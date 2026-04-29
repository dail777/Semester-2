bilangan = 2
print(bilangan)

def kuadrat():
    global bilangan
    bilangan = 5 
    hasil = bilangan ** 2
    return hasil

print(kuadrat())
print(bilangan)
