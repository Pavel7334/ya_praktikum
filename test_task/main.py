import datetime as dt


class Record:  # Между классом и конструктором класса должен быть отступ
    def __init__(self, amount, comment, date=''):  # Можно добавить аннотации для аргументов
        self.amount = amount
        self.date = (  # Получение date лучше вынести в отдельный метод
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment  # Атрибут comment должен быть приватным так как он не используется вне класса


class Calculator:   # Между классом и конструктором класса должен быть отступ
    def __init__(self, limit):  # Можно добавить аннотации для аргументов
        self.limit = limit
        self.records = []  # Атрибут records должен быть приватным так как он не используется вне класса
                           # Можно добавить аннотацию для records

    def add_record(self, record):     # Нужно добавить для всех методов Docstrings
        self.records.append(record)   # Docstring Conventions: начинаются с большой буквы,
                                      # заканчиваются точкой и содержат описание того, что делает функция

    def get_today_stats(self):
        today_stats = 0
        for Record in self.records:  # Название переменной должно быть с маленькой буквы
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount  # Можно сократить today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and  # Можно сократить if (today - record.date).days in range(7):
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        # Переменные должны быть названы в соответствии с их смыслом,
        # по-английски, не должно быть однобуквенных названий и транслита.
        # В названии переменной не должен содержаться её тип.
        # При необходимости применяются type annotations.
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \ 
                   f' ещё, но с общей калорийностью не более {x} кКал' # Для переноса вместо бэкслэша используй скобки
        else:  # else тут не нужен так как есть Guard Block в виде return
            return('Хватит есть!') # Здесь скобки не нужны


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE): # Не надо передавать атрибуты класса
        currency_type = currency                                         # В аргументы метода. Можно использовать
        cash_remained = self.limit - self.get_today_stats()              # self.USD_RATE и self.EURO_RATE
        if currency == 'usd':  # вместо простыни из if'оф лучше создать словарь {'usd': 'USD'}
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00  # Должен быть знак присвоения вместо знака сравнения
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '  # В f строках не желательно делать расчёты
                f'{currency_type}'
            )
        elif cash_remained == 0:  # Можно обойтись только if'ом так как есть Guard Block в виде return
            return 'Денег нет, держись'
        elif cash_remained < 0:  # Можно обойтись только if'ом так как есть Guard Block в виде return
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,  # Вместо format можно использовать f строки
                                                     currency_type)  # Бэкслэши для переносов не применяются.

    def get_week_stats(self):  # Этот метод не надо переопределять так как ничего не добавилось
        super().get_week_stats()

    # Исполняемый код в .py-файлах должен быть закрыт конструкцией if __name__ == '__main__'
