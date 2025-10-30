from langchain.tools import BaseTool 
from pydantic import BaseModel, Field
from typing import Type 

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")