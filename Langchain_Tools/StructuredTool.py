from langchain_core.tools import StructuredTool
from pydantic import BaseModel , Field

class MultiplyInput(BaseModel):
  a: int= Field(required=True , description="The first number to add"),
  b: int =Field(required=True,description="The second number to add")


def mutiply(a:int ,b:int)-> int :
  return a*b

mutiply_tool =StructuredTool(
  func=mutiply,
  name='multiply',
  description='Mutiply two numbers',
  args_schema=MultiplyInput
)

result =mutiply_tool.invoke({'a': 10,'b':4})
print(result)