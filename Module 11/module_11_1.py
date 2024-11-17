import requests
from bs4 import BeautifulSoup
path_file = './index.html'

# Requests
url = 'https://yandex.ru/pogoda'
st_accept = 'text/html'
st_useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}
payload = {'city': 37107}

flag_upgrade = input('Обновить страничку в файле: y, n ')
if flag_upgrade == 'y':
    # пример использования метода 'get'
    response = requests.get(url, params=payload, headers=headers)
    response_text = response.text
    # пример использования метода 'status_code и 'codes.ok'
    if response.status_code == requests.codes.ok:
        # пример использования 'метода headers'
        print(response.headers.get('content-type'))
        with open(path_file, 'w', encoding='utf-8') as file:  # Сохраняю в файл, чтоб не нарваться на капчу.
            file.write(response_text)
else:
    with open(path_file, 'r', encoding='utf-8') as file:
        response_text = file.read()


# Пример использования библиотеки 'BeautifulSoup'
bs = BeautifulSoup(response_text, 'html.parser')
# Ищем тег с нужным названием
bs_sity = bs.find("h1", "title title_level_1 header-title__title")
bs_temp = bs.find("div", "temp fact__temp fact__temp_size_s")
# Печатаем нужные атрибуты
print(bs_sity.text, bs_temp.text)

# Пример использования метода 'perents' и 'parent'
for parent in bs_sity.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.attrs)
print(bs_temp.parent)
