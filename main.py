import logging
import random
import time
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from handlers.basic import router
from middlewares.db import DbSession
import asyncio
import asyncpg
import psycopg2
#Токен для тг бота
token = '7301514117:AAHRtLY1Rz1SZfe0I0jgQhTh6Kxbj-SPe3A'
hh_api_token = 'USERS5TPPE2K4IRIGP5JQU9LJ5SEESS2FH2DG56EPAT37HU3CTS5JTST82SCN6R1'



async def start_bot(bot:Bot):
    await bot.send_message(680830540, text='Бот запущен')

async def stop_bot(bot:Bot):
    await bot.send_message(680830540, text='Бот остановлен')


async def start():
    dp = Dispatcher()
    bot = Bot(token=token)
    bot.parse_mode = 'HTML'
    try:
        dp.include_router(router)
        # подключаем бд, асинхрон
        pool_connect = await asyncpg.create_pool(user='postgres', password='postgres',
                                                 database='myBd', host='localhost', port='5432', command_timeout=300)

        dp.update.middleware.register(DbSession(pool_connect))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()











##########################parser

def get_vacancies(city, vacancy, page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': f"{vacancy} {city}",
        'area': city,
        'specialization': 1,
        'per_page': 100,
        'page': page
    }
    headers = {
        'Authorization': f'Bearer {hh_api_token}'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Функция для получения навыков вакансии
def get_vacancy_skills(vacancy_id):
    url = f'https://api.hh.ru/vacancies/{vacancy_id}'
    headers = {
        'Authorization': f'Bearer {hh_api_token}'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    skills = [skill['name'] for skill in data.get('key_skills', [])]
    return ', '.join(skills)

# Функция для получения отрасли компании
def get_industry(company_id):
    # Получение отрасли компании по ее идентификатору
    if company_id is None:
        return 'Unknown'

    url = f'https://api.hh.ru/employers/{company_id}'
    response = requests.get(url)
    if response.status_code == 404:
        return 'Unknown'
    response.raise_for_status()
    data = response.json()

    if 'industries' in data and len(data['industries']) > 0:
        return data['industries'][0].get('name')
    return 'Unknown'

# Функция для парсинга вакансий
def parse_vacancies():
    cities = {
        'Москва': 1,
        'Санкт-Петербург': 2
    }

    vacancies = [
        'BI Developer', 'Business Development Manager', 'Community Manager', 'Computer vision',
        'Data Analyst'
    ]

    mass=[]
    for city, city_id in cities.items():
            for vacancy in vacancies:
                for page in range(2):
                        data = get_vacancies(city_id, vacancy, page)
                        if not data.get('items'):
                            break
                        for item in data['items']:
                            if vacancy.lower() not in item['name'].lower():
                                continue  # Пропустить, если название вакансии не совпадает

                            title = f"{item['name']} ({city})"
                            keywords = item['snippet'].get('requirement', '')
                            skills = get_vacancy_skills(item['id'])
                            company = item['employer']['name']
                            industry = get_industry(item['employer'].get('id'))
                            experience = item['experience'].get('name', '')
                            salary = item['salary']
                            if salary is None:
                                salary = "з/п не указана"
                            else:
                                salary = salary.get('from', '')
                            url = item['alternate_url']

                            mass.append([city, company, industry, title, keywords, skills, experience, salary, url, vacancy])


    logging.info("Парсинг завершен. Данные сохранены в базе данных PostgreSQL.")
    return mass


def parseToDataBase():
    #парсим
    data = parse_vacancies()
    #подключаем бд, не асинхрон
    connection = psycopg2.connect(
        user='postgres', password='postgres',
        database='myBd', host='localhost', port='5432'
    )
    for elements in data:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO information (city, company, industry, title, keywords, skills, experience, '
                           'salary, url, vacancy)'
                           'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (str(elements[0]), str(elements[1]), str(elements[2]), str(elements[3]), str(elements[4]), str(elements[5]),
                                                               str(elements[6]), str(elements[7]), str(elements[8]), str(elements[9])))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    parseToDataBase()
    print("Парсер закончил работу")
    asyncio.run(start())


