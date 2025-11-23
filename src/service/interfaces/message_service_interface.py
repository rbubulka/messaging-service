from abc import ABC, abstractmethod
from typing import List, Optional
from ...dtos.dtos import MessageDTO
class MessageServiceInterface(ABC):
    @abstractmethod
    async def send_sms_message(self, message: MessageDTO) -> MessageDTO:
        pass
    @abstractmethod
    async def send_mms_message(self, message: MessageDTO) -> MessageDTO:
        pass
    @abstractmethod
    async def send_email_message(self, message: MessageDTO) -> MessageDTO:
        pass