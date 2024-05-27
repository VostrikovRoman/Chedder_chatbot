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
            bot.send_message(message.chat.id,'Телефон: +79221981149 \nАдрес: г.Нижний Тагил, ул. уральская, д. 38 \n',reply_markup = markup  )
        
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
            bot.send_message(message.chat.id, '🛒  Корзина', reply_markup = markup)
            
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
            vegatarian = types.KeyboardButton('vegetarian')
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
    
# parse_mode='html'  \\\\\ можно юзать подчеркивание, жирный текст, это вставляй : bot.send_message(chat.chat.id, 'Привет!', СУДА)
    
bot.polling(none_stop=True)