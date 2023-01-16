# Импортируем библиотеку Telebot.
import telebot
# Создаем кнопку.
inline_bt1 = telebot.types.InlineKeyboardButton(
        "Замовити",
        callback_data= "замовити" 
    )
# Создаем вторую кнопку.
inline_bt2 = telebot.types.InlineKeyboardButton(
        "Перейти до сайту",
        url= "https://akspic.ru/album/best_wallpapers"
    )