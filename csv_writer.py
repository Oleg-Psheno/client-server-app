import csv
import re


def parse(data, pattern):
    for el in data:
        match = re.findall(pattern, el)
        if match:
            result = el.split(':')[1].lstrip()
            return result


def get_data(file):
    with open(file, 'r', encoding='cp1251') as f:
        info_file = f.read().split('\n')
    return info_file


def write_to_csv(data):
    with open('main.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data[0])
        for i in range(len(data[1:][0])):
            row = [el[i] for el in data[1:]]
            writer.writerow(row)


if __name__ == '__main__':

    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    patterns = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for file in files:
        data = get_data(file)
        os_prod_list.append(parse(data, patterns[0]))
        os_name_list.append(parse(data, patterns[1]))
        os_code_list.append(parse(data, patterns[2]))
        os_type_list.append(parse(data, patterns[3]))

    main_list = [patterns, os_prod_list, os_name_list, os_code_list, os_type_list]
    write_to_csv(main_list)

