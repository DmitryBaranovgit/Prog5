import requests
import json
import csv
from xml.etree import ElementTree as ET
from decimal import Decimal
from io import StringIO

class Component:
    """
    Базовый интерфейс компонента, который определяет поведение для декораторов.
    """
    def operation(self) -> dict:
        pass

class CurrenciesList(Component):
    """
    Класс CurrenciesList возвращает данные о курсах валют в формате словаря.
    """
    def operation(self) -> dict:
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ET.fromstring(response.content)

        currencies_data = {}
        for valute in root.findall("Valute"):
            char_code = valute.find("CharCode").text
            name = valute.find("Name").text
            value = valute.find("Value").text.replace(",",".")
            nominal = int(valute.find("Nominal").text)
            decimal_value = Decimal(value)
            int_part, frac_part = str(decimal_value).split(".")
            currencies_data[char_code] = (name, (int_part, frac_part), nominal)
        
        return currencies_data

class Decorator(Component):
    """
    Базовый класс Декоратора, который принимает компонент и делегирует ему работу.
    """
    def __init__(self, component: Component) -> None:
        self._component = component
    
    def operation(self) -> dict:
        return self._component.operation()
    
class ConcreteDecoratorJSON(Decorator):
    """
    Конкретный декоратор для вывода данных в формате JSON.
    """
    def operation(self) -> str:
        data = self._component.operation()
        return json.dumps(data, ensure_ascii = False, indent = 4)
    
class ConcreteDecoratorCSV(Decorator):
    """
    Конкретный декоратор для вывода данных в формате CSV.
    """
    def operation(self) -> str:
        data = self._component.operation()
        if isinstance(data, str):
            data = json.loads(data)
            
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Код валюты", "Название", "Целая часть", "Дробная часть", "Номинал"])

        for char_code, (name, (int_part, frac_part), nominal) in data.items():
            writer.writerow([char_code, name, int_part, frac_part, nominal])

        return output.getvalue()
    
def client_code(component: Component) -> None:
    """
    Клиентаский код работает с компонентом через общий интерфейс, не зависимо от конкретно класса.
    """
    print("Результат:")
    print(component.operation())

# Пример использования
if __name__ == "__main__":
    # Создаем базовй компонент
    simple_currencies = CurrenciesList()

    print("Базовый компонент (словарь):")
    client_code(simple_currencies)
    print("\n")

    # Используем декоратор JSON
    decorated_json = ConcreteDecoratorJSON(simple_currencies)
    print("Декоративный компонет (JSON):")
    client_code(decorated_json)
    print("\n")

    # Используем декоратор CSV
    decorated_csv = ConcreteDecoratorCSV(simple_currencies)
    print("Декорирующий компонент (CSV):")
    client_code(decorated_csv)
    print("\n")

    # Декорирование декоратора JSON с помощтю CSV
    print("Декорированный компонент (JSON + CSV):")
    decorated_json_csv = ConcreteDecoratorCSV(decorated_json)
    client_code(decorated_json_csv)