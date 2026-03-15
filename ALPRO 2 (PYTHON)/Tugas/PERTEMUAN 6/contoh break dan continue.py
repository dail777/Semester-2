for i in range(1, 6):
    if i == 3:
        break
    print(f"INI DALAM LOOP : {i}")
print("INI DILUAR LOOP")

for i in range(1, 6):
    if i == 3:
        continue
    print(f"INI DALAM LOOP : {i}")
print("INI DILUAR LOOP")