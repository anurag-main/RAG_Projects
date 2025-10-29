from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate 
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

video_id ="quVbERB8XFY" 

try:
    fetched_transcript = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
    transcript_list = fetched_transcript.to_raw_data()
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    # print(transcript)
    
except TranscriptsDisabled:
    print("No captions available for this video.")
except Exception as e:
    print(f"An error occurred: {e}")
    
splitter = RecursiveCharacterTextSplitter(
   chunk_size =1000,
   chunk_overlap=200
)

chunks = splitter.create_documents([transcript])

# print(len(chunks))
# print(chunks[5])

embeddings= OpenAIEmbeddings(model='text-embedding-3-small')
vector_store =Chroma.from_documents(chunks,embeddings)

# print(vector_store.get(include=['embeddings']))

retriever = vector_store.as_retriever(
    search_type="mmr",                  
    search_kwargs={"k": 3, "lambda_mult": 0.5}  
)

# print(retriever)

# print(retriever.invoke('what is deepmind'))


question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriever.invoke(question)

# print(retrieved_docs)

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain=RunnableParallel({
  'context': retriever | RunnableLambda(format_docs),
  'question': RunnablePassthrough()
})

# print(parallel_chain.invoke('who is deepmind'))

llm= ChatOpenAI(model='gpt-4o-mini',temperature=0.2)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

parser = StrOutputParser()

final_chain= parallel_chain | prompt | llm | parser

result = final_chain.invoke('Where is crow sitting and what he is doing')

print (result)