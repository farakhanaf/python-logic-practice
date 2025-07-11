# Contoh teks yang akan ditest menggunaakn function find()
teks = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets 
containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum. Python"""

# Untuk menghasilkan "Index Keberapa"
print(teks.find("Python"))  # 581
print(teks.find("Java"))    # -1

# Untuk menghasilkan "True or False"
print("Python" in teks)  # True
print("Java" in teks)    # False

# Test apakah user input mendeteksi kata yang ada di dalam variable teks
# print(teks.find(find_something))  # 581



### LOGIC ###
# Kalau variable find_something tidak menemukan apapun (-1)
# maka akan menampilkan keterangan "Not Found"

def show_result(text):
    is_found = teks.find(find_something)
    if is_found == -1:
        print("Not Found :(")
    elif is_found != -1:
        print("Teks",find_something,"ada di urutan:",is_found)
            

# User input untuk mencari sebuah kata dimasukan ke dalam variable find_something
find_something = input("Search... ")
# Function show_result langsung dipanggil setelah user input
show_result(find_something)
