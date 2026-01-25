import math
import requests
import os
import subprocess
import sys


# # Автообновления ----------------------------------------------
#
#
# with open("version.txt") as f:
#     current_version = f.read().strip()
#
#
# def get_latest_release(user, repo):
#     url = f"https://api.github.com/repos/{user}/{repo}/releases/latest"
#     r = requests.get(url)
#     r.raise_for_status()
#     data = r.json()
#     version = data["tag_name"]                      # пример: "v1.1.0"
#     download_url = data["assets"][0]["browser_download_url"]
#     return version, download_url
#
#
# def check_for_update():
#     try:
#         latest_version, url = get_latest_release("AgentZero-afk", "oop-learn")
#         if latest_version != current_version:
#             print(f"Доступна новая версия: {latest_version}")
#             r = requests.get(url)
#             with open("update.exe", "wb") as f:
#                 f.write(r.content)
#             # Запускаем updater
#             subprocess.Popen([os.path.join(os.getcwd(), "updater.exe"), "update.exe", sys.argv[0]])
#             print("Программа будет обновлена и перезапущена.")
#             sys.exit()
#     except Exception as e:
#         print("Не удалось проверить обновление:", e)
#
# check_for_update()



# Основной код для работы калькулятора
class Calculator:
    def __init__(self,num_1,num_2,num_3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

    def add(self):
        return self.num_1 + self.num_2

    def sub(self):
        return self.num_1 - self.num_2


    def mul(self):
        return self.num_1 * self.num_2


    def div(self):
        return self.num_1 / self.num_2

    def exponentiation(self):
        return math.pow(self.num_1, self.num_2)


    @staticmethod
    def ask_precision() -> int:
        raw = input("Сколько знаков после запятой оставить? (0..10, по умолчанию 2): ")
        if raw == "":
            return 2
        try:
            n = int(raw)
            if n < 0:
                print("Введено отрицательное число, использую 2")
                return 2
            if n > 10:
                print("Слишком много знаков, ограничиваю до 10")
                return 10
            return n
        except ValueError:
            print("Некорректный ввод, использую 2")
            return 2

    @staticmethod
    def format_result(value: float, precision: int) -> str:
        fmt = f"{{:.{precision}f}}"
        return fmt.format(value)

    def mod(self):
        precision = self.ask_precision()
        if self.num_3 == '1':
            result = self.add()
            action = 'Складываем'
        elif self.num_3 == '2':
            result = self.sub()
            action = 'Вычитаем'
        elif self.num_3 == '3':
            result = self.mul()
            action = 'Умножаем'
        elif self.num_3 == '4':
            if self.num_2 == 0:
                print('Деление на ноль невозможно')
                return
            result = self.div()
            action = 'Делим'
        elif self.num_3 == '5':
            result = self.exponentiation()
            action = 'Возведение в степень'
        else:
            print('Неверный выбор опции')
            return

        formatted = self.format_result(result, precision)
        print(f"{action} числа {self.num_1} и {self.num_2} \nРезультат: {formatted}")






x = input('Введите первое число: ')

y = input('Введите второе число: ')

c = input('Выберите опцию: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление:, 5 - возведение в степень: ')


calc = Calculator(float(x),float(y),c)
calc.mod()
input('Программа завершена, нажмите Enter для выхода из терминала...')



