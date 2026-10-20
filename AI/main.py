from langchain.agents import create_agent
from langchain.tools import tools
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.mcp import MCPAdapter
load_dotenv()

class AI():
    def __init__(self):
        self.modelo=ChatOpenAI( model="gemini-2.5-flash",
                                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                                api_key=os.getenv("AI_URL")
                            )
        self.system_prompt=""
        self.tools=Get_tools()
        self.agent=create_agent(model=self.modelo,tools=self.tools,system_prompt=self.system_prompt)
        self.memory=[]


    async def Get_tools(): 
        async with MCPAdapter("http://localhost:3000") as adapter:
            self.tools=await adapter.list_tools()


    def inferência():
        pass

