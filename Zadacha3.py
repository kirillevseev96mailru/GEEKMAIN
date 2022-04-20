''' https://drive.google.com/file/d/1Pw_aKVtQVfwL5fxtutrCLn1HF8hGPkJR/view?usp=sharing '''

vuosi = int(input('Введите год: '))
if (vuosi % 4 == 0):
    if (vuosi % 100 == 0):
        if (vuosi % 400 == 0):
            print('Год високосный')
        else:
            print('Год не високосный')
    else:
        print('Год високосный')
else:
    print('Год не високосный')
