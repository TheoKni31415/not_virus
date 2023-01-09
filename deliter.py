import os
try:
    with open("C:\\Users\\User\\Desktop\\file_path.txt", "r") as file:
        count = 0
        for i in file.readlines():
            try:
                os.remove(i[:-1])
                print(i[:-1] + " Файл удален")
                count += 1
            except FileNotFoundError:
                print(i[:-1] + " Такого файла нет")

        print(f"Количество удаленных файлов: {count}")
except FileNotFoundError:
    print('У вас нет файла "file_path.txt" на рабочем столе. Вероятно, вы его перенесли или удалили.')
while True:
    print (input())