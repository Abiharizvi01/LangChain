from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    provider="featherless-ai",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

#My code reached Hugging Face successfully, but the selected models aren't 
# available through my enabled inference providers. The tutorial's 
# model/provider setup is outdated or different from the current HF setup.
#  I understand the API integration and can move on to the local-model example.