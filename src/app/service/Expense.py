from typing import Optional
from langchain_mistralai import ChatMistralAI
from langchain_core.pydantic_v1 import BaseModel, Field


class Expense(BaseModel):
        """Information about a transaction made on any Card"""
        
        amount: Optional[str] = Field(default=None, description="Expense made on the transaction")
        merchant: Optional[str] = Field(default=None, description="Marchant name whom the transaction has been made")
        currency: Optional[str] = Field(default=None, description="currency of the transaction")
    