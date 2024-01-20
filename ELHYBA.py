from mody import Mody
import requests
import telebot
import time, base64, marshal, zlib, py_compile
import os , sys
token = Mody.QQZ_T
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start(message):
 
 bot.send_message(message.chat.id,f"""<strong>❀~ مرحبا انا بوت تشفير الملفات 🧑🏻‍💻 .
♆〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰♆

❀~ نوع تشفير : marshal, base64, zlib 🔒 .
❀~ الفئه : null 🌪️ .
❀~ عدد طبقات : 6 🚸 .

♆〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰♆</strong>""",parse_mode="html")
 @bot.message_handler(content_types=['document'])
 def send(message):
 	 bot.get_file(message.document.file_id)
 	 #bot.download_file(file_info.file_path)
 	# bot.send_photo(message.chat.id,open("file","rb"))
 	 file_info = bot.get_file(message.document.file_id)
 	 use = bot.download_file(file_info.file_path)
 	 bot.send_message(message.chat.id, f"""<strong>انتظر…</strong>""",parse_mode="html")
 	 cv =str("#@haetmane5")
 	 sa = compile(use, 'dg', 'exec')
 	 sb = marshal.dumps(sa)
 	 sc = zlib.compress(sb)
 	 sd = base64.b85encode(sc)
 	 b = '#https://t.me/haetmane5\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
 	 d = open('[@QQZ_T].py', 'w')
 	 d.write(b+'\n'+cv)
 	 d.close()
 	 file = {'document':open('[@QQZ_T].py','rb')}
 	 tex = ("❀~ تم التشفير بواسطة : @haetmane5\n❀~ شكرا لاستخدامك بوت التشفير الخاص بنا 🚸\n❀~ كل ما يهمنا هو سعادتكم و امانكم 🔱\n❀~ للتواصل مع المطور @QQZ_T")
 	 requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={message.chat.id}&caption={tex}', files=file)
 	 bot.send_message(message.chat.id, f"[🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱](t.me/haetmane5)",parse_mode="markdown",disable_web_page_preview="true")
 	 os.system(f'rm -rf [@QQZ_T].py')

print ("تم التشغيل بنجاح بواسطة @QQZ_T")
  	
bot.polling(True)

