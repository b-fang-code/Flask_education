import time
import requests
import os
import asyncio
import aiohttp

urls = ['https://rare-gallery.com/uploads/posts/795837-Cats-Eyes-Glance-Whiskers-Snout-Nose.jpg',
        'https://wallbox.ru/wallpapers/main/201546/13dcd7162ea7a31.jpg',
        'https://i.pinimg.com/originals/5b/e2/56/5be25606a1b0a0e951600ec09c4147f1.jpg'
        ]

start_time = time.time()


async def download_image_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = os.path.join('images', f'{url[-10:]}')
            with open(filename, 'wb') as file:
                file.write(await response.read())
                print(f'Файл {url} скачан за {time.time() - start_time:.2f} секунд')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
