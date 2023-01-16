# Импортируем библиотеку как m_button.
import modules.button_creation as m_button
# Импортируем библиотеку Telebot.
import telebot
# Создаем кнопки ответа снизу чата.
menu_bar = telebot.types.ReplyKeyboardMarkup()
# Привязываем эту кнопку к остальным.
menu_bar.add(m_button.button1)