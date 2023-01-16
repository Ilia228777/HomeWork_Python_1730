# Импортируем библиотеку как m_bot.
import modules.bot_creation as m_bot
# Импортируем библиотеку как m_start.
import modules.command_start as m_start
# Импортируем библиотеку processing_request.
import modules.processing_request 
# Принимает сообщения.
m_bot.bot.polling(none_stop=True)