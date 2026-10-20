# TUGAS KE 2
# NAMA ANGGOTA KELOMPOK 1
nama_anggota = ["Syira Azahra", "Habbel Wildan Haqiqy", "Agra", "Nisha"]

# untuk batas garis
garis = 50

ayam = int(input("Masukkan jumlah anak ayam : "))

print("-" * garis)
print("Nama Anggota Kelompok 1".center(garis))

# Menggunakan f-string (huruf 'f' di depan) agar variabel {i + 1} dan {nama_anggota[i]} bisa terbaca
for i in range(len(nama_anggota)):
    print(f"{i + 1}. {nama_anggota[i]}")

print("-" * garis)

# Cetak baris pertama di luar perulangan
print("TUGAS KE 2".center(garis))
print("tek kotek kotek kotek, anak ayam turun berkotek")


for i in range(ayam, 0, -1):
    # Cek jika angka sekarang adalah 1, maka sisa/tinggal "induknya"
    if i == 1:
        print("anak ayam turunlah", i ,"mati satu tinggallah induknya")
    else:
        # Jika lebih dari 1, kurangi 1 untuk sisa penurunannya
        print("anak ayam turunlah", i ,"mati satu tinggallah", i - 1)

print("-" * garis)