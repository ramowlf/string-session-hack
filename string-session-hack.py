from termcolor import colored
from pyrogram import Client 
import sys
print(colored("Ne yapmak istiyorsun? \n\n[1] Session giriş kodunu alın\n\n[2] Sessiondan bilgileri alın\n", "green"))
islem = input("Seçimini gir:")
if islem == "1":
  sesstring = input(colored("Sessionu giriniz:", "blue"))
  user = Client("ağzına_veririm", api_id=94575, api_hash="a3406de8d171bb422bb6ddf3bbd800e2", session_string=sesstring)
  user.start();
  try:
    for msg in user.get_chat_history(777000, limit=1):
      print(colored(msg.text, "green"))
  except Exception as e:
    print(colored(e, "red"))
  
elif islem == "2":

  sesstring = input(colored("Sessionu giriniz:", "blue"))
  try:
      user = Client("anan_nasıl_moruk", api_id=94575, api_hash="a3406de8d171bb422bb6ddf3bbd800e2", session_string=sesstring)
      user.start();
      me = user.get_me()
      print(colored(f"Telefon numarası: {me.phone_number}\n", "green"))
      print(colored(f"Kullanıcı adı: {me.username}\n", "green"))
      print(colored(f"İsmi: {me.first_name}", "green"))
      user.stop();
  except Exception as e:
      print(colored(f"Bir hata nedeniyle işlem tamamlanamadı: {e}", "red"))
else:
    print(colored("Geçersiz seçim!", "blue"))
    sys.exit();