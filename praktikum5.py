exp = '''Selamat datang silahkan pilih menu untuk menetukan program mana yang akan dijalan kan
1. untuk menghitung koinversi suhu
2. untuk menghitung berat badan ideal
3. untuk mencari luas bangun datar
'''

pilihan = input (exp)

match pilihan:
    case "1":
        print ("anda memilih konversi suhu")
        konvert = float(input("masukan suhu dalam farenheit = "))
        celcius = (konvert-32)*5/9
        print("nilai dalam celcius :", celcius,"C")
    case "2":
        print ("anda memilih menghitung index BMI")
        tinggiBadan = float(input("masukan tinggi badan:"))
        beratBadan = float(input("masukan berat badan:"))

        bmi = tinggiBadan/beratBadan
        print("BMI anda adalah", bmi)

        if bmi <= 18.5:
            print("terlalu kurus")
        elif 18.5 <= bmi <= 24.9:
            print("berat badan ideal")
        elif 25 < bmi <= 29.29:
            print("anda obesitas")
        else:
            print("anda obesitas")
    case "3":
        tinggi = float(input("masukan tinggi tabung :"))
        jari = float(input("masukan jari-jari : "))
        rumus = 2*3.14*(jari+tinggi)
        print(rumus)
    case _:
        print("pilihan tidak tersedia")