import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()


# llm = ChatOpenAI(model="gpt-4o")
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))


async def main():
    agent = Agent(
        task="go to rentbyowner and give me some data for all the hotels in cox's bazar",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())