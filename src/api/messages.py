from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.interfaces.message_service_interface import MessageServiceInterface as service
from ..dtos.dtos import MessageDTO
from ..database import get_db
from ..factories.service import ServiceFactory

router = APIRouter(prefix="/api/messages", tags=["messages"])

@router.post("/sms", tags=["messages"],  response_model=MessageDTO)
async def put_sms(message: MessageDTO, db: AsyncSession = Depends(get_db)):
    factory = ServiceFactory(db)
    message_service = await factory.get_message_service()
    message.message_type = "sms"
    return await message_service.send_sms_message(message)

@router.post("/mms", tags=["messages"], response_model=MessageDTO)
async def put_mms(message: MessageDTO, db: AsyncSession = Depends(get_db)):
    factory = ServiceFactory(db)
    message_service = await factory.get_message_service()
    message.message_type = "mms"
    return await message_service.send_mms_message(message)

@router.post("/email", tags=["messages"], response_model=MessageDTO)
async def put_sms(message: MessageDTO, db: AsyncSession = Depends(get_db)):
    factory = ServiceFactory(db)
    message_service = await factory.get_message_service()
    message.message_type = "email"
    return await message_service.send_email_message(message)
