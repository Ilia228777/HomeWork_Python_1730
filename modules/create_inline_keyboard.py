# Импортируем библиотеку как m_inline_bt.
import modules.create_inline_button as m_inline_bt
# Импортируем библиотеку Telebot.
import telebot
# Задаем размер кнопки сообщения бота.
inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
# Привязываем эту кнопку к остальным.
inline_keyboard.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt2)