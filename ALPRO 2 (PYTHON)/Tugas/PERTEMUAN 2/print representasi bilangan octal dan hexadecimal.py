    #Fungsi Representasi Octal 
def OctalRep(bilangan):
    bilangan = int(bilangan)
    print(f"{bilangan} dalam Octal = {oct(bilangan)}")
    print(f"Octal literal {oct(bilangan)} = {bilangan}")
   
    #Fungsi Representasi Hexadecimal
def HexadecimalRep(bilangan):
    bilangan = int(bilangan)
    print(f"{bilangan} dalam Hexadecimal = {hex(bilangan)}")
    print(f"Hexadecimal literal {hex(bilangan)} = {bilangan}")
    

    #Panggil fungsi
    OctalRep(15)
    HexadecimalRep(25)