from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from abc import ABC, abstractmethod
from typing import List, Optional
from src.dtos.dtos import MessageDTO

    
class MessageDAOInterface(ABC):
    @abstractmethod
    async def get_message_by_id(self, id:str) -> Optional[MessageDTO]:
        pass
    @abstractmethod
    async def get_messages_by_conversation(self, conversation_id: int) -> List[MessageDTO]:
        pass
    @abstractmethod
    async def create_message(self, message: MessageDTO):
        pass

