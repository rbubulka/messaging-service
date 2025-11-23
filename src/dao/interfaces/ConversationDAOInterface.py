from abc import ABC, abstractmethod
from typing import List, Optional
from src.dtos.dtos import ConversationDTO
class ConversationDAOInterface(ABC):

    @abstractmethod
    async def create_conversation(self, convo: ConversationDTO) -> ConversationDTO:
        pass

    @abstractmethod
    async def find_conversation(self, user1: str, user2: str) -> Optional[ConversationDTO]:
        pass

    @abstractmethod
    async def get_conversation(self, id:int)-> Optional[ConversationDTO]:
        pass

    @abstractmethod
    async def delete_conversation(self, convo_id: str):
        pass
    
    @abstractmethod
    async def get_all_conversations(self) -> List[ConversationDTO]:
        pass