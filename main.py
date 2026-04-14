from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain_tavily import TavilySearch
load_dotenv()

# tavily_client = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """Tool that searches the web for information about the given query.
    
#     Args:
#         query: The query to search for.
#     Returns:
#         The search result.
#     """
#     print(f"Searching the web for information about {query}")
#     return tavily_client.search(query=query)

llm = ChatOllama(model="llama3.2", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


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
