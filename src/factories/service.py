from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from ..dao import ConversationDAO, ConversationDAOInterface, MessageDAO, MessageDAOInterface
from ..service import ConversationService, ConversationServiceInterface, MessageService, MessageServiceInterface, WebhookService, WebhookServiceInterface
from .gateway import GatewayFactory

class ServiceFactory:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.message_dao = MessageDAO(db)
        self.conversation_dao = ConversationDAO(db)

    async def get_message_service(self) -> MessageServiceInterface:
        e =  await GatewayFactory.get_email_gateway()
        m = await GatewayFactory.get_mms_gateway()
        s = await GatewayFactory.get_sms_gateway()
        return MessageService(
                        m_dao= self.message_dao, 
                        c_dao = self.conversation_dao, 
                        e_gate = e, 
                        m_gate = m,
                        s_gate = s)

    async def get_conversation_service(self) -> ConversationServiceInterface:
        return ConversationService(c_dao = self.conversation_dao, m_dao = self.message_dao)
    
    async def get_webhook_service(self) -> WebhookServiceInterface:
        return WebhookService(c_dao = self.conversation_dao, m_dao = self.message_dao)

