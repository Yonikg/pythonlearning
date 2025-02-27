
st = 'Print only the words that start with s in this statement'
for f in st .split():
    if f [0]=='s':
        print(f)





strn = 'Print only the words that start with s in this statement'
words_starting_with_s = [word for word in strn.split() if word.lower().startswith('s')]

print(words_starting_with_s)  # Output the words that start with 's'
