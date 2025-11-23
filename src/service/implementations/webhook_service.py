from ...service.interfaces.webhook_service_interface import WebhookServiceInterface
from ...dao.interfaces import MessageDAOInterface, ConversationDAOInterface
from ...dtos.dtos import WebhookDTO, MessageDTO


class WebhookService(WebhookServiceInterface):
    def __init__(self, c_dao: ConversationDAOInterface, m_dao:MessageDAOInterface):
        self.c_dao = c_dao
        self.m_dao = m_dao
    

    async def recieve_sms(self, message: WebhookDTO) -> MessageDTO:
        convo = await self.c_dao.find_conversation(message.sender, message.recipient)
        if convo == None:
            convo = await self.c_dao.create_conversation(message.sender,message.recipient)
        await self.m_dao.create_webhook_message(message, convo.id)
        return message

    async def recieve_mms(self, message: WebhookDTO):
        convo = await self.c_dao.find_conversation(message.sender, message.recipient)
        if convo == None:
            convo = await self.c_dao.create_conversation(message.sender,message.recipient)
        await self.m_dao.create_webhook_message(message, convo.id)
        return message

    async def recieve_email(self, message: WebhookDTO):
        
        convo = await self.c_dao.find_conversation(message.sender, message.recipient)
        if convo == None:
            convo = await self.c_dao.create_conversation(message.sender,message.recipient)
        await self.m_dao.create_webhook_message(message, convo.id)
        return message

