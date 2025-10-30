import random
import json

data1 = {}
kandidat = []
suara = []
total_pemenang = 0
sifat = ["Ramah", "Baik Hati", "Bijaksana", "Sombong", "Keras Kepala"]
hasil_baik = ["Kelas menjadi nyaman, efektif dan menyenangkan", "Kelas menjadi seru dan kompak", "Kelas menjadi tidak membosankan"]
hasil_buruk = ["Kelas menjadi ribut dan tidak kompak", "Kelas menjadi membosankan"]

nama = "Nino"
data1 = {
    "Nama": nama,
    "Sifat": random.choice(sifat),
    "Suara": random.randint(1,10)
}
kandidat.append(data1)
nama = "Javas"
data1 = {
    "Nama": nama,
    "Sifat": random.choice(sifat),
    "Suara": random.randint(1,10)
}
kandidat.append(data1)
nama = "Dimas"
data1 = {
    "Nama": nama,
    "Sifat": random.choice(sifat),
    "Suara": random.randint(1,10)
}
kandidat.append(data1)
nama = "Andra"
data1 = {
    "Nama": nama,
    "Sifat": random.choice(sifat),
    "Suara": random.randint(1,10)
}
kandidat.append(data1)
nama = "Gilbert"
data1 = {
    "Nama": nama,
    "Sifat": random.choice(sifat),
    "Suara": random.randint(1,10)
}
kandidat.append(data1)
nama = "Rasya"
data1 = {
    "Nama": nama,
    "Sifat": random.choice(sifat),
    "Suara": random.randint(1,10)
}
kandidat.append(data1)

with open ("data.json", "w")as file:
    json.dump(kandidat, file, indent=4)

while True:
    vote = str(input("Masukkan pilihan Anda anda : ")).capitalize()

    with open ("data.json", 'r')as file:
        data = json.load(file)
    
    for info in data:
        if vote == info["Nama"]:
            info["Suara"] += 1
            with open ("data.json", "w")as file:
                json.dump(data, file, indent=4)
            print(f"{info["Nama"]} memiliki jumlah suara sebesar {info["Suara"]}")
        suara.append(info["Suara"])

    suara_terbanyak = max(suara)
    print(f"Suara terbanyak yaitu : {suara_terbanyak}")

    for info in data:
        if info["Suara"] == suara_terbanyak:
            nama = info["Nama"]
            total_pemenang += 1
            print (info["Suara"], info["Nama"])
            print(f"{info["Nama"]} menang dengan mendapatkan sebanyak {info["Suara"]} suara")
            if info["Sifat"] in ["Ramah", "Baik Hati", "Bijaksana"]:
                hasil_akhir = random.choice(hasil_baik)
                print (f"Bedasarkan voting yang diperoleh, {hasil_akhir} setelah {nama} menjadi ketua kelas.")
            elif info["Sifat"] in ["Sombong", "Keras Kepala"]:
                hasil_akhir = random.choice(hasil_buruk)
                print (f"Bedasarkan voting yang diperoleh, {hasil_akhir} setelah {nama} menjadi ketua kelas.")
        pemenang = info['Nama']

        if total_pemenang > 1:
            nama = info["Nama"]
            print ("Akan ada voting lanjutan karena terdapat beberapa kandidat yang memiliki jumlah voting sama1")

            data1 = {
                "Nama": nama,
                "Sifat": info['Sifat'],
                "Suara": info['Suara']
            }
            kandidat.append(data1)
            
            print(total_pemenang)