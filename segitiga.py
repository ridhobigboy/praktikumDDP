string = " "
bar = 1 


x = int (input("masukan angka = "))

# looping baris
while bar <= x:
    kol = bar 

    # looping kolom
    while kol > 0:
            string = string + "*"
            kol = kol - 1
    string = string + "\n"
    bar = bar +1 
    print (string)
    