import time
import requests
import os
import threading

urls = ['https://rare-gallery.com/uploads/posts/795837-Cats-Eyes-Glance-Whiskers-Snout-Nose.jpg',
        'https://wallbox.ru/wallpapers/main/201546/13dcd7162ea7a31.jpg',
        'https://i.pinimg.com/originals/5b/e2/56/5be25606a1b0a0e951600ec09c4147f1.jpg'
        ]

start_time = time.time()


def download_image(url):
    response = requests.get(url)
    filename = os.path.join('images', f'{url[-10:]}')
    with open(filename, 'wb') as file:
        file.write(response.content)
        print(f'Файл {url} скачан за {time.time() - start_time:.2f} секунд')


threads = []
for url in urls:
    t = threading.Thread(target=download_image, args=(url,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
