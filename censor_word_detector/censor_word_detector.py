"""
Welcome guys,
This is the second part of another simple function python project
The idea this time is we'll find logic & way to censor the user input
"""


# Practice Censor Word Detector

### LOGIC ###
# 1. Buat list kata" yang dilarang
# 2. Buat inputan user ke dalam programnya
# 3. Buat function yang mendeteksi inputan dengan list kata" yang dilarang
# 4. Bila terdeteksi kata terlarang di dalam inputan, maka beri sensor untuk masing masing kata, lalu munculkan
# 5. Bila tidak ada kata yang terdeteksi maka inputan akan dimunculkan di program

# 1. Buat list kata" yang dilarang
bad_words = ['bodoh', 'bangsat', 'anjing', 'kontol', 'goblok', 'tai', 'nigga', 'niggas', 'nigger', 'niggers', 'hitler', 'fuck', 'fucking']

# 2. Buat inputan user ke dalam programnya
input_kalimat = input('Chat: ')

# 3. Buat function yang mendeteksi inputan dengan list kata" yang dilarang
# variable 'teks' itu bebas dalam artian ketika memanggil function ini dengan variable lainnya maka variable baru tersebut sama dengan variable teks (semoga mengerti, bisa ditanyakan lagi kalau masih bingung urutannya ya)
def censor_bad_word(teks):
    # Pertama, konversi dulu kata yang masuk menjadi kecil
    # Karena, bila tiap kata memiliki huruf besar atau kecil (case sensitive) akan lebih rumit mendeteksinya
    teks = teks.lower()
    
    # 4. Bila terdeteksi kata terlarang di dalam inputan, maka beri keterangan 'Banned'
    # variable 'kata' disini adalah variable baru yang mewakilkan tiap value dari list bad_words oke?
    # jadi loop satu per satu untuk tiap tiap kata di bad_words dimana...
    for kata in bad_words:
        # Mengecek apakah kata (dari daftar bad_words) terdapat di dalam teks (yang sudah diinputkan oleh user).
        if kata in teks:
            # Disini logicnya, variable teks sama dengan... =
            # variable teks.yang direplace: yaitu variable kata, diubah menjadi string '*'
            # Yang dikalikan (* atau x) dengan jumlah len(kata) yang mana...
            # len(kata) --> memberikan informasi berapa jumlah huruf yang ada di dalam variable kata (misal len dari kata saat ini adalah goblok = ****** yaitu 6 buah)
            teks = teks.replace(kata, '*' * len(kata))
    
    # 5. Bila tidak ada kata yang terdeteksi maka inputan akan dimunculkan di program
    print(teks)

# Call the bad word detector fucntion
censor_bad_word(input_kalimat)