import requests
from bs4 import BeautifulSoup
import csv
"""https://www.kiper.by/catalog/bms-akb-control/"""

""" Функция для получения кода HTML"""
def get_html(url):
    r = requests.get(url)
    return r.text
"""Нормализуем информацию рейтинга.
Приводим данные к виду без запятых"""
def refined(s):
    """split с пробелом разбивает в список по "пробелу", [0] забирает первое
    значение из списка"""
    raiting = s.split(' ')[0]
    """replace заменяет ',' на пустоту """
    result = raiting.replace(',', '')
    return result

"""Записываем данные all_data в csv файл"""
def write_csv(all_data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((all_data['name'],
                         all_data['url'],
                         all_data['rating']))





"""В фнкцию передается HTML из def get_html(url) и создается объект BeautifulSoup
для последующего поиска необходимой информации в HTML"""
def get_date(html):
    suop = BeautifulSoup(html, 'lxml')
    popular = suop.find_all("section")[3]
    plagins = popular.find_all('article')

    for plagin in plagins:
        name = plagin.find('h3').text
        href = plagin.find('h3').find('a').get('href')
        rewie = plagin.find("span", class_="rating-count").find("a").text
        rating = refined(rewie)
        #print(rating)

        all_data = {'name':name, 'url':href, 'rating':rating}

        #print(all_data)
        write_csv(all_data)

    #return plagins

##print(get_html("https://www.kiper.by/catalog/bms-akb-control/"))

def main():
    url = "https://wordpress.org/plugins/"
    print(get_date(get_html(url)))



if __name__  == '__main__':
    main()