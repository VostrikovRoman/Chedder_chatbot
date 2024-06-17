import telebot
from telebot import types
bot=telebot.TeleBot('6439697475:AAE2WVZvBn_5PLgu95iOSiwOsPdF2WTGF_Y')

@bot.message_handler(commands=['start'])
def main(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn_menu = types.KeyboardButton('📖  Меню')
    btn_basket = types.KeyboardButton('🛒  Корзина')
    btn_info = types.KeyboardButton('ℹ️  О нас')
   
    markup.add(btn_menu,btn_basket,btn_info)
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>, выбери что-нибудь из нашего меню, и мы начнём готовить твой заказ!', parse_mode='html', reply_markup = markup )

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'ℹ️  О нас':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_back)
            bot.send_message(message.chat.id,'Чеддер - это пиццерия, основанная в Нижнем Тагиле. Мы специализируемся на приготовлении вкусной и качественной пиццы! В нашем чат-боте Вы можете просмотреть Нашу продукцию, а так же оформить Свой заказ, который мы приготовим для Вас быстро и вкусно!\n\n📞 Телефон: +79221981149 \n\nАдрес: г.Нижний Тагил, ул. уральская, д. 38 \n\n ОГРН: 2759305819394',reply_markup = markup  )
        
        elif message.text == '📖  Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn_pizza = types.KeyboardButton('🍕  Пиццы')
            btn_snack = types.KeyboardButton('🍟  Снэки')
            btn_drinks = types.KeyboardButton('🥤  Напитки')
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_pizza,btn_drinks,btn_snack,btn_back)
            bot.send_message(message.chat.id, '📖  Меню', reply_markup = markup)
            
        elif message.text == '🛒  Корзина':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_back)
            bot.send_message(message.chat.id, 'Приносим свои извинения, но данный раздел в разработке.\nА пока Вы можете оформить свой заказ в нашем ресторане, либо позвонив по нашему номеру: \n📞 +79221981149', reply_markup = markup)
            
        elif message.text == '🔙  Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn_menu = types.KeyboardButton('📖  Меню')
            btn_basket = types.KeyboardButton('🛒  Корзина')
            btn_info = types.KeyboardButton('ℹ️  О нас')
            markup.add(btn_menu,btn_basket,btn_info)
            bot.send_message(message.chat.id, '📖  Меню', reply_markup = markup)
   
        elif message.text == '🍕  Пиццы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
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
            markup.add(margarita,pepperoni,for_season,Hawaiian,Evil,Spring,Piter,Four_cheese_sea,vegatarian,Four_cheese,Beef,carbonara,btn_back_2)
            bot.send_message(message.chat.id, '🍕  Пиццы', reply_markup = markup)
        
        elif message.text == '🔙   Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn_pizza = types.KeyboardButton('🍕  Пиццы')
            btn_snack = types.KeyboardButton('🍟  Снэки')
            btn_drinks = types.KeyboardButton('🥤  Напитки')
            btn_back = types.KeyboardButton('🔙  Назад')
            markup.add(btn_pizza,btn_drinks,btn_snack,btn_back)
            bot.send_message(message.chat.id, '📖  Меню', reply_markup = markup)  
        
        
        elif message.text == '🍟  Снэки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            potato = types.KeyboardButton('Картофель фри')
            chiken_nag = types.KeyboardButton('Куриные наггетсы')
            chiken_str = types.KeyboardButton('Куриные стрипсы')
            btn_back_2 = types.KeyboardButton('🔙   Назад')
            markup.add(potato, chiken_nag, chiken_str, btn_back_2)
            bot.send_message(message.chat.id, '🍟  Снэки', reply_markup = markup)
                
                
        elif message.text == '🥤  Напитки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            obl = types.KeyboardButton('Облипиховый морс')
            black_cur = types.KeyboardButton('Морс из чёрной смородины')
            cherry = types.KeyboardButton('Вишнёвый морс')
            btn_back_2 = types.KeyboardButton('🔙   Назад')
            markup.add(obl, black_cur, cherry,  btn_back_2)
            bot.send_message(message.chat.id, '🥤  Напитки', reply_markup = markup)
            
            
            
            
        ## Фотографии пицц ##
        
        elif message.text == 'Маргарита':
            margarita = open('1.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Маргарита\n\nСостав: Соус томатный, моцарелла, томат, базилик, чеснок, перец чёрный.\nДиаметр: 35 см. \nМасса нетто: 1300 гр.\nСтоимость: 899 ₽")
            
        elif message.text == 'Пепперони':
            margarita = open('2.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Пепперони\n\nСостав: Соус томатный, колбаски пепперони, гауда, моцарелла\nДиаметр:35см.\nМасса нетто: 1000гр.\nСтоимость: 1350 ₽")  
            
        elif message.text == 'Four Season':
            margarita = open('3.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Four Season\n\nСостав: Соус томатный, ветчина, шампиньоны, артишок, оливки, чеддер,моцарелла\nДиаметр: 35см.\nМасса нетто: 1490 гр.\nСтоимость: 1620 ₽")  
            
        elif message.text == 'Гавайская':
            margarita = open('4.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Гавайская\n\nСостав: Соус томатный, кура запечённая, ананас, моцарелла, чеддер, соус белый\nДиаметр: 35см.\nМасса нетто: 1250 гр.\nСтоимость: 1300 ₽") 
            
        elif message.text == 'Evil Pizza':
            margarita = open('5.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Evil Pizza\n\nСостав: Томатный соус, моцарелла, салями, перец халапеньо, лук \nДиаметр:35см.\nМасса нетто: 1200 гр.\nСтоимость: 1010 ₽") 
            
        elif message.text == 'Spring Pizza':
            margarita = open('6.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Spring Pizza\n\nСостав: Томатный соус, моцарелла, чеддер кукуруза, томат, бекон\nДиаметр: 35см.\nМасса нетто: 1250 гр.\nСтоимость: 1380 ₽") 
            
        elif message.text == 'Питерская':
            margarita = open('7.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Питерская\n\nСостав: Томатный соус, моцарелла, салями, перец болгарский, томат, шампиньоны\nДиаметр: 35см.\nМасса нетто: 1300 гр.\nСтоимость: 1390 ₽") 
            
        elif message.text == 'Four cheese sea':
            margarita = open('8.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Four cheese sea\n\nСостав Сливочный соус, моцарелла, чеддер гауда, сыр с голубой плесенью, креветки:\nДиаметр: 30см.\nМасса нетто: 900 гр.\nСтоимость: 1560 ₽") 
            
        elif message.text == 'Vegetarian':
            margarita = open('9.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Vegetarian\n\nСостав: Томатный соус, томат, моцарелла, шампиньоны, лук, перец болгарский, кукуруза\nДиаметр: 40см.\nМасса нетто: 1480 гр.\nСтоимость: 1100 ₽")  
            
        elif message.text == 'Четыре сыра':
            margarita = open('10.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Четыре сыра\n\nСостав: Сливочный соус, чеддер, гауда, сыр с голубой плесенью, моцарелла\nДиаметр: 35см.\nМасса нетто: 1000 гр. \nСтоимость: 1340 ₽") 
            
        elif message.text == 'Мясная':
            margarita = open('11.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Мясная\n\nСостав: Томатный соус, чеддер, ветчина, томат, бекон \nДиаметр:35см.\nМасса нетто: 1400гр.\nСтоимость: 1560 ₽")  
            
        elif message.text == 'Карбонара':
            margarita = open('12.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita, "Пицца Карбонара\n\nСостав: Сливочный соус, моцарелла, бекон, чеддер, томат \nДиаметр:35см.\nМасса нетто: 1390 гр.\nСтоимость: 1250 ₽") 
            
        ## фотографии пицц закончились ##    
            
        ## фотографии снэков ##
        elif message.text == 'Картофель фри':
            margarita = open('13.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,'Картофель фри\n\nСостав: картофель, соль\nМасса нетто: 200гр\nСтоимость: 120 ₽')
            
        elif message.text == 'Куриные наггетсы':
            margarita = open('14.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,'Куриные наггетсы\n\nСостав: Филе куриное рубленное, соль, перец, паприка\nМасса нетто: 350гр\nКол-во: 10 шт\nСтоимость: 190 ₽')
            
        elif message.text == 'Куриные стрипсы':
            margarita = open('15.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,'Куриные стрипсы\n\nСостав: Филе куриное, соль, перец, кляр, специя "10 трав"\nМасса нетто: 300гр\nКол-во: 5 шт\nСтоимость: 240 ₽')
        
        ## фотографии снэков ##
            
        ## Фотографии напитков ##
        elif message.text == 'Облипиховый морс':
            margarita = open('18.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,'Облипиховый морс\n\nСостав: облипиха, вода, сахар\nОбъём: 400мл\nСтоимость: 105 ₽ ')
            
        elif message.text == 'Морс из чёрной смородины':
            margarita = open('17.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,'Морс из чёрной смородины\n\nСостав: чёрная смородина, вода, сахар\nОбъём: 400мл\nСтоимость: 105 ₽')
            
        elif message.text == 'Вишнёвый морс':
            margarita = open('16.jpg', 'rb')
            bot.send_photo(message.chat.id, margarita,'Вишнёвый морс\n\nСостав: вишня, вода, сахар\nОбъём: 400мл\nСтоимость: 105 ₽')
        ## Фотографии напитков ##
            
        
# parse_mode='html'  \\\\\ можно юзать подчеркивание, жирный текст, это вставляй : bot.send_message(chat.chat.id, 'Привет!', СУДА)
    
bot.polling(none_stop=True)