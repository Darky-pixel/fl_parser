from bs4 import BeautifulSoup
import requests
import re
import json
import re
import sqlite3
import matplotlib

URL = "https://www.fl.ru/projects/category/programmirovanie/?page={page}&kind=5"

HEADERS = {"user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"}



def find_page(session):
    pages = []
    current_page = 1
    while True:
        pages.append(session.get(URL.format(page=current_page)))
        print(f"page {current_page} status code is {pages[-1].status_code}")
        current_page += 1
        if pages[-1].status_code != 200:
            pages = list(map(lambda elm:elm.text, pages[:-1]))
            break
    return pages



def pars_page(page):
    soup = BeautifulSoup(page, "lxml")
    projects_list = soup.find("div", id="projects-list")

    projects_body = projects_list.find_all("div", class_="b-post__grid")
    projects_body = list(map(lambda elm: elm.find_all("script", limit=2)[1].string.replace('document.write(\'<div class="b-post__body b-post__grid_descript b-post__body_overflow_hidden b-layuot_width_full"> <div class="b-post__txt ">', "").upper(),
                            projects_body))


    projects_head = projects_list.find_all("h2", class_="b-post__title b-post__grid_title p-0")
    projects_head = list(map(lambda elm : elm.text.upper(), projects_head))

    

    for i in range(len(projects_head)):
        projects_body[i] += projects_head[i]

    return projects_body




if __name__ == "__main__":

    projects = []

    data = {
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

    session = requests.session()
    session.post(URL.format(page=1), data=data)
    
    pages = find_page(session)

    # with open("index.html", encoding="utf-8") as file:
    #     pages = list(file.read())


    for i in pages:
        projects += pars_page(i)



    flask = 0
    django = 0
    telegram_bot = 0
    instagram_bot = 0
    vk_bot = 0
    unknown_bot = 0
    sql = 0


    for string in projects:
        if "SQL" in string:
            sql += 1

        if "DJANGO" in string:
            django += 1

        elif "FLASK" in string:
            flask += 1

        elif "БОТ" in string or "BOT" in string:

            if "TELEGRAM" in string or "ТЕЛЕГРАМ" in string:
                telegram_bot += 1

            elif "INSTAGRAM" in string or "ИНСТАГРАМ" in string:
                instagram_bot += 1

            elif "VK" in string or "ВК" in string:
                vk_bot += 1

            else:
                unknown_bot += 1



    print(f"""--------------------
Flask = {flask}
Django = {django}
Telegram bot = {telegram_bot}
Instagram bot = {instagram_bot}
Vk bot = {vk_bot}
unknown bot = {unknown_bot}
sql = {sql}
--------------------""")