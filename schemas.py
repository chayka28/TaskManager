from pydantic import BaseModel, field_validator 
from typing import Literal

class STaskAdd(BaseModel):

    title: str
    description: str | None = None
    status: Literal["new", "in_progress", "done"]

    @field_validator("status", mode="before")
    @classmethod
    def valid_status(cls, v: str) -> str:
        if isinstance(v, str):
            return v.strip().lower()
        return v
    
class TaskResponse(STaskAdd):
    id: int