from typing import List, Optional
from fastapi import APIRouter, Depends
from ..service.interfaces.conversations_service_interface import ConversationServiceInterface as service
from sqlalchemy.ext.asyncio import AsyncSession
from ..dtos.dtos import ConversationDTO, CompleteMessageDTO
from ..database import get_db
from ..factories.service import ServiceFactory

router = APIRouter(prefix="/api/conversations")

@router.get("", tags=["conversations"], response_model=List[ConversationDTO])
async def get_conversations(db: AsyncSession = Depends(get_db)):
    conversation_service = await ServiceFactory(db).get_conversation_service()
    return await conversation_service.get_all_conversations()

@router.get("/{id}/messages", tags=["conversations"], response_model=List[CompleteMessageDTO])
async def get_conversation_messages(id: int, db: AsyncSession = Depends(get_db)):
    factory = ServiceFactory(db)
    conversation_service = await factory.get_conversation_service()
    return await conversation_service.get_conversation_messages(id)
