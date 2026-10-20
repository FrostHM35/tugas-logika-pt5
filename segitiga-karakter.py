# TUGAS KE 1
# NAMA ANGGOTA KELOMPOK 1
# 1. Syira Azahra
# 2. Habbel Wildan Haqiqy
# 3. Agra
# 4. Nisha

garis = 50

print("-" * garis)
print("TUGAS KE 1 - POLA SEGITIGA".center(garis))
print("-" * garis)

# Meminta masukan (input) dari pengguna
segitiga = int(input("Masukkan jumlah baris : "))
karakter = input("Masukkan karakter (contoh: *, $, #): ")

print("-" * garis)
print("Keluaran Pola Segitiga:")

# MENGGUNAKAN NESTED LOOP

# Loop Luar i : Mengatur jumlah baris dari 1 sampai segitiga
for i in range(1, segitiga + 1):
    
    # Loop Dalam 1 j : Mencetak spasi di sebelah kiri agar segitiga menjadi simetris/tengah
    for j in range(segitiga - i):
        print(" ", end="")
        
    # Loop Dalam 2 k : Mencetak karakter dan spasi sebanyak baris saat ini (i)
    for k in range(i):
        print(karakter, end=" ")
        
    # Perintah untuk pindah ke baris baru di bawahnya
    print()

print("-" * garis)