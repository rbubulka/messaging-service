from typing import Optional, List
from ...service.interfaces.conversations_service_interface import ConversationServiceInterface
from ...dao.interfaces import MessageDAOInterface, ConversationDAOInterface
from ...dtos.dtos import ConversationDTO

class ConversationService(ConversationServiceInterface):
    def __init__(self, c_dao: ConversationDAOInterface, m_dao: MessageDAOInterface):
        self.c_dao = c_dao
        self.m_dao = m_dao
        

    async def get_conversation_messages(self, conversation_id) -> List[ConversationDTO]:
        return await self.m_dao.get_messages_by_conversation(conversation_id)
    
    async def create_conversation(self, convo: ConversationDTO) -> ConversationDTO:
        return await self.c_dao.create_conversation(convo.member_1, convo.member_2)

    async def get_conversation_by_id(self, id:str) -> Optional[ConversationDTO]:
        return await self.c_dao.get_conversation(id)

    async def get_conversation_by_participants(self, person1: str, person2: str) -> ConversationDTO:
        return await self.c_dao.find_conversation(person1, person2)

    async def get_conversations_with_user(self, user: str) -> Optional[ConversationDTO]:
        pass
    
    async def get_all_conversations(self) -> List[ConversationDTO]:
        return await self.c_dao.get_all_conversations()

    async def delete_conversation(self, convo_id: str):
        pass