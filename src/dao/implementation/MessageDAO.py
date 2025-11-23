from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ...dao.interfaces import MessageDAOInterface
from ...dtos.dtos import MessageDTO, WebhookDTO, CompleteMessageDTO
from ...dtos.db_models import Message
    
class MessageDAO(MessageDAOInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_message_by_id(self, id:int) -> Optional[MessageDTO]:
        result = await self.session.execeute(
            select(Message).where(Message.id == id)
        )
        if not result.scalar_one_or_none():
            return None
        
        return MessageDTO(
                    sender= result.sent_by, 
                    recipient=result.recieved_by,
                    message_type=result.message_type,
                    body=result.body,
                    attachment=result.attachment,
                    timestamp = result.date_sent)

    async def get_messages_by_conversation(self, c_id: int) -> List[CompleteMessageDTO]:
        result  = await self.session.execute(
            select(Message).where(Message.conversation_id == c_id))
        result_list = []
        for res in result.all():
            result_list.append(
                CompleteMessageDTO(
                    id = res[0].id,
                    sender= res[0].sent_by, 
                    recipient=res[0].recieved_by,
                    message_type=res[0].message_type,
                    messaging_provider_id = res[0].provider,
                    body=res[0].body,
                    attachment=res[0].attachment,
                    conversation_id=c_id,
                    timestamp = res[0].date_sent)
            )     
        return result_list
    
    async def create_message(self, new_message: MessageDTO, c_id: int):
        if new_message.attachments == None:
            self.session.add( Message(
                sent_by= new_message.sender,
                recieved_by = new_message.recipient,
                conversation_id = c_id,
                date_sent = new_message.timestamp,
                body = new_message.body,
                message_type = new_message.message_type
            ))
        else:
            message_list = []
            for attach in new_message.attachments:
                message_list.append(Message(
                sent_by= new_message.sender,
                recieved_by = new_message.recipient,
                conversation_id = c_id,
                date_sent = new_message.timestamp,
                body = new_message.body,
                message_type = new_message.message_type,
                attachment = attach))
            self.session.add_all(message_list)

        await self.session.commit()
        return new_message

    async def create_webhook_message(self, new_message: WebhookDTO, c_id: int):
        if new_message.attachments == None:
            self.session.add( Message(
                sent_by= new_message.sender,
                recieved_by = new_message.recipient,
                conversation_id = c_id,
                date_sent = new_message.timestamp,
                body = new_message.body,
                message_type = new_message.message_type,
                provider = new_message.messaging_provider_id
            ))
        else:
            message_list = []
            for attach in new_message.attachments:
                message_list.append(Message(
                sent_by= new_message.sender,
                recieved_by = new_message.recipient,
                conversation_id = c_id,
                date_sent = new_message.timestamp,
                body = new_message.body,
                message_type = new_message.message_type,
                attachment = attach,
                provider = new_message.messaging_provider_id))
            self.session.add_all(message_list)
        await self.session.commit()
        return new_message

