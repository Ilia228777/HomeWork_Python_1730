# Импортируем библиотеку как m_bot.
import modules.bot_creation as m_bot
# Импортируем библиотеку как m_keyboard.
import modules.keyboard_creation as m_keyboard
# Импортируем библиотеку как m_send_message.
import modules.user_sending_message as m_send_message
# Создаем команду start.
@m_bot.bot.message_handler(commands=["start"])
# Создаем функцию отправки сообщения ботом.
def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id, "Hi user!", 
        reply_markup=m_keyboard.menu_bar 
    )
    m_bot.bot.register_next_step_handler(
        message, 
        m_send_message.send_message_user
    )
