import asyncio
import re
from aiogram import Bot, Dispatcher, types

bot = Bot(token="1362818951:AAEX6xNLeAK5N9Eah_lCme4q77pAMkUJSYA")
dp = Dispatcher(bot)

def getPhone(phone):
    numbers = re.findall("([0-9]){1,1}", phone)
    numbersLen = len(numbers)
    if (numbersLen==11):
        numbers[0]=7
    elif (numbersLen==10):
        numbers.insert(0,7)
    else:
        raise Exception("wrong phone (string param) length")
    return ''.join(str(number) for number in numbers)

@dp.message_handler()
async def phoneConverter(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, getPhone(msg.text))
    except:
        await bot.send_message(msg.from_user.id, "Incorrect phone format")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
