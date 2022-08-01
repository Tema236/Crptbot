import math
import crfun
import config
import telebot
from collections import defaultdict
#from telebot import types

user_by_messages = defaultdict(list)
keylist = defaultdict(list)
messages = []
messages1 = []
zd = ''
aclr = False
bot = telebot.TeleBot(config.token)

keyboard = telebot.types.InlineKeyboardMarkup()

keyboard.row(
    telebot.types.InlineKeyboardButton('Активация', callback_data='activate'),
    telebot.types.InlineKeyboardButton('clearing', callback_data='clear')
)
keyboard.row(
    telebot.types.InlineKeyboardButton('HOK', callback_data='HOK'),
    telebot.types.InlineKeyboardButton('HOD', callback_data='HOD'),
    telebot.types.InlineKeyboardButton('a mod b', callback_data='md')
)

keyboard.row(
    telebot.types.InlineKeyboardButton('zadacha 1', callback_data='zd1'),
    telebot.types.InlineKeyboardButton('zadacha 2', callback_data='zd2'),
    telebot.types.InlineKeyboardButton('zadacha 3', callback_data='zd3')
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Обратный элемент', callback_data='obr'),
    telebot.types.InlineKeyboardButton('Функция Эйлера', callback_data='fi')
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Китайская теорема об остатках', callback_data='ch_t'),
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Каноническое разложение числа на множители', callback_data='kan_r'),
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Обратимые элементы кольца', callback_data='ob_el'),
)

keyboard.row(
    telebot.types.InlineKeyboardButton('сл. т. Ферма', callback_data='sl_fe'),
    telebot.types.InlineKeyboardButton('сл. т. Эйлера', callback_data='sl_eil'),
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Поддержать разработку', callback_data='support'),
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Анонимная обратная связь', callback_data='anon'),
)

keyboard.row(
    telebot.types.InlineKeyboardButton('Посмотреть статистику(только для меня)', callback_data='stat'),
)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет тебе \nс криптой, чтобы увидеть список реашемых мной задач введи команду \n/tasks')
    bot.send_message(message.chat.id, 'ОБЯЗАТЕЛЬНО ПРОЧИТАТЬ ПЕРЕД ИСПОЛЬЗОВАНИЕМ https://telegra.ph/Post2-12-07-2')
    a = message.chat.username
    otv = str('@') + str(a) + str(' ') + str(message.chat.first_name)
    bot.send_message(message.chat.id, otv)
    print(a)

