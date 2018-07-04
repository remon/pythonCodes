#added by @Modydj
#Python 2.7
#2 in 1 (Twilio + Profanity Editor)



#Mechanism of Action:

#1. I will create def call: see_me_that_in_phone

#2 - I will make it back to the functions (check_profainty, read_text)

#3 - Finally, I will receive on my mobile only the result if the message contains the words undesirable or not


#Well, Let's start:


#import the appropriate libraries in the first



import urllib
from twilio.rest import Client

# Write two def to check from our work,
# The first one is read_text, which will read your target file.


def read_text():
    quotes = open(r'C:\Users\Desktop\movie_quotes.txt','r')# Let's change this address according to your destination
    contents_of_file = quotes.read()
    #print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


# The second one is check profanity , which will take the order after knowing
# the result by using read_text def.


def check_profanity(text_to_check):
    account_sid = "ACdXXXXXXXXXXXXXXXX" #Enter your twilio account_sid
    auth_token = "3bXXXXXXXXXXXXXXXXX" # Enter your twilio account_token
    client = Client(account_sid, auth_token)
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output= connection.read()
    #print (output)
    connection.close()

    if "true" in output:
        message = client.messages.create(
            body="profainty Alert!",
            to="+213xxxxxxxx", # put your number phone
            from_="+143xxxxxxx")# put your number phone on Twilio
        print(message.sid)

    elif "false" in output:
        message = client.messages.create(
            body="This document has no curse words!",
            to="+213xxxxxxxx",# put your number phone
            from_="+143xxxxxxx")# put your number phone on Twilio
        print(message.sid)

    else:
        message = client.messages.create(
            body="Could not scan the document properly.",
            to="+213xxxxxxxx",# put your number phone
            from_="+143xxxxxxx")# put your number phone on Twilio
        print(message.sid)

# The last step, but in fact, this is the first step, when you run this program,
# This def will start in the begging to summon read_text def.

def see_me_that_in_phone():
          x = read_text()


#And here we go ;)

see_me_that_in_phone()