import tornado.ioloop
import tornado.web
import tornado.websocket
import requests
import json
import time

class CurrencyRateFetcher:
    """ 
    Класс для получения и отслеживания курсов валют
    """
    def __init__(self):
        self.observers = []
        self.current_rates = {}

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.write_message(json.dumps(self.current_rates))
        
    def fetch_currency_rates(self):
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        if response.status_code == 200:
            data = response.json()
            self.current_rates = {
                "USD": data["Valute"]["USD"]["Value"],
                "EUR": data["Valute"]["EUR"]["Value"],
                "GBP": data["Valute"]["GBP"]["Value"]
            }
            self.notify_observers()

class CurrencyRateHandler(tornado.websocket.WebSocketHandler):
    """
    Обработчик WebSocket соединений
    """
    def open(self):
        self.application.currency_fetcher.add_observer(self)
        print("Новое подключение наблюдателя")

    def on_close(self):
        self.application.currency_fetcher.remove_observer(self)
        print("Наблюдатель отключился")

class MainHandler(tornado.web.RequestHandler):
    """
    Главная страница с отображением идентификатора клиента
    """
    def get(self):
        self.render("index.html", client_id = id(self))

class Application(tornado.web.Application):
    """
    Приложение Tornado
    """
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/ws", CurrencyRateHandler)
        ]
        super().__init__(handlers)
        self.currency_fetcher = CurrencyRateFetcher()
        self.scheduler = tornado.ioloop.PeriodicCallback(self.update_rates, 10000)
        self.scheduler.start()

    def update_rates(self):
        self.currency_fetcher.fetch_currency_rates()

if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()