@bot.message_handler(commands=['tasks'])
def getMessage(message):
    bot.send_message(message.from_user.id, 'Выберите что вы хотите сделать', reply_markup=keyboard)
    a = message.chat.username
    otv = str('@') + str(a) + str(' ') + str(message.chat.first_name)
    bot.send_message(message.chat.id, otv)
    print(a)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'HOD':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('HOD')
        bot.send_message(call.message.chat.id, 'Найти НОД для 2х чисел. Введите отдельными сообщениями два числа.')

    if call.data == 'zd1':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('zd1')
        bot.send_message(call.message.chat.id, 'Введите: y,m,a,b. Пример: zd1;12001;3;00210;12010 (отдельными сообщениями)')

    if call.data == 'HOK':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('HOK')
        bot.send_message(call.message.chat.id, 'Найти НОК для 2х чисел. Введите отдельными сообщениями два числа.')

    if call.data == 'zd2':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('zd2')
        bot.send_message(call.message.chat.id, 'Введите: lambda и degf')

    if call.data == 'zd3':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('zd3')
        bot.send_message(call.message.chat.id, 'Введите: b, tay, n, m, t')

    if call.data == 'fi':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('fi')
        bot.send_message(call.message.chat.id, 'Введите число')

    if call.data == 'md':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('md')
        bot.send_message(call.message.chat.id, 'a mod b введите а, затем b')

    if call.data == 'clear':
        user_by_messages[call.message.chat.id].clear()
        bot.send_message(call.message.chat.id, 'Очистка выполнена', reply_markup=keyboard)

    if call.data == 'obr':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('obr')
        bot.send_message(call.message.chat.id, 'Введите число, а затем модуль')

    if call.data == 'ch_t':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('ch_t')
        bot.send_message(call.message.chat.id, 'x = a mod b вводите СНАЧАЛА b, а затем A, прекратить ввод - введите 0')

    if call.data == 'kan_r':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('kan_r')
        bot.send_message(call.message.chat.id, 'Введите число')

    if call.data == 'ob_el':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('ob_el')
        bot.send_message(call.message.chat.id, 'Введите число')

    if call.data == 'sl_fe':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('sl_fe')
        bot.send_message(call.message.chat.id, 'Введите сначала степень, а затем модуль')

    if call.data == 'sl_eil':
        user_by_messages[call.message.chat.id].clear()
        user_by_messages[call.message.chat.id].append('sl_eil')
        bot.send_message(call.message.chat.id, 'a^p mod m введите сначала a, затем p и m')

    if call.data == 'activate':
        user_id = call.message.chat.id
        print(user_id)
        for i in range(len(config.elite)):
            if (str(call.message.chat.id) == str(config.elite[i])) or (1 == 1):
                keylist[user_id] = True
                bot.send_message(call.message.chat.id, 'activated')
                user_by_messages[user_id].clear()
                break
        if keylist[user_id] != True:
            bot.send_message(call.message.chat.id, 'not activated, write the developer @temadadada')
        print(keylist)

    if call.data == 'support':
        bot.send_message(call.message.chat.id, 'Тинькофф')
        bot.send_message(call.message.chat.id, '5536 9139 8069 0685')

    if call.data == 'anon':
        user_by_messages[call.message.chat.id].append('anon')
        bot.send_message(call.message.chat.id, 'Напишите, что вам понравилось, что нет, сообщение полностью анонимное')

    if call.data == 'stat':
        if (call.message.chat.id == 1082154848):
            bot.send_message(1082154848, str(list(keylist.keys())))
        else:
            bot.send_message(call.message.chat.id, 'ONLY FOR ME, не тыкац больше')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    a = message.text
    user_id = message.from_user.id
    if user_by_messages[user_id][0] != 'ch_t':
        user_by_messages[user_id].append(a)

    if user_by_messages[user_id][0] == 'anon':
        bot.send_message(1082154848, a)
        bot.send_message(user_id, 'Спасибо за ваш ответ, надеюсь вам помог данный бот')
        return

    if keylist[user_id] == True:
        if user_by_messages[user_id][0] == 'ch_t':
            ch_r = []
            while True:
                if a != '0':
                    user_by_messages[message.from_user.id].append(int(a))
                    print(user_by_messages[user_id])
                    return
                elif a == '0':
                    break
                else:
                    bot.send_message(user_id, 'Not correct symbols')
            for i in range(1,len(user_by_messages[message.from_user.id]) - 1):
                if (i % 2) != 0:
                    ch_r.append((int(user_by_messages[user_id][i]), int(user_by_messages[user_id][i+1])))
                    print(ch_r)
            dch = crfun.chinese_remainder(ch_r)
            bot.send_message(message.chat.id, dch, reply_markup=keyboard)
            user_by_messages[user_id].clear()
            return
        if user_by_messages[user_id][0] == 'kan_r':
            if len(user_by_messages[user_id]) == 2:
                d8 = str(crfun.primfacs(int(user_by_messages[user_id][1])))
                bot.send_message(message.chat.id, d8, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'ob_el':
            if len(user_by_messages[user_id]) == 2:
                d9 = str(crfun.wz_pr_chisla(int(user_by_messages[user_id][1])))
                bot.send_message(message.chat.id, d9, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'sl_fe':
            if len(user_by_messages[user_id]) == 3:
                d10 = crfun.t_ferma(int(user_by_messages[user_id][1]),int(user_by_messages[user_id][2]))
                bot.send_message(message.chat.id, d10, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'sl_eil':
            if len(user_by_messages[user_id]) == 4:
                d11 = crfun.sl_el(int(user_by_messages[user_id][1]),int(user_by_messages[user_id][2]),int(user_by_messages[user_id][3]))
                bot.send_message(message.chat.id, d11, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'HOD':
            if len(user_by_messages[user_id]) == 3:
                d = math.gcd(int(user_by_messages[user_id][1]), int(user_by_messages[user_id][2]))
                bot.send_message(message.chat.id, d, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'zd1':
            if len(user_by_messages[user_id]) == 5:
                d1 = crfun.n212(user_by_messages[user_id][1], int(user_by_messages[user_id][2]), user_by_messages[user_id][3], user_by_messages[user_id][4])
                bot.send_message(message.chat.id, d1, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'HOK':
            if len(user_by_messages[user_id]) == 3:
                d2 = crfun.fnok(int(user_by_messages[user_id][1]), int(user_by_messages[user_id][2]))
                bot.send_message(message.chat.id, d2, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'zd2':
            if len(user_by_messages[user_id]) == 3:
                d3 = crfun.zd33(int(user_by_messages[user_id][1]), int(user_by_messages[user_id][2]))
                bot.send_message(message.chat.id, d3, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'zd3':
            if len(user_by_messages[user_id]) == 6:
                d4 = crfun.n43(int(user_by_messages[user_id][1]), int(user_by_messages[user_id][2]), int(user_by_messages[user_id][3]), int(user_by_messages[user_id][4]), int(user_by_messages[user_id][5]))
                bot.send_message(message.chat.id, d4, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'fi':
            if len(user_by_messages[user_id]) == 2:
                d5 = crfun.fi(int(user_by_messages[user_id][1]))
                bot.send_message(message.chat.id, d5, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'obr':
            if len(user_by_messages[user_id]) == 3:
                d6 = crfun.mulinv(int(user_by_messages[user_id][1]), int(user_by_messages[user_id][2]))
                bot.send_message(message.chat.id, d6, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        if user_by_messages[user_id][0] == 'md':
            if len(user_by_messages[user_id]) == 3:
                d7 = int(user_by_messages[user_id][1]) % int(user_by_messages[user_id][2])
                bot.send_message(message.chat.id, d7, reply_markup=keyboard)
                user_by_messages[user_id].clear()
                return
            else:
                return
        else:
            bot.send_message(message.chat.id,
                             'Вы неверно ввели данные, попробуйте снова:(',
                             reply_markup=keyboard)
            user_by_messages[user_id].clear()
            return
    else:
        bot.send_message(message.chat.id, "Бот не активирован, чтобы использовать полный его функционал активируйте его, нажав на кнопку Активация", reply_markup=keyboard)


if __name__ == '__main__':
     bot.infinity_polling()