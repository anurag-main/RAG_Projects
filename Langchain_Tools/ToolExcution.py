from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

load_dotenv()

# Tool Creation 
@tool
def multiply (a:int , b:int) -> int :
  """"Mutilply two numbers"""
  return a*b


# Tool binding with LLM 

llm = ChatOpenAI()

LLM_tool = llm.bind_tools([multiply])

query =HumanMessage('multiply 3 with 2')
messages = [query]
# Tool calling 

result =LLM_tool.invoke('multiply 3 with 4')
messages.append(result)

# Tool Exection 

# print(result.tool_calls[0]['args'])

multiply_result = multiply.invoke(result.tool_calls[0])
messages.append(multiply_result)

final_result =LLM_tool.invoke(messages).content
print(final_result)