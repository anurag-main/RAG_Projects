from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

loader= TextLoader('eassy.txt', encoding='utf-8')

docs = loader.load()

model = ChatOpenAI()
prompt =PromptTemplate(
  template = 'Write a 2 line summury about following {text}',
  input_variables=['text']
)

parser= StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'text' : docs[0].page_content})
print(result)