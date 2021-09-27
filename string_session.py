from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""Welcome To MAFIA USERBOT String Session Generator By @H1M4N5HU0P""")
print("""Special Thanks To My Buddy Respective HellBot Owner @Kraken_The_BadASS""")
print("""Enter Your Valid Details To Continue! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!! "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @MAFIA_USERBOT For Any Help!"
   )

   print(
       "Thanks for Choosing Mafia Userbot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
   )
 except:
  print("")
  print(
      "Wrong phone number \n make sure its with correct country code. Example : +918925534834! Kindly Retry"
  )
  print("")
  continue
 break
