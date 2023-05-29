"""
    Напишите программу, которая будет скачивать страницы из списка URL-адресов и сохранять их в отдельные файлы на диске.
    В списке может быть несколько сотен URL-адресов.
    При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
    Представьте три варианта решения.

"""

import requests
import threading
import multiprocessing
import aiohttp
import asyncio


URL_LIST = [
    'https://gb.ru/',
    'https://google.com/',
    'https://yandex.ru/',
    'https://mail.ru/',
    'https://python.org/',
    'https://rambler.ru/',
    'https://vk.com/',
    'https://yahoo.com/',
]


def parser_url_threads(url, file_name):
    response = requests.get(url)
    with open(file_name, 'w', encoding='UTF-8') as f:
        f.write(response.text)
    print(f'Записал страницу по этому адресу: {url}')


async def parser_url(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_name, 'w', encoding='UTF-8') as f:
                _response = await response.text()
                f.write(_response)
                print(f'Записал страницу по этому адресу: {url}')


if __name__ == '__main__':

    threads = []

    for url in URL_LIST:
        t = threading.Thread(target=parser_url_threads, args=(url, f'file_name_theards.txt'))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(50*'*')
    threads = []

    for url in URL_LIST:
        p = multiprocessing.Process(target=parser_url_threads, args=(url, f'file_name_multip.txt'))
        threads.append(p)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(50 * '*')
    tasks = []

    for url in URL_LIST:
        task = asyncio.ensure_future(parser_url(url, f'async_asyncio.html'))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))