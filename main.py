from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain_tavily import TavilySearch
load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")
    title: str = Field(description="The title of the source")
    description: str = Field(description="The description of the source")
    content: str = Field(description="The content of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm = ChatOllama(model="gemma4:e2b", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)


def main():
    print("Hello from langchain-course-p!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"
            )
        }
    )
    print(result)

if __name__ == "__main__":
    main()
