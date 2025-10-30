import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='kepuasan_pengguna')

cursor = db.cursor()

def insert_item():
    nama = input("Masukkan Nama Anda : ").capitalize()
    rating = int(input("Masukkan kepuasan anda terhadap produk-produk kami? (Bilangan bulat 1-5) : "))
    if rating > 5:
        print("Berikan rating yang sesuai")
    kritik_saran = str(input("Masukkan kritik/saran dari anda untuk kelompok kami (wajib) : "))
    cursor.execute("INSERT INTO rating_pengguna (nama, rating, kritik_saran) VALUES (%s, %s, %s)", (nama, rating, kritik_saran))
    db.commit()
    if cursor.rowcount > 0:
        print("Data berhasil ditambahkan")
        print("Terimakasih atas masukkannya")
    else:
        print("Data belum berhasil ditambahkan")

def fetch_items():
    cursor.execute("SELECT * FROM `rating_pengguna`")
    items = cursor.fetchall()
    print (items)
    return items

def statistic(items):
    listrating = []
    i = 0
    dictrating = {}

    for index in items:
        i += 1
        rating = index[2]
        nama = index[1]
        listrating.append(rating)
        dictrating[nama] = rating
    print (dictrating)

    rating_total = sum(listrating)
    print (rating_total)

    average = rating_total/i
    print ("Rata-rata", average)
    if ZeroDivisionError:
        print ("Belum ada data")

    highest_rating = max(listrating)
    print ("Rating tertinggi ", highest_rating)

    lowest_rating = min(listrating)
    print ("Rating Terendah", lowest_rating)