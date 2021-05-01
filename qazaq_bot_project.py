import telebot
import random
import requests
from telebot import types
from bs4 import BeautifulSoup
from requests import get

from qazaq import Jumbaq
from qazaq import Jayaptar
from qazaq import Maqal
from qazaq import MJayaptar
from qazaq import Motivation
from qazaq import QaraSoz

TOKEN = '1459461110:AAHlRubyPy9abOq_E20ojjZnAitg8ZJ2TfE'
bot = telebot.TeleBot(TOKEN)

x = random.randint(0,5)
y = random.randint(0,3)

@bot.message_handler(commands=['start'])
def welcome(message):
    # basatyn knopkalar
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("Qalaysiz?")
    item3 = types.KeyboardButton("Qanatty sözder")

    markup.add(item2, item3)
    bot.send_message(message.chat.id,
                     "Ассалаумагалейкум, {0.first_name}!\nМен - <b>{1.first_name}</b> 🤖, сізге пайдалы болу үшін жасалдым."
                     "Мен сізге мотивация беруге және ақыл ойдың жылдам ойлауына көмек беруге тырысамын.    "
                     " Командалар арқылы сіз өзіңізге қажет бағытты таңдай аласыз.Олар:"
                    "\n/start  (қайта бастау үшін)"
                    "\n/story  шығаршылық бағыт (ертегілер мен қара сөздер)"
                    "\n/quiz  жұмбақ, мақал-мәтел ойындары"
                     "\n/kui  қазақы нақыштағы музыкалық шығарма тындауға мүмкіндік береді".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html',reply_markup=markup)
@bot.message_handler(commands=['quiz'])
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ойын ойнаймыз ба? 😁")
    markup.add(item1)
    bot.send_message(message.chat.id,
                     "Тағы да сәлем, {0.first_name}!\nбұл - <b>{1.first_name}</b>, ойын ойнап ақыл ойдың жүйріктігін дамытатын сәт келді деп ойлаймын 😉".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['story'])
def story(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ертегілер 💫💤")
    item2 = types.KeyboardButton("Абайдың Қара сөздері📌")
    markup.add(item1,item2)
    bot.send_message(message.chat.id,
                     "Сәлем, {0.first_name}!\nМен - <b>{1.first_name}</b>, ертегілермен және қара сөздермен бөлісе аламын."
                     "  Қызықты болса...😁".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
@bot.message_handler(commands=['kui'])
def muz(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Күй: Адай📌")
    item2 = types.KeyboardButton("Күй: Ерке сылқым📌")
    item3 = types.KeyboardButton("Күй: Жұмыр қылыш📌")
    item4 = types.KeyboardButton("Күй: Көңіл толқыны📌")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     "{0.first_name}!\nМен - <b>{1.first_name}</b>, қазақтың қанына біткен күй арқылы шабыттану керек болса мен бармын😁".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
class parsingg:
    @bot.message_handler(commands=['arystan'])
    def parsing(message):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://balalaralemi.kz/article/1731/Arystan-men-tulki#.X9acBdgzaMp/', headers=headers).text
        soup = BeautifulSoup(resp, 'html.parser')
        # find
        title = soup.find('div', class_='content')
        title1 = soup.find('div', class_='title_top')
        bot.send_photo(message.chat.id, get("https://balalaralemi.kz/upd/2015/0827/144067093655dee4d8bf2443.38028297.jpg").content)
        bot.send_message(message.chat.id, title1.get_text())
        bot.send_message(message.chat.id, title.get_text())
    @bot.message_handler(commands=['altynbalta'])
    def parsing(message):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://balalaralemi.kz/article/3149/Altyn-balta#.X9e_StgzaMo/', headers=headers).text
        soup = BeautifulSoup(resp, 'html.parser')
        # find
        title = soup.find('div', class_='content')
        title1 = soup.find('div', class_='title_top')
        bot.send_photo(message.chat.id, get("https://balalaralemi.kz/upd/2016/0516/146338926357398c4f68b2a0.31418572.png").content)
        bot.send_message(message.chat.id, title1.get_text())
        bot.send_message(message.chat.id, title.get_text())
    @bot.message_handler(commands=['ekidos'])
    def parsing(message):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://balalaralemi.kz/article/2079/Eki-dos-pen-ayu#.X9fDRtgzaMo/', headers=headers).text
        soup = BeautifulSoup(resp, 'html.parser')
        # find
        title = soup.find('div', class_='content')
        title1 = soup.find('div', class_='title_top')
        bot.send_photo(message.chat.id, get("https://balalaralemi.kz/upd/2015/0929/1443548759560ace57a10fc4.68300114.gif").content)
        bot.send_message(message.chat.id, title1.get_text())
        bot.send_message(message.chat.id, title.get_text())
    @bot.message_handler(commands=['qoian'])
    def parsing(message):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        resp = requests.get('https://balalaralemi.kz/article/1925/Qorqaq-qoyan#.X9e_yNgzaMo/', headers=headers).text
        soup = BeautifulSoup(resp, 'html.parser')
        # find
        title = soup.find('div', class_='content')
        title1 = soup.find('div', class_='title_top')
        bot.send_photo(message.chat.id, get("https://balalaralemi.kz/upd/2015/0818/143991965955d36e2b154080.92851652.jpg").content)
        bot.send_message(message.chat.id, title1.get_text())
        bot.send_message(message.chat.id, title.get_text())
c = parsingg()

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Ойын ойнаймыз ба? 😁':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Maqal-matelder", callback_data='Maqal')
        item2 = types.InlineKeyboardButton("Jumbaq", callback_data='Jumbaq')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Keremet oinaiyq!', bot.get_me(), parse_mode='html',
                         reply_markup=markup)

    elif message.text == 'Ертегілер 💫💤':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Видео формат")
        item2 = types.KeyboardButton("Жазбаша формат")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Ерте, ерте, ертедее...', bot.get_me(), parse_mode='html',
                         reply_markup=markup)
    elif message.text == 'Абайдың Қара сөздері📌':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('1', callback_data='1')
        item2 = types.InlineKeyboardButton('...45', callback_data='...45')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Абай атамыздың қара сөздері керемет таңдау 👍🏻',bot.get_me(), parse_mode='html', reply_markup=markup)

    elif message.text.lower() == 'жалғасы':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Жалғасын білу", callback_data='Жалғасы')
        item2 = types.InlineKeyboardButton("Жалғасын жазу", callback_data='Maqal jalgasin jazy')

        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         'Ал ендешее...'.format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)

    elif message.text.lower() == 'жауабы':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Жауабын білу", callback_data='Жауап')
        item2 = types.InlineKeyboardButton("Жауабын жазу", callback_data='Жауабын жазу')

        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         'Ал ендешее...'.format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)

    elif message.text == 'Qanatty sözder':
        bot.send_message(message.chat.id, str(random.choice(Motivation)))

    elif message.text.lower() == str(Jayaptar[x]):
        bot.send_message(message.chat.id,'Жарайсын, келесісін тауып көр 😊.  Қайтадан менюден ойын таңдауыңызды сұраймын')
    elif message.text.lower() == str(MJayaptar[y]):
        bot.send_message(message.chat.id,'Жарайсын, келесісін тауып көр 😊.  Қайтадан менюден ойын таңдауыңызды сұраймын')

    elif message.text == 'Qalaysiz?':

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Шүкір, жақсы", callback_data='good')
        item2 = types.InlineKeyboardButton("Онша емес", callback_data='bad')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Бәрі керемет, өзіңіз қалайсыз?', reply_markup=markup)

    elif message.text == 'Видео формат':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Ақ қасқыр", callback_data='қасқыр')
        item2 = types.InlineKeyboardButton("Бақыт пен сәттілік", callback_data='бақыт')
        item3 = types.InlineKeyboardButton("Аю мен маса", callback_data='аю')
        item4 = types.InlineKeyboardButton("Бақыт құсы", callback_data='бақытқұс')
        item5 = types.InlineKeyboardButton("Боран батыр", callback_data='боран')
        item6 = types.InlineKeyboardButton("Алтын алма", callback_data='алтын')
        item7 = types.InlineKeyboardButton("Басқа да ертегі видеоларын көру", callback_data='басқа')

        markup.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, 'Keremet tanday! 👍🏻'
                                          'Төмендегі видеоларды ертегі тақырыбы бойынша таңдасаңыз болады😁',
                         reply_markup=markup)

    elif message.text == 'Жазбаша формат':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Арыстан мен тулкы", callback_data='Арыстан')
        item2 = types.InlineKeyboardButton("Алтын балта", callback_data='Алтынбалта')
        item3 = types.InlineKeyboardButton("Екі дос пен аю", callback_data='Екідос')
        item4 = types.InlineKeyboardButton("Қорқақ қоян", callback_data='қоян')
        item5 = types.InlineKeyboardButton("Басқа да ертегілерді оқу", callback_data='басқаертегі')
        markup.add(item1,item2,item3,item4,item5)
        bot.send_message(message.chat.id, 'Keremet tanday! 👍🏻 '
                                          'Төмендегі ертегілердің біреуін таңдап оқысаңыз болады😁', reply_markup=markup)
    elif message.text == 'Күй: Адай📌':
        bot.send_message(message.chat.id, 'Адай күйін тыңдау үшін сәл күтіңіз, жіберілуде...📌')
        bot.send_audio(message.chat.id,
                       get("https://dl2.mp3party.net/online/7513813.mp3").content)
    elif message.text == 'Күй: Ерке сылқым📌':
        bot.send_message(message.chat.id, 'Ерке сылқым күйін тыңдау үшін сәл күтіңіз, жіберілуде...📌')
        bot.send_audio(message.chat.id,
                       get("https://as2.musicapp.nur.kz/11/94/ae/34/86/fd/94ae3486fd9d29da09769ac80b599c54.mp3?id=94ae3486fd9d29da09769ac80b599c54").content)
    elif message.text == 'Күй: Жұмыр қылыш📌':
        bot.send_message(message.chat.id, 'Жұмыр қылыш күйін тыңдау үшін сәл күтіңіз, жіберілуде...📌')
        bot.send_audio(message.chat.id,
                       get("https://as1.musicapp.nur.kz/2/96/7a/46/84/c3/967a4684c33abc1aad8f5c82d0ae32ce.mp3?id=967a4684c33abc1aad8f5c82d0ae32ce").content)
    elif message.text == 'Күй: Көңіл толқыны📌':
        bot.send_message(message.chat.id, 'Көңіл толқыны күйін тыңдау үшін сәл күтіңіз, жіберілуде...📌')
        bot.send_audio(message.chat.id,
                       get("https://as2.musicapp.nur.kz/12/da/03/ba/cf/15/da03bacf152bc8fdfff507223b41b520.mp3?id=da03bacf152bc8fdfff507223b41b520").content)
    else:
        bot.send_message(message.chat.id, 'хммм... қайта жазып көріңіз 😊')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Өте керемет 😊')
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, 'Ештеңе етпес 😢')
        elif call.data == 'Maqal':
            bot.send_message(call.message.chat.id, str(str(Maqal[y]))+str('.Jayabin kutem :)'))
        elif call.data == 'Жалғасы':
            bot.send_message(call.message.chat.id, str('Жалғасы:'+ (MJayaptar[y])))
        elif call.data == 'Maqal jayabin jazy':
            bot.send_message(call.message.chat.id, 'жалғасын кіші әріппен жазуынызды өтінемін')
        elif call.data == 'Jumbaq':
            bot.send_message(call.message.chat.id, str(str(Jumbaq[x])) + str('.Жауабын кутем :)'))
        elif call.data == 'Жауап':
            bot.send_message(call.message.chat.id, str('Жауабы:' + (Jayaptar[x])))
        elif call.data == 'Жауабын жазу':
            bot.send_message(call.message.chat.id, 'жауабын кіші әріппен жазуынызды өтінемін')

        elif call.data == 'қасқыр':
            bot.send_message(call.message.chat.id, 'Осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://kitap.kz/video/1/aq-qasqyr')
        elif call.data == 'бақыт':
            bot.send_message(call.message.chat.id, 'Осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://kitap.kz/video/1/baqyt-pen-sattilik')
        elif call.data == 'аю':
            bot.send_message(call.message.chat.id, 'Осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https: // kitap.kz / video / 1 / ayu - men - masa')
        elif call.data == 'бақытқұс':
            bot.send_message(call.message.chat.id, 'Осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://kitap.kz/video/1/baqyt-qusy')
        elif call.data == 'боран':
            bot.send_message(call.message.chat.id, 'Осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://kitap.kz/video/1/boran-batyr')
        elif call.data == 'алтын':
            bot.send_message(call.message.chat.id, 'Осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://kitap.kz/video/1/altyn-alma')
        elif call.data == 'басқа':
            bot.send_message(call.message.chat.id, 'Басқа да видеоларды көру үшін осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://kitap.kz/video/1')
        elif call.data == 'Арыс':
            bot.send_message(call.message.chat.id, '/arystan  батырмасын basyinizdi suraimin 😊')
        elif call.data == 'Алтынбалта':
            bot.send_message(call.message.chat.id, '/altynbalta  батырмасын basyinizdi suraimin 😊')
        elif call.data == 'Екідос':
            bot.send_message(call.message.chat.id, '/ekidos  батырмасын basyinizdi suraimin 😊')
        elif call.data == 'қоян':
            bot.send_message(call.message.chat.id, '/qoian  батырмасын basyinizdi suraimin 😊')
        elif call.data == 'басқаертегі':
            bot.send_message(call.message.chat.id, 'Басқа да ертегілерді оқу үшін осы сілтемеге өтуіңізді өтінемін 😊'
                                                   'https://balalaralemi.kz/catalog/view/1')
        elif call.data == '1':
            bot.send_message(call.message.chat.id,
                             str(QaraSoz[0]))
        elif call.data == '...45':
            bot.send_message(call.message.chat.id,'Келесіз қарасөздерді оқу үшін төмендегі сілтемеге өтіңіз 😊'
                                                  'https://abai.kz/post/6 📌')

#Bastau
bot.polling()