from abc import ABC, abstractmethod
from typing import List, Optional
from ...dtos.dtos import WebhookDTO, MessageDTO

class WebhookServiceInterface(ABC):
    @abstractmethod
    async def recieve_sms(self, message: WebhookDTO)->MessageDTO:
        pass
    
    @abstractmethod
    async def recieve_mms(self, message: WebhookDTO)->MessageDTO:
        pass

    @abstractmethod
    async def recieve_email(self, message: WebhookDTO)->MessageDTO:
       pass