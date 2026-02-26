from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def main():
    print("Hello from langchain-course-p!")


if __name__ == "__main__":
    main()
