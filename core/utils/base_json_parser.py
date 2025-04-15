from abc import ABC, abstractmethod

class JsonParser(ABC):
    @abstractmethod
    def parse_notion_data(self, data):
        pass