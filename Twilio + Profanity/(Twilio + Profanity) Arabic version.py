#أضيفت من قبل @Modydj
#Python 2.7
#2 in 1 (Twilio + Profanity Editor)




#آلية العمل:


#1- سأقوم بإنشاء دالة def تحت اسم see_me_that_in_phone

#2- سأجعله يعود للدالتين functions (check_profainty, read_text)

#3- سأستقبل على جوالي فقط النتيجة ان كانت الرسالة تحوي على كلمات غير مرغوب بها أم لا


#حسناً ، فلنبدأ ;)


#استيراد المكتبات المناسبة في البداية




import urllib
from twilio.rest import Client

# كتابة دالتين def لتحقق من عملنا،
# الأولى تدعى بـ read_text, والتي سوف تقرأ الملف المراد قراءته وفحصه.

def read_text():
    quotes = open(r'C:\Users\2\Desktop\movie_quotes.txt','r')# قم بتغير هذا الكود بحسب مسار الملف المراد فحصه
    contents_of_file = quotes.read()
    #print (contents_of_file)
    quotes.close()
    check_profainty(contents_of_file)

# الثانية check profanity , والتي سوف تأخذ زمام الأمور لتنفيذ الأمر
# الناتج عن قراءة الدالة الأولى read_text def.


def check_profainty(text_to_check):
    account_sid = "ACdXXXXXXXXXXXXXXXX" #ادخل هذا الرقم من twilio
    auth_token = "3bXXXXXXXXXXXXXXXXX" #ادخل هذا الرقم من twilio
    client = Client(account_sid, auth_token)
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output= connection.read()
    #print (output)
    connection.close()

    if "true" in output:
        message = client.messages.create(
            body="profainty Alert!",
            to="+213xxxxxxxx", # ضع رقم هاتفك
            from_="+143xxxxxxx") # ضع رقمك في موقع twilio
        print(message.sid)

    elif "false" in output:
        message = client.messages.create(
            body="This document has no curse words!",
            to="+213xxxxxxxx", # ضع رقم هاتفك
            from_="+143xxxxxxx") # ضع رقمك في موقع twilio
        print(message.sid)

    else:
        message = client.messages.create(
            body="Could not scan the document properly.",
            to="+213xxxxxxxx", # ضع رقم هاتفك
            from_="+143xxxxxxx") # ضع رقمك في موقع twilio
        print(message.sid)

# الخطوة الأخيرة, ولكن في الواقع , هذه الخطوة الأولى, عندما تقوم بتشغيل البرنامج,
# هذه الدالة سوف تبدأ بالعمل على استدعاء دالة read_text .


def see_me_that_in_phone():
          x = read_text()


# دعونا نبدأ ;)


see_me_that_in_phone()
