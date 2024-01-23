from aiogram import Bot, Dispatcher
from aiogram.types.bot_command import BotCommand

import logging
import sys
import asyncio

from farm.chicken import router_chicken
from farm.cow import router_cow
from farm.sheep import router_sheep
from farm.bee import router_bee

from backyard.potato import router_potato
from backyard.tomato import router_tomato
from backyard.carrot import router_carrot
from backyard.cucumber import router_cucumber
from backyard.corn import router_corn
from backyard.beds import router_beds
from backyard.sale_bed import router_sale_beds
from backyard.backyard import router_backyard

from other.other_commands import router_other_command
from other.ads import router_ads
from other.level import router_level

from garden_Bot.garden import router_garden
from garden_Bot.trees import router_tree


async def main():
    proxy_url="http://proxy.server:3128"
    TOKEN = "5957173294:AAEIgZLBSCXfZM9mfPTayI8KygPFiYQXL5Q"
    bot = Bot(token=TOKEN)
    list = [
        ('start', 'Запуск бота 😁'),
        ('help', 'Допомога 🆘'),
        ('farm', 'Показує все, що є на фермі'),
        ('backyard', 'Показує все, що є на городі'),
        ('birthday', 'День народження бота 🥳'),
        ('level', 'Перевірити/підвищити рівень'),
        ('a', '----- Ферма -----'),
        ('chicken', 'Список команд для курей 🐔'),
        ('cow', 'Список команд для корів 🐮'),
        ('sheep', 'Список команд для овечки 🐏'),
        ('bee', 'Список команд для бджіл 🐝'),
        ('b', '----------'),
        ('get_eggs', 'Зібрати яйця 🥚'),
        ('get_milk', 'Зібрати молоко 🥛'),
        ('get_wool', 'Зібрати шерсть 🌫'),
        ('get_honey', 'Зібрати мед 🍯'),
        ('c', '----------'),
        ('sale_eggs', 'Продати яйця 🥚'),
        ('sale_milk', 'Продати молоко 🥛'),
        ('sale_wool', 'Продати шерсть 🌫'),
        ('sale_honey', 'Продати мед 🍯'),
        ('d', '----------'),
        ('buy_chicken', 'Купити курку 🐔'),
        ('buy_cow', 'Купити корову 🐮'),
        ('buy_sheep', 'Купити овечку 🐏'),
        ('buy_bee', 'Купити пасіку 🐝'),
        ('e', '----------'),
        ('sale_chicken', 'Продати курку 🐔'),
        ('sale_cow', 'Продати корову 🐮'),
        ('sale_sheep', 'Продати овечку 🐏'),
        ('sale_bee', 'Продати пасіку 🐝'),
        ('f', '----------'),
        ('farm_chicken', 'Збільшити курятник 🐔'),
        ('farm_cow', 'Збільшити корівник 🐮'),
        ('farm_sheep', 'Збільшити баранник 🐏'),
        ('farm_bee', 'Збільшити пасіку 🐝'),
        ('g', '----- Город -----'),
        ('buy_backyard', "Збільшити площу городу м²"),
        ('buy_bed', 'Купити грядку для овочів'),
        ('sale_bed', 'Продати грядку'),
        ('h', '----------'),
        ('get_potato', 'Зібрати картоплю 🥔'),
        ('get_tomato', 'Зібрати помідор 🍅'),
        ('get_carrot', 'Зібрати моркву 🥕'),
        ('get_cucumber', 'Зібрати огірок 🥒'),
        ('get_corn', 'Зібрати кукурудзу 🌽'),
        ('i', '----------'),
        ('sale_potato', 'Продати картоплю 🥔'),
        ('sale_tomato', 'Продати помідор 🍅'),
        ('sale_carrot', 'Продати морку 🥕'),
        ('sale_cucumber', 'Продати огірок 🥒'),
        ('sale_corn', 'Продати кукурудзу 🌽'),
    ]

    command_list = [BotCommand(command=cmd, description=desc) for cmd, desc in list]
    await bot.set_my_commands(command_list)
    
    dp = Dispatcher()

    dp.include_routers(router_chicken, router_cow, router_sheep, router_bee, router_potato, router_tomato, router_carrot, router_cucumber, router_corn, router_beds, router_sale_beds, router_ads, router_level, router_garden, router_tree, router_backyard, router_other_command)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Close connection with Telegram Servers")