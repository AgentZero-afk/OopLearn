from abc import ABC, abstractmethod
from _datetime import *

class Handler(ABC):
    @abstractmethod
    def emit(self,message:str):
        pass

class ConsoleHandler(Handler):
    def emit(self,message:str):
        print(message)

class FileHandler(Handler):
    def emit(self,message:str):
        return f'Запись в файл: {message}'

class TimeMixin:
    def format_with_timestamp(self, message: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'[{timestamp}] [{message}]'


class Logger(TimeMixin):
    def __init__(self,handlers:list):
        self._handlers = handlers

    def log(self,message:str):
        message = self.format_with_timestamp(message)
        for handler in self._handlers:
            handler.emit(message)

    def __call__(self, message:str):
        self.log(message)

