# Импортируем библиотеку как m_bot.
import modules.bot_creation as m_bot
# Создаем метод, который будет принимать заказы.
@m_bot.bot.callback_query_handler(func= lambda callback: callback.data)
# Создаем функцию, которая будет оформлять заказы.
def processing_callback(callback):
    if callback.data == "замовити":
        m_bot.bot.send_message(
            callback.message.chat.id, 
            "Ваше замовлення прийняте в обробку\nОчікуйте зворотнього зв'язку!"
        )
