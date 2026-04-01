# Abstract Repository class for handling database operations
from abc import ABC, abstractmethod
from typing import List, Optional


class BaseRepository(ABC):
    @abstractmethod
    def add(self, item) -> Optional[object]:
        pass

    @abstractmethod
    def get(self, item_id) -> Optional[object]:
        pass

    @abstractmethod
    def update(self, item_id, item) -> Optional[object]:
        pass

    @abstractmethod
    def delete(self, item_id) -> bool:
        pass

    @abstractmethod
    def list(self) -> List[object]:
        pass
