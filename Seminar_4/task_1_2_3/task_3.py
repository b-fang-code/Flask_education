# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.


import os
import asyncio


async def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 0


async def process_directory(directory_path):
    files = os.listdir(directory_path)
    tasks = []
    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            tasks.append(count_words_in_file(file_path))

    results = await asyncio.gather(*tasks)
    for i, file in enumerate(files):
        print(f"Файл: {file}, Количество слов: {results[i]}")


if __name__ == '__main__':
    directory_path_ = "dir_for_task"
    asyncio.run(process_directory(directory_path_))
