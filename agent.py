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
    # 2. Locate the "Property Tile" section, which includes:
    #    - An input field with the placeholder "Where do you want to go?"
    #    - A date picker beside the input field that opens a modal calendar.
    #    - Ensure that dates before today are disabled, and previous months cannot be selected.
    # 3. Test the search functionality:
    #    - Enter a valid location and click "Show Best Price". 
    #      Verify that hotels or resorts appear based on the entered place and selected dates.
    #    - Enter random meaningless text and ensure that some properties still appear instead of an empty result.
    # 4. Verify the navigation:
    #    - After clicking "Show Best Price", the user should be directed to the "Refine Page" with the appropriate listings.
    # 5. Generate a report in Google Docs, checking if all the functionality works correctly. Write the findings in list format.
    # 6. Save or download the report locally.
    #    - Write report in Google Docs (named as "QA Report") after finishing every task. 
    #      If everything is okay then write 'okay' beside each task otherwise 'not okay'.
    #    - Use xyz_name as username or email and xyz_password as password for logging into Google Docs whenever needed.
    #    - Finally, save or download the document locally.
    # 7. Navigate to rentbyowner.com.
    # 8. Test the search functionality:
    #    - Enter a valid location (e.g., Cox's Bazar, Bangladesh), select valid dates, and click "Show Best Price".
    #      Verify that hotels or resorts appear based on the entered place and selected dates.
    #    - Enter random meaningless text and ensure that some properties still appear instead of an empty result.
    # 9. Verify each navigation step.


    sensitive_data = {
        'xyz_name': 'ashfiqpractice@gmail.com',
        'xyz_password': 'topu596@Practice'
    }

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
                 - open google sheets and use username as xyz_name and password as xyz_password
              5. Generate a report in Google Sheets based on above scenario, checking if all the functionality works correctly.if you need to make column or row you can
                 named as  “Test Case”, “URL”, “Status” .
              6. Save or download the sheet locally.
        """,
        llm=llm,
        sensitive_data=sensitive_data,
    )

    result = await agent.run()
    print(result)


asyncio.run(main())




# #    agent = Agent(
        # task="""
        #       - write report in google docs (named as QA report) after finish every task that if everything is okay then write 'okay' beside each task otherwise 'not okay'.
        #         Use xyz_name as username or email and xyz_password as password for login google to access google docs whenever needed.
        #       1. Navigate to rentbyowner.com.
        #       2. Test the search functionality:
        #          - Enter a valid location (e.g. Cox's Bazar, Bangladesh) , valid date for how many days you will stay and then click "Show Best Price". 
        #            Verify that hotels or resorts appear based on the entered place and selected dates. 
        #          - Enter random meaningless text and ensure that some properties still appear instead of an empty result.
        #       3. Verify the navigation:
        #       4. Locate the "Property Tile" section, which includes:
        #          - An input field with the placeholder "Where do you want to go?"
        #          - A date picker beside the input field that opens a modal calendar.
        #          - Ensure that dates before today are disabled, and previous months cannot be selected.
        #          - After clicking "Show Best Price", the user should be directed to the "Refine Page" with the appropriate listings.
        #       5. Generate a report in Google Docs based on above scenario, checking if all the functionality works correctly. Write the findings in list format.
        #       6. Save or download the report locally.
        # """,
# #         llm=llm,
# #         sensitive_data=sensitive_data
# #     )

# from typing import ClassVar, Any, List
# from langchain_google_genai import ChatGoogleGenerativeAI
# from browser_use import Agent
# from pydantic import SecretStr
# import os
# import asyncio
# from dotenv import load_dotenv

# load_dotenv()


# class TokenStats:
#     def __init__(self):
#         self.prompt_tokens = 0
#         self.completion_tokens = 0

#     def log_prompt(self, text: str):
#         self.prompt_tokens += len(text) // 4  # rough estimate

#     def log_completion(self, text: str):
#         self.completion_tokens += len(text) // 4  # rough estimate

#     def get_stats(self):
#         return {
#             'prompt_tokens': self.prompt_tokens,
#             'completion_tokens': self.completion_tokens,
#             'total_tokens': self.prompt_tokens + self.completion_tokens,
#             'estimated_cost': ((self.prompt_tokens + self.completion_tokens) / 1000) * 0.0005  # Gemini Pro pricing
#         }


# class TokenTrackingLLM(ChatGoogleGenerativeAI):
#     stats: ClassVar[TokenStats] = TokenStats()  # Class-level stats tracker

#     async def agenerate(self, prompts: List[str], **kwargs: Any) -> Any:
#         """Override generate to add token tracking."""
#         # Log prompt tokens
#         for prompt in prompts:
#             self.stats.log_prompt(prompt)
#             print(f"\nStarting LLM with prompt length: {len(prompt)} characters")

#         # Get response
#         response = await super().agenerate(prompts, **kwargs)
#         print("Model Response:", response)  # Log full response

#         # Log completion tokens
#         if hasattr(response, 'generations') and response.generations:
#             completion_text = response.generations[0][0].text
#             self.stats.log_completion(completion_text)
#             print(f"Completion length: {len(completion_text)} characters")
#             print(f"Estimated completion tokens: {self.stats.completion_tokens}")

#         return response


# async def main():
#     api_key = os.getenv("GEMINI_API_KEY")

#     # Initialize the model with token tracking
#     llm = TokenTrackingLLM(
#         model='gemini-2.0-flash-exp',
#         api_key=SecretStr(api_key)
#     )

#     sensitive_data = {'xyz_name': 'ashfiqpractice@gmail.com', 'xyz_password': 'topu596@Practice'}

#     agent = Agent(
#         task="""
#         Navigate to rentbyowner.com and see search button is working or not
#         """,
#         llm=llm,
#         sensitive_data=sensitive_data,
#     )

#     try:
#         result = await agent.run()
#         print("\nTask Result:", result)

#         # Print token usage and cost summary
#         usage = llm.stats.get_stats()
#         print("\nToken Usage Summary:")
#         print(f"Prompt tokens: {usage['prompt_tokens']}")
#         print(f"Completion tokens: {usage['completion_tokens']}")
#         print(f"Total tokens: {usage['total_tokens']}")
#         print(f"Estimated cost: ${usage['estimated_cost']:.4f}")
        
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     asyncio.run(main())
