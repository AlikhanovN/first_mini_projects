import json
import requests
from pprint import pprint
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


tgbot_token = '1915579708:AAE-9eZAF_DuzN59Wr4RHgdsq2518f2cQrA'
bot = Bot(token=tgbot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    with open('sulpak_for_bot.csv', 'r') as f:
        # print(f.readlines()[2::6])
        btn_list = ''
        a = 0

        for name in f.readlines()[2::6]:
            # print(name.strip())
            btn_list += f"InlineKeyboardButton(str('{name.strip()[8:]}'), callback_data='{a}'), "
            a += 1
        # print(btn_list[:-2])
        inl_kb_btns = f"InlineKeyboardMarkup(row_width=1).add({btn_list[:-2]})"
        await message.reply('Выберите:', reply_markup=eval(inl_kb_btns))


@dp.callback_query_handler()
async def get_chatacter(callback_query: types.CallbackQuery):
    with open('sulpak_for_bot.csv', 'r') as f:
        # print(f.readlines()[4::6][4])
        # print(f.readlines()[1::6][0])
        caption = (f"""
        Price : {f.readlines()[5::6][int(callback_query.data)]}
        """)
        f.seek(0)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=f.readlines()[1::6][int(callback_query.data)][:-3], caption=caption)


# r = requests.get('https://rickandmortyapi.com/api/character').json()
# res_list = []
# for i in range(20):
#     character_quatity = r['results']
#     name = character_quatity[i]['name']
#     gender = character_quatity[i]['gender']
#     status = character_quatity[i]['status']
#     image = character_quatity[i]['image']
#     data = {
#         'name': name,
#         'gender': gender,
#         'status': status,
#         'image': image,
#     }
#     res_list.append(data)
# with open('data.json', 'a') as f:
#     json.dump(res_list, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    executor.start_polling(dp)