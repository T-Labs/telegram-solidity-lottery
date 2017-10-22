# -*- coding: utf-8 -*-

import telebot
import config
from eth_rpc_client import Client


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, важно не повторяться
    client = Client(host="ubuntu.athex.ru", port="8545")
    bot.send_message(message.chat.id, client.get_balance(client.get_coinbase()))

if __name__ == "__main__":
    bot.polling(none_stop=True)