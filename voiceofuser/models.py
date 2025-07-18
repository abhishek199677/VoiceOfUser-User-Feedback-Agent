from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class FeedbackModel(BaseModel):
    user_id: Optional[str] = None
    business_id: str
    rating: int
    comment: str
    metadata: Optional[Dict] = None
    timestamp: datetime = datetime.utcnow()
