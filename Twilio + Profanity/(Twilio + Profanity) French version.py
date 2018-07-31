#ajouté par @Modydj
#Python 2.7
# 2 en 1 ( Twilio + Profanity Éditeur)



# Mécanisme d'action:

#1. Je vais créer def appel: see_me_that_in_phone

#2 - Je vais revenir aux fonctions: (check_profainty, read_text)

# 3 - Enfin, je recevrai sur mon portable  le résultat si le message contient les mots indésirables ou non


#Bien, On y va ;)


#importer les bibliothèques appropriées dans le premier

import urllib
from twilio.rest import Client

# Ecrire deux def pour vérifier de notre travail,
# Le premier est read_text, qui lira votre fichier cible.


def read_text():
    quotes = open(r'C:\Users\Desktop\movie_quotes.txt','r')# Changeons cette adresse en fonction de votre destination
    contents_of_file = quotes.read()
    #print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


# Le second est de vérifier check_profanity, qui prendra l'ordre après avoir connu
# le résultat en utilisant read_text def.


def check_profanity(text_to_check):
    account_sid = "ACdXXXXXXXXXXXXXXXX" # Entrez votre twilio account_sid
    auth_token = "3bXXXXXXXXXXXXXXXXX" # Entrez votre twilio account_token
    client = Client(account_sid, auth_token)
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output= connection.read()
    #print (output)
    connection.close()

    if "true" in output:
        message = client.messages.create(
            body="profainty Alert!",
            to="+213xxxxxxxx", # mettez votre numéro de téléphone
            from_="+143xxxxxxx")# mettez votre numéro de téléphone sur Twilio
        print(message.sid)

    elif "false" in output:
        message = client.messages.create(
            body="This document has no curse words!",
            to="+213xxxxxxxx",# mettez votre numéro de téléphone
            from_="+143xxxxxxx")# mettez votre numéro de téléphone sur Twilio
        print(message.sid)

    else:
        message = client.messages.create(
            body="Could not scan the document properly.",
            to="+213xxxxxxxx",# mettez votre numéro de téléphone
            from_="+143xxxxxxx")# mettez votre numéro de téléphone sur Twilio
        print(message.sid)

# La dernière étape, mais en fait, c'est la première étape, lorsque vous exécutez ce programme,
# Cette def commencera dans le begging pour invoquer read_text def.

def see_me_that_in_phone():
          x = read_text()


#Et c'est parti ;)

see_me_that_in_phone()