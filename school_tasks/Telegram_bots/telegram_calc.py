import telebot

tg_token = "1915579708:AAE-9eZAF_DuzN59Wr4RHgdsq2518f2cQrA"
bot = telebot.TeleBot(tg_token)

@bot.message_handler(content_types=['text'])
def welcome(pm):
    first_message = bot.send_message(pm.chat.id, "Welcome, my name is Salco, i'm simple calculator. Enter 1st number: ")
    bot.register_next_step_handler(first_message, name_handler)


def name_handler(pm):
    first_num = pm.text
    second_mes = bot.send_message(pm.chat.id, "Enter operation: (+ - * /)")
    bot.register_next_step_handler(second_mes, oper_handler, first_num)


def oper_handler(pm, first_num):
    operation = pm.text
    therd_mes = bot.send_message(pm.chat.id, "Enter 2nd number: ")
    bot.register_next_step_handler(therd_mes, sec_mes, first_num, operation)

def sec_mes(pm, first_num, operation):
    second_num = pm.text
    res = 0
    try:
        if operation in ["+", "-", "*", "/"]:
            if operation == "+":
                res = int(first_num) + int(second_num)
            elif operation == "-":
                res = int(first_num) - int(second_num)
            elif operation == "*":
                res = int(first_num) * int(second_num)
            elif operation == "/":
                res = int(first_num) / int(second_num)
            last_mes = bot.send_message(pm.chat.id, f"The answer: {first_num} {operation} {second_num} = {res}")
        else:
            bot.send_message(pm.chat.id, "Enter correct operation")
    except ValueError:
        bot.send_message(pm.chat.id, "Enter only Digits!")
    except ZeroDivisionError:
        bot.send_message(pm.chat.id, "Can not division by zero!")


bot.polling(none_stop=True)

