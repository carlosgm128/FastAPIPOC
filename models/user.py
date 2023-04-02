from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any, AnyStr, Text


class User(BaseModel):
    id: str
    username: str
    first_name: str
    last_name: str
    is_active: bool = True
    last_login: datetime = datetime.now
    created_at: datetime = datetime.now()
    dob: Optional[datetime]

