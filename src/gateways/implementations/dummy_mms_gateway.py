from typing import Optional, List
from ...gateways.interfaces.mms_gateway_interface import MMSGatewayInterface
from ...dtos.dtos import MessageDTO

class DummyMMSGateway(MMSGatewayInterface):
    def __init__(self):
        self.client = ""
        pass    
    async def authenticate_gateway():
        print("stub authenticate")
        
    async def send_mms_message(self, message: MessageDTO)-> MessageDTO:
        return message
        
