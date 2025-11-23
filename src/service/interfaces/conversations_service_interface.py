from abc import ABC, abstractmethod
from typing import List, Optional
from ...dtos.dtos import ConversationDTO, CompleteMessageDTO

class ConversationServiceInterface(ABC):


    @abstractmethod
    async def create_conversation(self, convo: ConversationDTO) -> ConversationDTO:
        pass

    @abstractmethod
    async def get_conversation_by_id(self, id:str) -> Optional[ConversationDTO]:
        pass

    @abstractmethod
    async def get_conversation_by_participants(self, person1: str, person2: str) -> ConversationDTO:
        pass

    @abstractmethod
    async def get_conversations_with_user(self, user: str) -> Optional[ConversationDTO]:
        pass
    
    @abstractmethod
    async def get_all_conversations(self) -> List[ConversationDTO]:
        pass
    
    @abstractmethod
    async def get_conversation_messages(self, id:int) ->List[CompleteMessageDTO]:
        pass

    @abstractmethod
    async def delete_conversation(self, convo_id: str):
        pass