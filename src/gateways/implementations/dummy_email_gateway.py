from typing import Optional, List
from ...gateways.interfaces.email_gateway_interface import EmailGatewayInterface
from ...dtos.dtos import MessageDTO

class DummyEmailGateway(EmailGatewayInterface):
    def __init__(self):
        self.client = ""
        pass
    async def authenticate_gateway():
        print("stub authenticate")

    async def send_email_message(self, message: MessageDTO) -> MessageDTO:
        return message
