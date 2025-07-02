'''
KETERANGAN SMALL PROJECT: USER_DATA_APP

IDE:
- Form validasi lengkap (pakai regex)
- Aplikasi input data banyak user
- Simpan ke file .csv

PERPADUAN:
- Validasi email
- Input banyak user
- Simpan data ke file .csv

TUJUAN:
User bisa input:
- Nama
- Email

Aplikasi akan:
- Validasi email
- Simpan data ke file CSV jika valid
'''


# Pertama" import csv karena hasil dari inputan akan disimpan ke file csv tersebut
import csv

# Buat function sederhana untuk validasi email
def email_validation(email):
    if email.endswith("@gmail.com"):
        print(email,"is valid a email address")
        return True
    else:
        print(email,"is invalid email address")
        return False
    
# Buka (atau buat) file CSV untuk menyimpan data

''' Penjelasan "with open("user_data_app/user_data.csv", "a", newline="") as file:"
1. open(...): Membuka (atau membuat) file bernama user_data.csv
2. "a": Mode append → artinya menambahkan baris ke akhir file, bukan menimpa isinya
3. newline="": Mencegah baris kosong tambahan di Windows saat menulis ke CSV
4. as file: File yang dibuka disimpan ke variabel file
5. with ...:: Menggunakan context manager → otomatis menutup file setelah selesai
'''
with open("user_data_app/user_data.csv", "a", newline="") as file:
    ''' Penjelasan "writer = csv.writer(file)"
    1. csv.writer(...): Membuat objek writer dari modul csv
    2. Objek ini digunakan untuk menulis data ke file CSV dengan format yang benar (misalnya setiap nilai jadi kolom)
    '''
    writer = csv.writer(file)
    
    # Dengan menggunakan loop While, selama masih True maka...:
    while True:
        # Buat variable 'name' yang akan menyimpan inputan dari user
        name = input("Enter your name (or type 'exit' to quit): ")
        # Tapi, Jika inputan di dalam variable 'nama' itu berisi inputan sama dengan 'exit'
        # Dengan function lower() maka teks yang diinput dikonversi menjadi huruf kecil semua
        if name.lower() == 'exit':
            # Program akan berhenti
            break
        
        # Buat variable dengan nama 'email' yang akan menampung email user lewat inputan
        email = input("Enter your email: ")
        
        # Validasi...
        if email_validation(email):
            writer.writerow([name, email])
            print("✅ Data saved.")
        else:
            print("❌ Invalid email. Data not saved.")