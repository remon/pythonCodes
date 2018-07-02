#added by @Azharoo 
#Python 3

def revirse_string(word):
    s=""
    word= word.split()
    for e in word:
        s+= e[::-1] + " "
    print s


word="Welcome to pythonCodes on GitHub"

revirse_string(word)
