from  sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_ , or_
from typing import List, Optional
from ...dtos.dtos import ConversationDTO
from ...dao.interfaces import ConversationDAOInterface
from ...dtos.db_models import Conversation
class ConversationDAO(ConversationDAOInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_conversation(self, m_1: str, m_2:str) -> ConversationDTO:
        new_convo_obj = Conversation(member_1 = m_1, member_2 = m_2)
        self.session.add(new_convo_obj)
        await self.session.commit()
        await self.session.refresh(new_convo_obj)
        return ConversationDTO(id = new_convo_obj.id, member_1 = new_convo_obj.member_1, member_2 = new_convo_obj.member_2)


    async def find_conversation(self, user1: str, user2: str) -> Optional[ConversationDTO]:
        result = await self.session.execute(
            select(Conversation.id,Conversation.member_1,Conversation.member_2).where(or_(
                and_((Conversation.member_1 == user1),(Conversation.member_2 == user2)),
                and_((Conversation.member_1 == user2),(Conversation.member_2 == user1))
                )))
        top_res = result.first()
        if top_res == None:
            return None
        return ConversationDTO(id= top_res.id, member_1 = top_res.member_1, member_2 = top_res.member_2)
    
    async def find_user_conversations(self, user_1: str) -> Optional[ConversationDTO]:
        convos = await self.session.execute(
            select(Conversation).where((Conversation.member_1 == user_1)|(Conversation.member_2 == user_2))
        )
        result = []
        for c in convos:
            result.append(ConversationDTO(id= c.id, member_1 = c.member_1, member_2 = c.member_2))    
        return result



    async def get_conversation(self, c_id: int) -> Optional[ConversationDTO]:
        result = await self.session.execute(
            select(Conversation).where(Conversation.id == c_id)
        )
        if not result.scalar_one_or_none:
            return None
        return ConversationDTO(id= result.id, member_1 = result.member_1, member_2 = result.member_2)

    async def delete_conversation(self, convo_id:str):
        pass
    
    async def get_all_conversations(self) -> List[ConversationDTO]:
        convos = await self.session.execute(select(Conversation.id, Conversation.member_1, Conversation.member_2))
        result = []
        for c in convos.all():
            result.append(ConversationDTO(id= c[0], member_1 = c[1], member_2 = c[2]))
        return result