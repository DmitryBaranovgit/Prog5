import requests
import time
from xml.etree import ElementTree as ET  
from decimal import Decimal
import matplotlib.pyplot as plt
    
# TODO 1: Исследовать самостоятельно есть ли более оптимальная библиотека для парсинга XML или
# посмотреть есть ли возможность использовать у ЦБ другой API для получения json изначально

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class CurrencyManager(metaclass = SingletonMeta):
    def __init__(self):
        self._last_request_time = 0
        self._cache = {}
    
    def get_currencies(self, currencies_ids_lst: list, refresh_interval: int = 1) -> list:
        current_time = time.time()
        if current_time - self._last_request_time < refresh_interval:
            print("Частый запрос: используются кэшированные данные")
            return self._cache
        
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ET.fromstring(response.content)

        result = []
        for valute in root.findall("Valute"):
            valute_id = valute.get("ID")

            if valute_id in currencies_ids_lst:
                char_code = valute.find("CharCode").text
                name = valute.find("Name").text
                value = valute.find("Value").text.replace(",",".")
                nominal = int(valute.find("Nominal").text)

                decimal_value = Decimal(value)
                int_part, frac_part = str(decimal_value).split(".")

                result.append({char_code: (name, (int_part, frac_part), nominal)})
        self._cache = result
        self._last_request_time = current_time
        return result
    
# valutes = root.findall(
#     "Valute"
# )  # исследовать, есть ли отдельный метод получения валют с опреденным id
# # если да, упростить алгоритм ниже
# for _v in valutes:
#     valute_id = _v.get('ID')
#     valute = {}
#     if (str(valute_id) in currencies_ids_lst):
#         valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find(
#             'Value').text
#         valute_charcode = _v.find('CharCode').text
#         valute[valute_charcode] = (valute_cur_name, valute_cur_val)
#         result.append(valute)
# return result

class CurrenciesLst():

    def __init__(self, currencies_data):
        self.__cur_lst = currencies_data
        # self.__cur_lst = [{
        #     'GBP': ('Фунт стерлингов Соединенного королевства', '113,2069')
        # }, {
        #     'KZT': ('Казахстанских тенге', '19,8264')
        # }, {
        #     'TRY': ('Турецких лир', '33,1224')
        # }]

    def visualize_currencies(self):

        fig, ax = plt.subplots()
        labels = [list(currency.keys())[0] for currency in self.__cur_lst]
        values = [
            float(".".join(currency[list(currency.keys())[0]][1]))
            for currency in self.__cur_lst
        ]

        ax.bar(labels, values, color = 'skyblue')
        ax.set_ylabel('Курсы к рублю')
        ax.set_title('Курсы валют на текущую дату')

        plt.savefig('currencies.jpg')
        plt.show()

def get_currencies(currencies_ids_lst: list) -> list:
    manager = CurrencyManager()
    return manager.get_currencies(currencies_ids_lst)
        
        # currencies = []
        # for el in self.__cur_lst:
        #     currencies.append(str(el.keys()))

        # print(currencies)

        # fruits = ['apple', 'blueberry', 'cherry', 'orange']
        # counts = [40, 100, 30, 55]
        # bar_labels = ['red', 'blue', '_red', 'orange']
        # bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

        # ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

        # ax.set_ylabel('fruit supply')
        # ax.set_title('Fruit supply by kind and color')
        # ax.legend(title='Fruit color')

        # plt.show()

        # обращается к атрибуту __cur_lst, преобразовывать значения курсов валют в нужный формат и выводить эти данные в файл

        # self.__cur_lst


if __name__ == '__main__':

    currency_ids = ['R01035', 'R01335', 'R01700J']
    result = get_currencies(currency_ids)

    if result:
        print("Полученные данные о валютах:", result)

        currencies_list = CurrenciesLst(result)
        currencies_list.visualize_currencies()