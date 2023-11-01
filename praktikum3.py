# print("Nilai Konversi Suhu")

celcius = float(input("masukan nilai celcius :"))
farenheit = (9/5)*celcius + 32
print("nilai dalam fahrenheit :", farenheit,"F")

# # buat lah konversi susuh dari farenheit ke celcius

farenheit = float(input("masukan nilai farenheit :"))
celcius = (farenheit-32)*5/9
celcius = (5/9)*(farenheit-32)
print("nilai dalam celcius :", celcius,"C")

# a = "ridho"
# b = "0110116047"
# c = "SI 2016"
# d = "depok"

# print(a,b,c,d)

tinggiBadan = float(input("masukan tinggi badan:"))
beratBadan = float(input("masukan berat badan:"))

Bmi = tinggiBadan / beratBadan
print("BMI anda adalah:", Bmi)

if Bmi <= 18.5 :
    print("terlalu kurus")
elif 18.5 < Bmi <= 24.9 :
    print("berat badan normal")
elif 25 < Bmi <= 29.29 :
    print("anda obesitas")
else:
    print("anda obesitas")

# rumus luas tabung 

tinggi=float(input("masukan tinggi :"))
jari=float(input("masukan jari-jari"))
rumus = 2*3.14*jari*(jari+tinggi)

print(rumus)