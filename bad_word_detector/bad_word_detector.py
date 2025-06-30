"""
First of all welcome guys,
Look, these codes just some basic ahh logic practice of mine
Nothing too serious (I don't think anyone will be here to read it anyway)
But anyway, my point is in case I need to go back to check some old codes
And practicing my sharpness and senses in 'programming world'
I do have skill issues since long time ago, but my bosses told me to not giving up, so here I am now
"""


# Practice Bad Word Detector

# Dictonary/List of Bad Words
bad_words = ['bodoh', 'bangsat', 'anjing', 'kontol', 'goblok', 'tai', 'nigga']

# User will input words here
input_kalimat = input('Chat: ')

# Function to detect the bad word inside the input text
def detect_bad_word(teks):
    #pass
    
    # Logic to detect the bad word
    for kata in bad_words:
        # Dilakukan pengecekan untuk setiap 
        if kata.lower() == teks.lower():
            print('Maaf, anda di banned')
        else:
            print(input_kalimat)

# Call the bad word detector fucntion
detect_bad_word(input_kalimat)