from abc import ABC, abstractmethod
from typing import List, Optional
from ...dtos.dtos import MessageDTO
class EmailGatewayInterface(ABC):

    @abstractmethod
    async def authenticate_gateway():
        pass
    @abstractmethod
    async def send_email_message(self, message: MessageDTO) -> MessageDTO:
        pass