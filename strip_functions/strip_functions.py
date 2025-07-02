# Variabel bermana 'teks' dengan isi "   halo dunia   " (terdapat spasi yang berlebihan di ujung kanan & kiri)
teks = "   halo dunia   "

# Menggunakan function strip() pada variabel teks
print(teks.strip()+'.')   # "halo dunia"

# Menggunakan function lstrip() pada variabel teks untuk menghapus spasi berlebih di bagian kiri
print(teks.lstrip()+'.')  # "halo dunia   "

# Menggunakan function rstrip() pada variabel teks untuk menghapus spasi berlebih di bagian kanan
print(teks.rstrip()+'.')  # "   halo dunia"
