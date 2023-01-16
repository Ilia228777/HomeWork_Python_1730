# Импортируем библиотеку как m_bot.
import modules.bot_creation as m_bot
# Импортируем библиотеку как m_path.
import modules.find_path as m_path
# Импортируем библиотеку как m_inline_key.
import modules.create_inline_keyboard as m_inline_key
# Создаем функцию, которая будет принимать/отправлять сообщения.
def send_message_user(message):
    if message.text.lower() == "get picture":
        path_file = m_path.find_path_file("images/1.jpeg")
        m_bot.bot.send_photo(
            message.chat.id, 
            open(path_file, "rb"),
            "Повітряна куля",
            reply_markup= m_inline_key.inline_keyboard
        )