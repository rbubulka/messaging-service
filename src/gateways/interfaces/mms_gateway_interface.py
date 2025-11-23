from abc import ABC, abstractmethod
from typing import List, Optional
from ...dtos.dtos import MessageDTO
class MMSGatewayInterface(ABC):
    @abstractmethod
    async def authenticate_gateway():
        # this is probably more to the effect of generatin the client injecting the credentials
        pass
    @abstractmethod
    async def send_mms_message(self, message: MessageDTO) -> MessageDTO:
        pass