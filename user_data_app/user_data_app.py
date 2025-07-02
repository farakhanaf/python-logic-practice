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
    writer = csv.writer(file)
    
    while True:
        name = input("Enter your name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        
        email = input("Enter your email: ")
        
        if email_validation(email):
            writer.writerow([name, email])
            print("✅ Data saved.")
        else:
            print("❌ Invalid email. Data not saved.")