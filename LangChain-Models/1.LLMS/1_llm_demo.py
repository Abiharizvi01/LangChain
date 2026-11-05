from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=openAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke('what is the capital of india')

print(result)

#it will usually return a text output but we have no api in our env file so
#we cant use it it is just a demo code.