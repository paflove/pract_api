
from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.inline import getInlineStartKeyBoard, getInlineUserSettingsKeyboard, getInlinePointSettingsKeyboard_M, getInlinePointSettingsKeyboard_SP
from aiogram.types import CallbackQuery
import time
import random
import logging
import requests
from middlewares.db import Request
router = Router()


@router.message(Command(commands=['start']))
async def startBotMessage(message: Message, request: Request):
    await message.answer(f'Привет! Парсер бот заработал',
                         reply_markup=getInlineStartKeyBoard())

@router.callback_query(F.data == "getUsersSettings")
async def chooseCity(call: CallbackQuery, request: Request):
    await call.message.answer("Выберете город:",
                            reply_markup=getInlineUserSettingsKeyboard())

@router.callback_query(F.data == "Moscow")
async def PointSettingsMos(call: CallbackQuery):
    await call.message.answer(f'Теперь выберите вакансию',
                              reply_markup=getInlinePointSettingsKeyboard_M())


@router.callback_query(F.data == "SP")
async def PointSettingsSpb(call: CallbackQuery):
    await call.message.answer(f'Теперь выберите вакансию',
                              reply_markup=getInlinePointSettingsKeyboard_SP())

@router.callback_query(F.data == "BI_M")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "BI Developer"
    city = "Москва"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]]) #и тд , просто в record указываещь нужную колонку из бд
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)




@router.callback_query(F.data == "BDM_M")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Business Development Manager"
    city = "Москва"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "CM_M")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Community Manager"
    city = "Москва"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)

@router.callback_query(F.data == "CV_M")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Computer vision"
    city = "Москва"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "DA_M")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Data Analyst"
    city = "Москва"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "BI_SP")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "BI Developer"
    city = "Санкт-Петербург"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "BDM_SP")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Business Development Manager"
    city = "Санкт-Петербург"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "CM_SP")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Community Manager"
    city = "Санкт-Петербург"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "CV_SP")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Computer vision"
    city = "Санкт-Петербург"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)


@router.callback_query(F.data == "DA_SP")
async def BiDev(call: CallbackQuery, request: Request):
    vacancy = "Data Analyst"
    city = "Санкт-Петербург"
    information = await request.getInformationFromVacancy(city, vacancy)
    messages = []
    for record in information:
        print(record['company'])
        messages.append([[f"Компания", f"{record['company']}", "Вакансия",  f"{record['vacancy']}", "Умения",f"{record['skills']}","Ссылка на вакансию", f"{record['url']}"]])
    elements = 0
    itog = ""
    for mess in messages:
        if elements == 2:
            await call.message.answer(itog)
            itog = ""
            for part in mess:
                itog += str(part) + " "
            elements = 1
            continue
        for part in mess:
            itog += str(part) + " "
        elements += 1
    if len(itog) > 0:
        await call.message.answer(itog)