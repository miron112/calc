while True:
    BUTE = input('введите количество байтов: ')
    try:
        BUTE_BUTE = int(BUTE)
        break
    except:
        if BUTE.isalpha():
            print("Введены буквы")
        else:
            print("Введены непонятные символы")
i = 1
while i == 1:
    TIPE = input('введите до каких значений преобразовать пример: КБ МБ ГБ ТБ ПБ ЙОБ ')
    try:
        if TIPE == ('КБ'):
            RESULT = BUTE_BUTE/1024
            print('в килобайтах это', RESULT)
            break
        if TIPE == ('МБ'):
            RESULT = BUTE_BUTE/1024
            RESULT1 = RESULT/1024
            print('в килобайтах это', RESULT)
            print('в мегабайтах это', RESULT1)
            break
        if TIPE == ('ГБ'):
            RESULT = BUTE_BUTE/1024
            RESULT1 = RESULT/1024
            RESULT2 = RESULT1/1024
            print('в килобайтах это', RESULT)
            print('в мегабайтах это', RESULT1)
            print('в гигабайтах это', RESULT2)
            break
        if TIPE == ('ТБ'):
            RESULT = BUTE_BUTE/1024
            RESULT1 = RESULT/1024
            RESULT2 = RESULT1/1024
            RESULT3 = RESULT2/1024
            print('в килобайтах это', RESULT)
            print('в мегабайтах это', RESULT1)
            print('в гигабайтах это', RESULT2)
            print('в терабайтах это', RESULT3)
            break
        if TIPE == ('ПБ'):
            RESULT = BUTE_BUTE/1024
            RESULT1 = RESULT/1024
            RESULT2 = RESULT1/1024
            RESULT3 = RESULT2/1024
            RESULT4 = RESULT3/1024
            print('в килобайтах это', RESULT)
            print('в мегабайтах это', RESULT1)
            print('в гигабайтах это', RESULT2)
            print('в терабайтах это', RESULT3)
            print('в петабайтах это', RESULT4)
            break
        if TIPE == ('ЙОБ'):
            RESULT = BUTE_BUTE/1024
            RESULT1 = RESULT/1024
            RESULT2 = RESULT1/1024
            RESULT3 = RESULT2/1024
            RESULT4 = RESULT3/1024
            RESULT5 = RESULT4/1024
            print('в килобайтах это', RESULT)
            print('в мегабайтах это', RESULT1)
            print('в гигабайтах это', RESULT2)
            print('в терабайтах это', RESULT3)
            print('в петабайтах это', RESULT4)
            print('в йотобайтах это', RESULT5)
            break
        else:
            print("введены не коректные данные")
    except:
        break