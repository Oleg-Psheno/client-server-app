with open('test.txt','r') as f:
    data = f.readlines()

print(f)
print(data)

'''
Вручную создал файл test.txt

Результаты:
    <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
    ['сетевое программирование\n', 'сокет\n', 'декоратор']
    
т.к. использую mac кодировка по умолчанию у меня UTF-8
'''