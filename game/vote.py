import random
import json

kandidat = []
sifat = ["Ramah", "Baik Hati", "Bijaksana", "Sombong", "Keras Kepala"]
visi = ["Menjadikan kelas nyaman dan aman.", "Membuat kelas menjadi lebih efektif ketika KBM.", "Membuat kelas menjadi lebih bersahabat.", "Membuat kelas menjadi bebas.", "Membuat peraturan yang dapat mengatur seluruh aktivitas kelas."]
hasil_baik = ["Kelas menjadi nyaman, efektif dan menyenangkan", "Kelas menjadi seru dan kompak", "Kelas menjadi tidak membosankan"]
hasil_buruk = ["Kelas menjadi ribut dan tidak kompak", "Kelas menjadi membosankan"]

# Data awal kandidat
for nama in ["Nino", "Javas", "Dimas", "Andra", "Gilbert", "Rasya"]:
    kandidat.append({
        "Nama": nama,
        "Visi": random.choice(visi),
        "Suara": random.randint(1, 10)
    })

with open("data.json", "w") as file:
    json.dump(kandidat, file, indent=4)

seri = False
while not seri:
    print("\nKandidat Calon Ketua Kelas:")
    for k in kandidat:
        print(f"- {k['Nama']} (Visi: {k['Visi']}, Suara: {k['Suara']})")

    vote = input("Masukkan pilihan Anda : ").capitalize()

    with open("data.json", "r") as file:
        data = json.load(file)

    for info in data:
        if vote == info["Nama"]:
            info["Suara"] += 1
            print(f"{info['Nama']} memiliki jumlah suara sebesar {info['Suara']}")

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    suara = [i["Suara"] for i in data]
    suara_terbanyak = max(suara)
    total_pemenang = [i for i in data if i["Suara"] == suara_terbanyak]

    if len(total_pemenang) > 1:
        print("\n=== VOTING SERI ===")
        print("Kandidat dengan suara sama:")
        for p in total_pemenang:
            print(f"- {p['Nama']} ({p['Suara']} suara)")
        with open("dataseri.json", "w") as file:
            json.dump(total_pemenang, file, indent=4)
        seri = True
        break
    else:
        info = total_pemenang[0]
        print(f"\n{info['Nama']} menang dengan {info['Suara']} suara!")
        if info["Visi"] in ["Menjadikan kelas nyaman dan aman.", "Membuat kelas menjadi lebih efektif ketika KBM.", "Membuat kelas menjadi lebih bersahabat."]:
            hasil_akhir = random.choice(hasil_baik)
        else:
            hasil_akhir = random.choice(hasil_buruk)
        print(f"Berdasarkan voting, {hasil_akhir} setelah {info['Nama']} menjadi ketua kelas.")
        break

if seri:
    print("\n=== VOTING ULANG DIMULAI ===")
    with open("dataseri.json", "r") as file:
        kandidat_seri = json.load(file)
    print("Kandidat Seri:", [k["Nama"] for k in kandidat_seri])
