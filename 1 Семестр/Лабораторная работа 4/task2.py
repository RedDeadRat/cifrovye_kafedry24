# TODO импортировать необходимые молули

import csv
import json

SOURCE_FOR_INPUT_FILE = "tests/output.txt"
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

"""def input_data_generator() -> None:
    with open(SOURCE_FOR_INPUT_FILE) as input_file:
        contents = json.load(input_file)
        headers = list(contents[0].keys())
        raw_data = []
        for i in range(len(contents)):
            raw_data.append(list(contents[i].values()))
    with open(INPUT_FILENAME, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)                    #Запись заголовков
        writer.writerows(raw_data)                  #Запись остальных данных"""

def task() -> None:
    #input_data_generator()                          #Мой input.csv был пустым, так исправим же это
    with open(INPUT_FILENAME) as input_file:  # TODO считать содержимое csv файла
        reader = csv.DictReader(input_file)
        data = list(reader)
        with open(OUTPUT_FILENAME, "w") as output_file:
            json.dump(data, output_file, indent=4)  # TODO Сериализовать в файл с отступами равными 4



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

