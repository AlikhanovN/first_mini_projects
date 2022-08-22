import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

tgbot_token = '1915579708:AAE-9eZAF_DuzN59Wr4RHgdsq2518f2cQrA'
bot = Bot(token=tgbot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


class Parking:
    #  Enter string - "Model avto number", integer - time
    total_places = 20
    number_list = []
    total_money = 0
    total_hours = 0
    def __init__(self, avto_model_number, wanted_time):
        if Parking.total_places > 0:
            self.validate_avto(avto_model_number)
            self.validation_time(wanted_time)
            self.__avto = f"{avto_model_number.split()[0]}, {avto_model_number.split()[1]}"
            self.__wanted_time = wanted_time
            self.__free_count = Parking.total_places  # 4 floor, each by 5 places
            Parking.total_places = self.__free_count - 1
            self.__park_time = datetime.datetime.now()
            self.__cost = 25
            self.__total_price = 25 * wanted_time
            Parking.total_money += self.__total_price
            Parking.total_hours += self.__wanted_time
            self.__free_ground = abs(-(Parking.total_places + 1) // 5)
        else:
            print("No Places")


    def __str__(self):
        return f"""
    ==================================
    
        Auto: {self.__avto}
        Free places: {self.__free_count}
        Parking time: {self.__park_time.strftime("%A, %d. %B %Y %H:%M")}
        Total price: {self.__total_price} {"som"}
        Free grounds: {tuple([i for i in range(5 - self.__free_ground, 5)])}
    ==================================
        """
    def __call__(self, number):
        print(number)

    @classmethod
    def validate_avto(cls, av):
        print(av.split())
        if type(av) != str:
            raise TypeError("Only String")

        if len(av.split()) != 2:
            raise TypeError("Enter 'Model Number'")

        if len(av.split()[1]) != 7:
            raise TypeError("Number must have 7 characters")
        if av.split()[1] in Parking.number_list:
            raise ValueError("Already exist")
        else:
            Parking.number_list.append(av.split()[1])

    @classmethod
    def validation_time(cls, time):
        if type(time) != int:
            raise TypeError("Only whole numbers")

        if time < 1 or time > 168:
            raise ValueError("Min 1, Max 168 hours")

    @property
    def park_model(self):
        return Parking.total_places
    @park_model.deleter
    def park_model(self, res):
        Parking.total_places += 1





@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    await message.reply("""
Hi, you are in the <b>Parking</b>!
    
Enter your car model and id, how many hours you want.\nExample: <b>Mercedes 77NA177, 5</b>

For <b>EXIT</b> Enter: /exit car number
""")

@dp.message_handler(commands="count")
async def full_parking(message: types.Message):
    print(Parking.total_places)
    await message.answer(f"<b>Cars in Parking:</b> {20 - Parking.total_places},  <b>Cars:</b> {Parking.number_list}")

@dp.message_handler(commands="total")
async def full_parking(message: types.Message):
    print(Parking.total_money)
    await message.answer(f"<b>Total money for today:</b>{Parking.total_money},  <b>Total parking hours</b> {Parking.total_hours}")

@dp.message_handler(commands="exit")
async def full_parking(message: types.Message):
    # await message.reply("Enter car's number")
    Parking.__call__(Parking, message.text.split()[1])
    await message.answer(f"<b>Car {message.text.split()[1]} exit </b>")
    Parking.number_list.remove(message.text.split()[1])
    Parking.total_places += 1


@dp.message_handler()
async def parking_info(message: types.Message):
    a = f"visitor = Parking('{message.text.split(',')[0]}',{message.text.split(',')[1]})"
    exec(a)
    await message.answer(eval(a.split()[0]))



# exec('alex = Parking("Mercedes 77NA177", 5)')
# print(alex)





#  Tests.....

# alex = Parking("Mercedes 77NA177", 5)
# dany = Parking("Hyundai 77SS577", 3)
# any = Parking("Kia 77OI789", 2)
# sam = Parking("Mazda 99St547", 1)
# jony = Parking("Chevrolet 77HH873", 6)
# april = Parking("Toyota 77PO999", 8)
# alex2 = Parking("Mercedes 77NA177", 9)
# dany2 = Parking("Hyundai 77SS577", 3)
# any2 = Parking("Kia 77OI789", 2)
# sam2 = Parking("Mazda 99St547", 1)
# jony2 = Parking("Chevrolet 77HH873", 4)
#
# print(alex)
# print(dany)
# print(any)
# print(sam)
# print(jony)
# print(april)
# print(alex2)
# print(dany2)
# print(any2)
# print(sam2)
# print(jony2)
# print(jony2.total_places)
# del jony2.park_model
# jony3 = Parking("Chevrolet 77HH555", 4)
# print(jony3)
# print(jony3.total_places)

if __name__ == '__main__':
    executor.start_polling(dp)