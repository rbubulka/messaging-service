from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.interfaces.webhook_service_interface import WebhookServiceInterface as service
from ..dtos.dtos import WebhookDTO
from ..database import get_db
from ..factories.service import ServiceFactory
router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])

@router.post("/sms", tags=["webhooks"], response_model=WebhookDTO)
async def put_sms(webhook: WebhookDTO, db: AsyncSession = Depends(get_db)):
    webhook.message_type = "sms"
    web_service = await ServiceFactory(db).get_webhook_service()
    return await web_service.recieve_sms(message=webhook)

@router.post("/mms", tags=["webhooks"], response_model=WebhookDTO)
async def put_mms(webhook: WebhookDTO, db: AsyncSession = Depends(get_db)):
    webhook.message_type = "mms"
    web_service = await ServiceFactory(db).get_webhook_service()
    return await web_service.recieve_mms(message=webhook)

@router.post("/email", tags=["webhooks"], response_model=WebhookDTO)
async def put_sms(webhook: WebhookDTO, db: AsyncSession = Depends(get_db)):
    webhook.message_type = "email"
    web_service = await ServiceFactory(db).get_webhook_service()
    return await web_service.recieve_email(message=webhook)




# Test 6: Simulate incoming Email webhook
# "/api/webhooks/email" \
#   -H "$CONTENT_TYPE" \
#   -d '{
#     "from": "contact@gmail.com",
#     "to": "user@usehatchapp.com",
#     "xillio_id": "message-3",
#     "body": "<html><body>This is an incoming email with <b>HTML</b> content</body></html>",
#     "attachments": ["https://example.com/received-document.pdf"],
#     "timestamp": "2024-11-01T14:00:00Z"
#   }' \
#   -w "\nStatus: %{http_code}\n\n"