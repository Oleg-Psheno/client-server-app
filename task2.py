byte_words = [b'class', b'function', b'method']
for word in byte_words:
    print(f'{word}: тип - {type(word)}, длина - {len(word)}')


"""
Результаты:
    b'class': тип - <class 'bytes'>, длина - 5
    b'function': тип - <class 'bytes'>, длина - 8
    b'method': тип - <class 'bytes'>, длина - 6
"""