from pydantic import BaseModel, Field, ConfigDict
from typing import Any, Optional
import datetime

class MessageDTO(BaseModel):
    sender: str = Field(alias='from')
    recipient: str = Field(alias='to')
    message_type: Optional[str] = None
    body: str
    attachments: Optional[list[str]] = None
    timestamp: datetime.datetime
    model_config = ConfigDict(
        extra='allow',
    )
    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        data = super().model_dump(**kwargs)
        return data

class CompleteMessageDTO(BaseModel):
    id: int
    sender: str
    recipient: str
    message_type: str
    messaging_provider_id: Optional[str] = None
    body: Optional[str] = None
    attachments: Optional[list[str]] = None
    conversation_id: int
    timestamp: datetime.datetime

    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        data = super().model_dump(**kwargs)
        return data

class ConversationDTO(BaseModel):
    id: int
    member_1: str
    member_2: str
    
    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        data = super().model_dump(**kwargs)
        return data

class WebhookDTO(BaseModel):
    sender: str = Field(alias='from')
    recipient: str = Field(alias='to')
    message_type: Optional[str] = Field(default = None, alias='type')
    messaging_provider_id: Optional[str] = Field(default = None, alias="xillio_id")
    body: str
    attachments: Optional[list[str]] = None
    timestamp: datetime.datetime
    model_config = ConfigDict(
        extra='allow',
    )
    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        data = super().model_dump(**kwargs)
        return data
