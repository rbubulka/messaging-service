from ...service.interfaces.message_service_interface import MessageServiceInterface
from ...dao.interfaces import MessageDAOInterface, ConversationDAOInterface
from ...dtos.dtos import MessageDTO
from ...gateways import EmailGatewayInterface,MMSGatewayInterface, SMSGatewayInterface

class MessageService(MessageServiceInterface):
    def __init__(self, m_dao: MessageDAOInterface, c_dao: ConversationDAOInterface, e_gate: EmailGatewayInterface,m_gate: MMSGatewayInterface,s_gate:SMSGatewayInterface):
        self.m_dao = m_dao
        self.c_dao = c_dao
        self.e_gate = e_gate
        self.m_gate = m_gate
        self.s_gate = s_gate
        

    async def send_sms_message(self, message: MessageDTO) -> MessageDTO:
        convo = await self.c_dao.find_conversation(message.sender, message.recipient)
        await self.s_gate.send_sms_message(message)
        if convo == None:
            convo = await self.c_dao.create_conversation(message.sender,message.recipient)
        await self.m_dao.create_message(message, convo.id)
        return message

    async def send_mms_message(self, message: MessageDTO) -> MessageDTO:
        convo = await self.c_dao.find_conversation(message.sender, message.recipient)
        await self.m_gate.send_mms_message(message)
        if convo == None:
            convo = await self.c_dao.create_conversation(message.sender,message.recipient)
        await self.m_dao.create_message(message, convo.id)
        return message

    async def send_email_message(self, message: MessageDTO) -> MessageDTO:
        convo = await self.c_dao.find_conversation(message.sender, message.recipient)
        await self.e_gate.send_email_message(message)
        if convo == None:
            convo = await self.c_dao.create_conversation(message.sender,message.recipient)
        await self.m_dao.create_message(message, convo.id)
        return message