from flask import Flask, render_template, request, redirect, url_for, session
import json
import subprocess
import os
import random

app = Flask(__name__)
app.secret_key = "vote_aman"

# 🔹 Halaman utama
@app.route('/')
def home():
    session.clear()
    return render_template("home.html")

# 🔹 Halaman daftar kandidat
@app.route('/index')
def index():
    if not os.path.exists("data.json"):
        subprocess.run(["python", "vote.py"])

    with open("data.json", "r") as file:
        data = json.load(file)

    if isinstance(data, dict):
        data = [data]

    jumlah_vote = session.get("jumlah_vote", 0)
    return render_template("index.html", kandidat=data, jumlah_vote=jumlah_vote)

# 🔹 Proses voting
@app.route('/vote', methods=['POST'])
def vote():
    pilihan = request.form.get("pilihan")
    jumlah_vote = session.get("jumlah_vote", 0)

    # Batasi maksimal 3 kali voting
    if jumlah_vote >= 3:
        return render_template("limit.html", jumlah_vote=jumlah_vote)

    with open("data.json", "r") as file:
        data = json.load(file)

    if isinstance(data, dict):
        data = [data]

    # Tambah suara untuk kandidat yang dipilih
    for info in data:
        if pilihan == info["Nama"]:
            info["Suara"] += 1

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    session["jumlah_vote"] = jumlah_vote + 1

    # Cek hasil voting
    suara_terbanyak = max([k["Suara"] for k in data])
    pemenang_list = [k for k in data if k["Suara"] == suara_terbanyak]

    # 🔸 Jika ada seri
    if len(pemenang_list) > 1:
        with open("dataseri.json", "w") as seri_file:
            json.dump(pemenang_list, seri_file, indent=4)
        return render_template("seri.html", kandidat=pemenang_list)

    # 🔸 Jika sudah ada pemenang tunggal
    pemenang = pemenang_list[0]

    hasil_baik = [
        "Kelas menjadi nyaman, efektif dan menyenangkan", "Kelas menjadi seru dan kompak", "Kelas menjadi tidak membosankan"
    ]
    hasil_buruk = [
        "Kelas menjadi ribut dan tidak kompak",
        "Kelas menjadi membosankan"
    ]

    hasil_akhir = random.choice(
        hasil_baik if pemenang["Visi"] in ["Menjadikan kelas nyaman dan aman.", "Membuat kelas menjadi lebih efektif ketika KBM.", "Membuat kelas menjadi lebih bersahabat."] else hasil_buruk
    )

    # Simpan hasil ke session
    session["pemenang"] = pemenang
    session["pilihan"] = pilihan
    session["hasil_akhir"] = hasil_akhir

    return render_template("congrats.html", pilihan=pilihan, pemenang=pemenang)

# 🔹 Halaman hasil voting akhir
@app.route("/result")
def result():
    pemenang = session.get("pemenang")
    hasil_akhir = session.get("hasil_akhir")

    if not pemenang:
        return redirect(url_for("index"))

    return render_template("result.html", pemenang=pemenang, hasil_akhir=hasil_akhir)

# 🔹 Voting ulang jika seri
@app.route("/revote", methods=["POST"])
def revote():
    pilihan = request.form.get("pilihan")

    with open("dataseri.json", "r") as file:
        data_seri = json.load(file)

    for info in data_seri:
        if pilihan == info["Nama"]:
            info["Suara"] += 1

    with open("dataseri.json", "w") as file:
        json.dump(data_seri, file, indent=4)

    suara_terbanyak = max([k["Suara"] for k in data_seri])
    pemenang_list = [k for k in data_seri if k["Suara"] == suara_terbanyak]

    if len(pemenang_list) > 1:
        return render_template("seri.html", kandidat=pemenang_list)  # Seri lagi

    # Jika sudah ada pemenang
    pemenang = pemenang_list[0]
    session["pemenang"] = pemenang

    return render_template("result.html", pemenang=pemenang)

# Halaman tambahan jika pilihan user menang
@app.route("/win")
def win():
    pilihan = session.get("pilihan")
    print(pilihan)
    hasil_akhir = session.get("hasil_akhir")
    return render_template("win.html", pilihan=pilihan, hasil_akhir=hasil_akhir)

# 🔹 Reset session
@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
