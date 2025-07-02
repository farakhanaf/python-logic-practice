"""
First of all welcome guys,
Look, these codes just some basic ahh logic practice of mine
Nothing too serious (I don't think anyone will be here to read it anyway)
But anyway, my point is in case I need to go back to check some old codes
And practicing my sharpness and senses in 'programming world'
I do have skill issues since long time ago, but my bosses told me to not giving up, so here I am now
"""


# Practice Bad Word Detector

### LOGIC ###
# 1. Buat list kata" yang dilarang
# 2. Buat inputan user ke dalam programnya
# 3. Buat function yang mendeteksi inputan dengan list kata" yang dilarang
# 4. Bila terdeteksi kata terlarang di dalam inputan, maka beri keterangan 'Banned'
# 5. Bila tidak ada kata yang terdeteksi maka inputan akan dimunculkan di program

# 1. Buat list kata" yang dilarang
bad_words = ['bodoh', 'bangsat', 'anjing', 'kontol', 'goblok', 'tai', 'nigga', 'niggas', 'nigger', 'niggers', 'hitler', 'fuck', 'fucking']

# 2. Buat inputan user ke dalam programnya
input_kalimat = input('Chat: ')

# 3. Buat function yang mendeteksi inputan dengan list kata" yang dilarang
# variable 'teks' itu bebas dalam artian ketika memanggil function ini dengan variable lainnya maka variable baru tersebut sama dengan variable teks (semoga mengerti, bisa ditanyakan lagi kalau masih bingung urutannya ya)
def detect_bad_word(teks):
    # Pertama, konversi dulu kata yang masuk menjadi kecil
    # Karena, bila tiap kata memiliki huruf besar atau kecil akan lebih rumit mendeteksinya
    teks = teks.lower()
    
    # 4. Bila terdeteksi kata terlarang di dalam inputan, maka beri keterangan 'Banned'
    # variable 'kata' disini adalah variable baru yang mewakilkan tiap value dari list bad_words oke?
    # jadi loop satu per satu untuk tiap tiap kata di bad_words dimana...
    for kata in bad_words:
        # Jika ada kata yang cocok dengan variable "teks/input_kalimat" maka...
        if kata in teks:
            # Munculkan teks berikut...
            print('Mohon untuk menghindari kata" yang dilarang')
            return
    
    # 5. Bila tidak ada kata yang terdeteksi maka inputan akan dimunculkan di program
    print(input_kalimat)

# Call the bad word detector fucntion
detect_bad_word(input_kalimat)