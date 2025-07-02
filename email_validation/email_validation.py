# Email validation menggunakan function endswith() (Ada juga function startswith())

# Buat function untuk validasi apakah variable user_email mengandung string yang valid untuk sebuah email (Gmail))
def email_validation(teks):
    if teks.endswith("@gmail.com"):
        print(user_email,"is valid a email address")
        return True
    else:
        print(user_email,"is invalid email address")
        return False


# User menginput email mereka
user_email = str(input("Enter your email: "))

# Panggil fungsi dan simpan hasilnya di variable is_valid
is_valid = email_validation(user_email)

# Panggil langsung fungsi email_validation setelah user input
# email_validation(user_email)

# Test apakah hasilnya True
# print(user_email.endswith("@gmail.com"))