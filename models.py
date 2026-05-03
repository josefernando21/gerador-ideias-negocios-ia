from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

Base = declarative_base()

class Idea(Base):
    __tablename__ = "ideas"
    
    id = Column(Integer, primary_key=True, index=True)
    niche = Column(String, nullable=False)
    market = Column(String, nullable=False)
    budget = Column(String, nullable=False)
    generated_ideas = Column(Text, nullable=False)  # JSON string
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Pydantic schemas
class IdeaCreate(BaseModel):
    niche: str
    market: str
    budget: str

class IdeaResponse(BaseModel):
    id: int
    niche: str
    market: str
    budget: str
    generated_ideas: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class GenerateRequest(BaseModel):
    niche: str
    market: str
    budget: str

class GenerateResponse(BaseModel):
    ideas: List[Dict[str, Any]]
    swot: Dict[str, str]

