# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def upword():
    for word in input('Введите строку: ').split():
        tempword = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                tempword += 1
        print(word.title() if tempword == len(word) else f'{word} - етсь недопустимые символы')


upword()
