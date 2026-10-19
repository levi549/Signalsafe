from langchain.agents import create_agent
from langchain.tools import tools
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

client=genai.Client(api_key=os.getenv("AI_URL"))


class AI():
    def __init__(self):
        self.modelo=ChatOpenAI( model="gemini-2.5-flash",
                                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                                api_key=os.getenv("AI_URL")
                            )
        self.system_prompt=""
        self.tools=[]
        self.agent=create_agent(model=self.modelo,tools=self.tools,system_prompt=self.system_prompt)

    def inferência():
        pass