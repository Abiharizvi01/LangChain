from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result=model.invoke('write five line poem on cricket')

print(result)

#this time we will not just get the text output instead we will get some 
#additional information like tokens n all