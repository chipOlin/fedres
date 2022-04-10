import telebot
import time
import datetime
from multiprocessing import *
import schedule
import main

# telebot.apihelper.proxy = {'PROXY'}
API_TOKEN = '1876044724:AAF2JMbTu5QsbBY40qbytjqZSL8wwlR0zMw'
bot = telebot.TeleBot(API_TOKEN)
debtor_dict = {}


def start_process():  # Запуск Process
    p1 = Process(target=P_schedule.start_schedule, args=()).start()


class P_schedule():  # Class для работы с schedule
    def start_schedule():  # Запуск schedule
        ######Параметры для schedule######
        # schedule.every().day.at("11:02").do(P_schedule.send_message1)
        schedule.every(1).minutes.do(P_schedule.send_message2)
        ##################################

        while True:  # Запуск цикла
            schedule.run_pending()
            time.sleep(1)

    ####Функции для выполнения заданий по времени
    def send_message1():
        bot.send_message(USER_ID, 'Отправка сообщения по времени')

    def send_message2():
        ldebt = main.get_data()
        if len(ldebt) > 0:
            for x, y in ldebt.items():
                if not x in debtor_dict:
                    mes = "\n".join(y.values())
                    bot.send_message(256155479, f'{x}\n{mes}')
                    debtor_dict[x] = ldebt[x]
        print(time.strftime('%c'))
        # 1915793473 - id резервный
        # 256155479 - id_2 основной
    ################


###Настройки команд telebot#########
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Нажали start')
    # bot.send_message(message.chat.id, print(message))
    # print(message)
#####################


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass
