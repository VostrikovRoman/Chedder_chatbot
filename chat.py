from socket import *
from typing import BinaryIO

import telebot
from telebot import types

bot = telebot.TeleBot('6439697475:AAE2WVZvBn_5PLgu95iOSiwOsPdF2WTGF_Y')


@bot.message_handler(commands=['start'])

# def start(message):
#     HOST = ('26.134.159.187', 10000)
#
#     client = socket(AF_INET, SOCK_STREAM)
#     client.connect(HOST)
#     name = bytes(message.from_user.first_name, 'utf8')
#
#     sent = 0
#     request = b'1 ' + name
#     while sent < len(request):
#         sent = sent + client.send(request[sent:])


def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_menu = types.KeyboardButton('📖  Меню')
    btn_basket = types.KeyboardButton('🛒  Корзина')
    btn_info = types.KeyboardButton('ℹ️  О нас')

    markup.add(btn_menu, btn_basket, btn_info)
    bot.send_message(message.chat.id,
                     f'Привет, <b>{message.from_user.first_name}</b>, выбери что-нибудь из нашего меню, и мы начнём готовить твой заказ!',
                     parse_mode='html', reply_markup=markup)

    HOST = ('26.134.159.187', 10000)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(HOST)
    name = bytes(message.from_user.username, 'utf8')

    sent = 0
    request = b'1 ' + name
    while sent < len(request):
        sent = sent + client.send(request[sent:])
    print('отправил1')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'ℹ️  О нас':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_back)
            bot.send_message(message.chat.id,
                             'Чеддер - это пиццерия, основанная в Нижнем Тагиле. Мы специализируемся на приготовлении вкусной и качественной пиццы! В нашем чат-боте Вы можете просмотреть Нашу продукцию, а так же оформить Свой заказ, который мы приготовим для Вас быстро и вкусно!\n\n📞 Телефон: +79221981149 \n\nАдрес: г.Нижний Тагил, ул. уральская, д. 38 \n\n ОГРН: 2759305819394',
                             reply_markup=markup)

        elif message.text == '📖  Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_pizza = types.KeyboardButton('🍕  Пиццы')
            btn_snack = types.KeyboardButton('🍟  Снэки')
            btn_drinks = types.KeyboardButton('🥤  Напитки')
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_pizza, btn_drinks, btn_snack, btn_back)
            bot.send_message(message.chat.id, '📖  Меню', reply_markup=markup)

        elif message.text == 'Купить':
            bot.send_message(message.chat.id, 'Покупка совершена!')
        
        elif message.text == 'Удалить всё':
            bot.send_message(message.chat.id, 'Корзина очищена!')

            HOST = ('26.134.159.187', 10000)

            client = socket(AF_INET, SOCK_STREAM)
            client.connect(HOST)

            name = bytes(message.from_user.username, 'utf8')

            sent = 0
            request = b'4 ' + name
            while sent < len(request):
                sent = sent + client.send(request[sent:])
            print('отправил4')


        elif message.text == '🛒  Корзина':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_back = types.KeyboardButton('🔙  Назад')
            btn_pay = types.KeyboardButton('Купить')
            btn_del = types.KeyboardButton('Удалить всё')
            markup.add(btn_back, btn_pay, btn_del)

            HOST = ('26.134.159.187', 10000)

            client = socket(AF_INET, SOCK_STREAM)
            client.connect(HOST)

            name = bytes(message.from_user.username, 'utf8')

            sent = 0
            request = b'3 ' + name
            while sent < len(request):
                sent = sent + client.send(request[sent:])
            print('отправил3')

            msg = client.recv(2048)
            msg1 = (msg.decode('utf-8'))
            msg2 = msg1.split()
            zakaz = ''
            price = 0
            for i in msg2:
                q = menuKostil[int(i)].split(';')
                zakaz = zakaz + q[0] + '\n'
                price+=int(q[1])

            bot.send_message(message.chat.id, 'Ваш заказ:\n\n'+zakaz+'\nИТОГ: '+str(price)+' Р', reply_markup=markup)




        elif message.text == '🔙  Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_menu = types.KeyboardButton('📖  Меню')
            btn_basket = types.KeyboardButton('🛒  Корзина')
            btn_info = types.KeyboardButton('ℹ️  О нас')
            markup.add(btn_menu, btn_basket, btn_info)
            bot.send_message(message.chat.id, '📖  Меню', reply_markup=markup)

        elif message.text == '🍕  Пиццы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            margarita = types.KeyboardButton('Маргарита')
            pepperoni = types.KeyboardButton('Пепперони')
            for_season = types.KeyboardButton('Four Season')
            Hawaiian = types.KeyboardButton('Гавайская')
            Evil = types.KeyboardButton('Evil Pizza')
            Spring = types.KeyboardButton('Spring Pizza')
            Piter = types.KeyboardButton('Питерская')
            Four_cheese_sea = types.KeyboardButton('Four cheese sea')
            vegatarian = types.KeyboardButton('Vegetarian')
            Four_cheese = types.KeyboardButton('Четыре сыра')
            Beef = types.KeyboardButton('Мясная')
            carbonara = types.KeyboardButton('Карбонара')
            btn_back_2 = types.KeyboardButton('🔙   Назад')
            markup.add(margarita, pepperoni, for_season, Hawaiian, Evil, Spring, Piter, Four_cheese_sea, vegatarian,
                       Four_cheese, Beef, carbonara, btn_back_2)
            bot.send_message(message.chat.id, '🍕  Пиццы', reply_markup=markup)

        elif message.text == '🔙   Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_pizza = types.KeyboardButton('🍕  Пиццы')
            btn_snack = types.KeyboardButton('🍟  Снэки')
            btn_drinks = types.KeyboardButton('🥤  Напитки')
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_pizza, btn_drinks, btn_snack, btn_back)
            bot.send_message(message.chat.id, '📖  Меню', reply_markup=markup)


        elif message.text == '🍟  Снэки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            potato = types.KeyboardButton('Картофель фри')
            chiken_nag = types.KeyboardButton('Куриные наггетсы')
            chiken_str = types.KeyboardButton('Куриные стрипсы')
            btn_back_2 = types.KeyboardButton('🔙   Назад')
            markup.add(potato, chiken_nag, chiken_str, btn_back_2)
            bot.send_message(message.chat.id, '🍟  Снэки', reply_markup=markup)


        elif message.text == '🥤  Напитки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            obl = types.KeyboardButton('Облепиховый морс')
            black_cur = types.KeyboardButton('Морс из чёрной смородины')
            cherry = types.KeyboardButton('Вишнёвый морс')
            btn_back_2 = types.KeyboardButton('🔙   Назад')
            markup.add(obl, black_cur, cherry, btn_back_2)
            bot.send_message(message.chat.id, '🥤  Напитки', reply_markup=markup)

        ## Фотографии пицц ##

        elif message.text == 'Маргарита':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add1")
            inmenu.add(btn_add)
            margarita = open('1.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Маргарита\n\nСостав: Соус томатный, моцарелла, томат, базилик, чеснок, перец чёрный.\nДиаметр: 35 см. \nМасса нетто: 1300 гр.\nСтоимость: 899 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Пепперони':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add2")
            inmenu.add(btn_add)
            margarita = open('2.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Пепперони\n\nСостав: Соус томатный, колбаски пепперони, гауда, моцарелла\nДиаметр:35см.\nМасса нетто: 1000гр.\nСтоимость: 1350 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Four Season':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add3")
            inmenu.add(btn_add)
            margarita = open('3.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Four Season\n\nСостав: Соус томатный, ветчина, шампиньоны, артишок, оливки, чеддер,моцарелла\nДиаметр: 35см.\nМасса нетто: 1490 гр.\nСтоимость: 1620 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Гавайская':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add4")
            inmenu.add(btn_add)
            margarita = open('4.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Гавайская\n\nСостав: Соус томатный, кура запечённая, ананас, моцарелла, чеддер, соус белый\nДиаметр: 35см.\nМасса нетто: 1250 гр.\nСтоимость: 1300 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Evil Pizza':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add5")
            inmenu.add(btn_add)
            margarita = open('5.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Evil Pizza\n\nСостав: Томатный соус, моцарелла, салями, перец халапеньо, лук \nДиаметр:35см.\nМасса нетто: 1200 гр.\nСтоимость: 1010 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Spring Pizza':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add6")
            inmenu.add(btn_add)
            margarita = open('6.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Spring Pizza\n\nСостав: Томатный соус, моцарелла, чеддер кукуруза, томат, бекон\nДиаметр: 35см.\nМасса нетто: 1250 гр.\nСтоимость: 1380 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Питерская':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add7")
            inmenu.add(btn_add)
            margarita = open('7.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Питерская\n\nСостав: Томатный соус, моцарелла, салями, перец болгарский, томат, шампиньоны\nДиаметр: 35см.\nМасса нетто: 1300 гр.\nСтоимость: 1390 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Four cheese sea':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add8")
            inmenu.add(btn_add)
            margarita = open('8.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Four cheese sea\n\nСостав Сливочный соус, моцарелла, чеддер гауда, сыр с голубой плесенью, креветки:\nДиаметр: 30см.\nМасса нетто: 900 гр.\nСтоимость: 1560 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Vegetarian':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add9")
            inmenu.add(btn_add)
            margarita = open('9.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Vegetarian\n\nСостав: Томатный соус, томат, моцарелла, шампиньоны, лук, перец болгарский, кукуруза\nДиаметр: 40см.\nМасса нетто: 1480 гр.\nСтоимость: 1100 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Четыре сыра':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add10")
            inmenu.add(btn_add)
            margarita = open('10.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Четыре сыра\n\nСостав: Сливочный соус, чеддер, гауда, сыр с голубой плесенью, моцарелла\nДиаметр: 35см.\nМасса нетто: 1000 гр. \nСтоимость: 1340 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Мясная':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add11")
            inmenu.add(btn_add)
            margarita = open('11.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Мясная\n\nСостав: Томатный соус, чеддер, ветчина, томат, бекон \nДиаметр:35см.\nМасса нетто: 1400гр.\nСтоимость: 1560 ₽",
                           reply_markup=inmenu)

        elif message.text == 'Карбонара':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add12")
            inmenu.add(btn_add)
            margarita = open('12.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           "Пицца Карбонара\n\nСостав: Сливочный соус, моцарелла, бекон, чеддер, томат \nДиаметр:35см.\nМасса нетто: 1390 гр.\nСтоимость: 1250 ₽",
                           reply_markup=inmenu)

            ## фотографии пицц закончились ##

        ## фотографии снэков ##
        elif message.text == 'Картофель фри':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add13")
            inmenu.add(btn_add)
            margarita = open('13.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           'Картофель фри\n\nСостав: картофель, соль\nМасса нетто: 200гр\nСтоимость: 120 ₽',
                           reply_markup=inmenu)

        elif message.text == 'Куриные наггетсы':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add14")
            inmenu.add(btn_add)
            margarita = open('14.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           'Куриные наггетсы\n\nСостав: Филе куриное рубленное, соль, перец, паприка\nМасса нетто: 350гр\nКол-во: 10 шт\nСтоимость: 190 ₽',
                           reply_markup=inmenu)

        elif message.text == 'Куриные стрипсы':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add15")
            inmenu.add(btn_add)
            margarita = open('15.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           'Куриные стрипсы\n\nСостав: Филе куриное, соль, перец, кляр, специя "10 трав"\nМасса нетто: 300гр\nКол-во: 5 шт\nСтоимость: 240 ₽',
                           reply_markup=inmenu)

        ## фотографии снэков ##

        ## Фотографии напитков ##
        elif message.text == 'Облепиховый морс':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add18")
            inmenu.add(btn_add)
            margarita = open('18.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           'Облепиховый морс \n\nСостав: облепиха, вода, сахар\nОбъём: 400мл\nСтоимость: 105 ₽ ',
                           reply_markup=inmenu)

        elif message.text == 'Морс из чёрной смородины':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add17")
            inmenu.add(btn_add)
            margarita = open('17.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           'Морс из чёрной смородины\n\nСостав: чёрная смородина, вода, сахар\nОбъём: 400мл\nСтоимость: 105 ₽',
                           reply_markup=inmenu)

        elif message.text == 'Вишнёвый морс':
            inmenu = types.InlineKeyboardMarkup(row_width=1)
            btn_add = types.InlineKeyboardButton(text="Добавить ✅", callback_data="btn_add16")
            inmenu.add(btn_add)
            margarita = open('16.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,
                           'Вишнёвый морс\n\nСостав: вишня, вода, сахар\nОбъём: 400мл\nСтоимость: 105 ₽',
                           reply_markup=inmenu)
        ## Фотографии напитков ##


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == "btn_add1":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '1')

    elif callback.data == "btn_add2":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '2')

    elif callback.data == "btn_add3":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '3')

    elif callback.data == "btn_add4":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '4')

    elif callback.data == "btn_add5":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '5')

    elif callback.data == "btn_add6":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '6')

    elif callback.data == "btn_add7":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '7')

    elif callback.data == "btn_add8":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '8')

    elif callback.data == "btn_add9":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '9')

    elif callback.data == "btn_add10":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '10')

    elif callback.data == "btn_add11":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '11')

    elif callback.data == "btn_add12":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '12')

    elif callback.data == "btn_add13":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '13')

    elif callback.data == "btn_add14":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '14')

    elif callback.data == "btn_add15":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '15')

    elif callback.data == "btn_add16":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '16')

    elif callback.data == "btn_add17":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '17')

    elif callback.data == "btn_add18":
        bot.send_message(callback.message.chat.id, "Товар добавлен в корзину!")
        add_in_corzina(callback.from_user.username, '18')


def add_in_corzina(name, menu_id):
    HOST = ('26.134.159.187', 10000)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(HOST)
    name = bytes(name + ' ', 'utf8')
    menu_id = bytes(menu_id, 'utf8')
    sent = 0
    request = b'2 ' + name + menu_id
    while sent < len(request):
        sent = sent + client.send(request[sent:])
    print('отправил2')


menuKostil = ['Вас;зарекрорили!', 'Маргарита;899', 'Пепперони;1350', 'Four Season;1620', 'Гавайская;1300',
              'Evil Pizza;1010', 'Spring Pizza;1380', 'Питерская;1390', 'Four cheese sea;1560', 'Vegetarian;1100',
              'Четыре сыра;1340', 'Мясная;1560', 'Карбонара;1250', 'Картофель фри;120', 'Куриные наггетсы;190',
              'Куриные стрипсы;240', 'Вишнёвый морс;105', 'Морс из чёрной смородины;105', 'Облепиховый морс;105']

bot.polling(none_stop=True)
