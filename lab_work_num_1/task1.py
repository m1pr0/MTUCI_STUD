'''
Напишите программу, которая запрашивает у пользователя ввод числа и
выводит на экран все числа от 1 до введенного числа включительно.
'''


try:
    num = int(input('введите число'))
    for i in range(1, num + 1):
        print(i)
except ValueError:
    print('ой, кажется это не число, попробуйте еще раз!')

