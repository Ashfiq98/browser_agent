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
    # agent = Agent(
    #     task="Find flights on kayak.com from Zurich to Beijing",
    #     llm=llm,
    # )
    # 1. Navigate to rentbyowner.com.
    #         2. Locate the "Property Tile" section, which includes:
    #            - An input field with the placeholder "Where do you want to go?"
    #            - A date picker beside the input field that opens a modal calendar.
    #            - Ensure that dates before today are disabled, and previous months cannot be selected.
    #         3. Test the search functionality:
    #            - Enter a valid location and click "Show Best Price". Verify that hotels or resorts appear based on the entered place and selected dates.
    #            - Enter random meaningless text and ensure that some properties still appear instead of an empty result.
    #         4. Verify the navigation:
    #            - After clicking "Show Best Price", the user should be directed to the "Refine Page" with the appropriate listings.
    #         5. Generate a report in Google Docs, checking if all the functionality works correctly. Write the findings in list format.
    #         6. Save or download the report locally.
    agent = Agent(
        task="""
              1. Navigate to rentbyowner.com.
              2. Locate the "Property Tile" section, which includes:
                 - An input field with the placeholder "Where do you want to go?"
                 - A date picker beside the input field that opens a modal calendar.
                 - Ensure that dates before today are disabled, and previous months cannot be selected.
              3. Test the search functionality:
                 - Enter a valid location and click "Show Best Price". Verify that hotels or resorts appear based on the entered place and selected dates.
                 - Enter random meaningless text and ensure that some properties still appear instead of an empty result.
              4. Verify the navigation:
                 - After clicking "Show Best Price", the user should be directed to the "Refine Page" with the appropriate listings.
              5. Generate a report in Google Docs based on above scenario, checking if all the functionality works correctly. Write the findings in list format.
              6. Save or download the report locally.
        """,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())