from bs4 import BeautifulSoup
import requests
import aiohttp
import asyncio
import time

URL = "https://www.fl.ru/projects/category/programmirovanie/?page={page}&kind=5"

HEADERS = {"user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"}

DATA = {
        'action': 'postfilter',
        'kind': '1',
        'pf_category': None,
        'pf_subcategory': None,
        'comboe_columns[1]': '0',
        'comboe_columns[0]': '0',
        'comboe_column_id': '0',
        'comboe_db_id': '0',
        'comboe': 'Все специализации',
        'pf_categofy[0][5]': '0',
        'pf_cost_from': None,
        'pf_cost_to': None,
        'pf_keywords': 'python',
        'u_token_key': None,
    }


async def find_pages():
    async with aiohttp.ClientSession() as session:
        # response = await session.get(url=URL.format(page=1), headers=HEADERS, data = DATA)
        tasks = []



def main_pars():
    
    asyncio.run(find_pages())

    '''
    proj_prep = dict( # projects_prepared
    flask = 0, 
    django = 0,
    telegram_bot = 0,
    instagram_bot = 0,
    vk_bot = 0,
    unknown_bot = 0,
    sql = 0,)


    for string in projects:
        if "SQL" in string:
            proj_prep['sql'] += 1

        if "DJANGO" in string:
            proj_prep['django'] += 1

        elif "FLASK" in string:
            proj_prep['flask'] += 1

        if "БОТ" in string or "BOT" in string:

            if "TELEGRAM" in string or "ТЕЛЕГРАМ" in string:
                proj_prep['telegram_bot'] += 1

            elif "INSTAGRAM" in string or "ИНСТАГРАМ" in string:
                proj_prep['instagram_bot'] += 1

            elif "VK" in string or "ВК" in string:
                proj_prep['vk_bot'] += 1 

            else: 
                proj_prep['unknown_bot'] += 1 



    print(f"""
--------------------
Flask = {proj_prep['flask']}
Django = {proj_prep['django']}
Telegram bot = {proj_prep['telegram_bot']}
Instagram bot = {proj_prep['instagram_bot']}
Vk bot = {proj_prep['vk_bot']}
unknown bot = {proj_prep['unknown_bot']}
sql = {proj_prep['sql']}
--------------------
""")
    del proj_prep['unknown_bot']
    return proj_prep

    '''

if __name__ == "__main__":
    main_pars()