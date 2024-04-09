# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.


import os
import multiprocessing


def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Файл {file_path}: {word_count} слов")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")


def process_directory(directory_path_):
    for root, _, files in os.walk(directory_path_):
        for file in files:
            file_path = os.path.join(root, file)
            process = multiprocessing.Process(target=count_words_in_file, args=(file_path,))
            process.start()
            process.join()


if __name__ == '__main__':
    directory_path = "dir_for_task"
    process_directory(directory_path)
