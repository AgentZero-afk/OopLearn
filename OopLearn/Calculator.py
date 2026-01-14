

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

    def ask_precision(self) -> int:
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

    def format_result(self, value: float, precision: int) -> str:
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
        else:
            print('Неверный выбор опции')
            return

        formatted = self.format_result(result, precision)
        print(f"{action} числа {self.num_1} и {self.num_2} \nРезультат: {formatted}")






x = input('Введите первое число: ')

y = input('Введите второе число: ')

c = input('Выберите опцию: 1 - сложение, 2 - вычитание , 3 - умножение, 4 - деление: ')


calc = Calculator(float(x),float(y),c)
calc.mod()
input('Программа завершена, нажмите Enter для выхода из терминала...')
