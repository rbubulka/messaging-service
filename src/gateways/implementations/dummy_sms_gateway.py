from typing import Optional, List
from ...gateways.interfaces.sms_gateway_interface import SMSGatewayInterface
from ...dtos.dtos import MessageDTO

class DummySMSGateway(SMSGatewayInterface):
    def __init__(self):
        self.character_limit = 160
        pass    
    
    async def authenticate_gateway():
        print("stub authetnicate")
    
    async def send_sms_message(self, message: MessageDTO) -> MessageDTO:
        return message