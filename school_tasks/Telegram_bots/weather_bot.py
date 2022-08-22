import requests
from datetime import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types
import psycopg2


postgres = psycopg2.connect(
    dbname='startsql',
    user='alikhanov',
    password='12345',
    host='localhost'
)

cursor = postgres.cursor()

ow_api = ''
t_api = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=t_api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Здр напишите название города")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={ow_api}&units=metric&lang=ru').json()

        time = datetime.fromtimestamp(r['dt'])
        temp = r['main']['temp']
        humidity = r['main']['humidity']
        city = r['name']
        country = r['sys']['country']
        sunrise = datetime.fromtimestamp(r['sys']['sunrise'])
        sunset = datetime.fromtimestamp(r['sys']['sunset'])
        weather = r['weather'][0]['description']
        wind = r['wind']['speed']
    except:
        await message.answer('Error')
    else:
        await message.answer(f"""
        Время : {time}
        Температура : {temp}
        Влажность : {humidity}
        Город : {city}
        Страна : {country}
        Восход : {sunrise}
        Закат : {sunset}
        Описание : {weather}
        Скорость ветра : {wind}
        """)

        cursor.execute(f"INSERT INTO weather(time, temp, humidity, city, country, sunrise, sunset, descr, wind) VALUES ('{time}', '{temp}', '{humidity}', '{city}', '{country}', '{sunrise}', '{sunset}', '{weather}', '{wind}');")
        cursor.execute("SELECT * FROM weather")
        print(cursor.fetchall())
        postgres.commit()

        with open("/Users/alikhanov/Desktop/weather_db.txt", "a") as adder:
            adder.write(str(f"""
        Время : {time}
        Температура : {temp}
        Влажность : {humidity}
        Город : {city}
        Страна : {country}
        Восход : {sunrise}
        Закат : {sunset}
        Описание : {weather}
        Скорость ветра : {wind}
        """))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
