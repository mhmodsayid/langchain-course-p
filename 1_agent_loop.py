import random
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain_tavily import TavilySearch
from langsmith import traceable
load_dotenv()

MAX_ITERATIONS = 10
MODEL_NAME = "gemma4:e2b"

@tool
def get_product_price(product_name: str) -> float:
    """Get the price of a product"""
    print(f"Getting price for {product_name}")
    prices = {"apple": 1.0, "banana": 2.0, "cherry": 3.0}
    return prices.get(product_name, 0.0)

@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Apply a discount to a product based on the discount tier
    available discount tiers: gold, silver, bronze
    """
    print(f"Applying discount {discount_tier} to {price}")
    discount_percentages = {"bronze": 0.8, "silver": 0.7, "gold": 0.6}
    return round(discount_percentages.get(discount_tier, 0.0) * price, 2)
    
@traceable(name="run_agent")
def run_agent(query: str) -> str:
    pass


if __name__ == "__main__":
    print("Starting agent loop")
    run_agent("What is the price of an apple with a gold discount?")
