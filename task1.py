words = ['разработка', 'сокет', 'декоратор']

for word in words:
    print(f'{word} тип: {type(word)}')

words_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430 ',
                 '\u0441\u043E\u043A\u0435\u0442',
                 '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440']
print('_' * 30)

for word in words_unicode:
    print(f'{word} тип: {type(word)}')

"""
Результаты:

    разработка тип: <class 'str'
    сокет тип: <class 'str'>
    декоратор тип: <class 'str'>
    ______________________________
    разработка  тип: <class 'str'>
    сокет тип: <class 'str'>
    декоратор тип: <class 'str'>
    
Как видим, отображение и тип данных не отличается
"""
