from ..gateways import EmailGatewayInterface,MMSGatewayInterface, SMSGatewayInterface, DummyEmailGateway, DummySMSGateway, DummyMMSGateway
class GatewayFactory:
    def __init__():
        # real scenario i think the creds injeted here
        pass
    async def get_email_gateway() -> EmailGatewayInterface:
        return DummyEmailGateway()

    async def get_sms_gateway() -> SMSGatewayInterface:
        return DummySMSGateway()
    
    async def get_mms_gateway() -> MMSGatewayInterface:
        return DummyMMSGateway()