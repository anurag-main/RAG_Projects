from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
text = "Artificial Intelligence (AI) is the branch of computer science that enables machines to think, learn, and act like humans. It allows computers to perform tasks such as recognizing speech, understanding language, solving problems, and making decisions. AI is used in many areas of our daily life — from voice assistants like Siri and Alexa to online shopping recommendations and self-driving cars. It has two main types: Narrow AI, which focuses on specific tasks, and General AI, which aims to mimic human intelligence completely. Through technologies like machine learning and deep learning, AI systems learn from data and improve over time. AI is transforming industries such as healthcare, finance, and education by making processes faster and more accurate. However, it also raises challenges like job loss and privacy concerns. Despite these issues, AI continues to grow rapidly and is becoming a key part of our future, changing the way we live, work, and interact with technology."


loader = PyPDFLoader('Android app flow .pdf')
docs = loader.load()
split = RecursiveCharacterTextSplitter(
  chunk_size=500,
  chunk_overlap=0,
  keep_separator=''
  
)

newText = split.split_text(text)
print(len(newText))
print (newText)