"""1.1: Дан список адресов. Заменить все  названия доменов (netloc) на 'www.admin.ru', используя метод .replace(). Метод возвращает новый объект ParseResult, заменяя указанные поля новыми значениями.
Например, список:
//www.cwi.nl:80/%7Eguido/Python.html
http://stackoverflow.com/search?q=question
http://www.example.org/default.html?ct=32&op=92&item=98
Получили:
//www.admin.ru/%7Eguido/Python.html
http://www.admin.ru/search?q=question
http://www.admin.ru/default.html?ct=32&op=92&item=98
"""
from urllib.parse import urlparse, urlunparse

def rmain(list, new):
    replace = []
    for url in list:
        parse = urlparse(url)
        repoc = new
        replac = parse._replace(netloc=repoc)
        replace.append(urlunparse(replac))
    return replace
urls = [
    "https://www.beatstars.com/k0nelsprod24",
    "https://www.youtube.com/channel/UCLOS66hR2HKPhOM3hIa7qTg",
    "https://www.instagram.com/k0nels/"]
newdom = 'www.admin.ru'
rurls = rmain(urls, newdom)
for url in rurls:
    print(url)
