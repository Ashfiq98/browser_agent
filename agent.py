# import asyncio
# # from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
# from browser_use import Agent
# # from pydantic import SecretStr
# import time
# from dotenv import load_dotenv

# load_dotenv()

# # llm = ChatOpenAI(model="gpt-4o")
# # api_key = os.getenv("GEMINI_API_KEY")

# # Initialize the model
# # llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))
# llm = ChatOpenAI(
#     model="gpt-4o-mini-2024-07-18",
#     temperature=0.0,
# )


# async def main():
#     # agent = Agent(
#     #     task="Find flights on kayak.com from Zurich to Beijing",
#     #     llm=llm,
#     # )

#     sensitive_data = {
#         'xyz_name': 'ashfiqulalam86@gmail.com',
#         'xyz_password': 'topu596@Microsoft'
#     }
#     overall_start_time = time.time()

#     agent = Agent(
#         task="""1. Open the TravelAI website.
#                 2. Click all "TravelAI" logos on the website and confirm they redirect to the homepage.
#                     - If it fails twice, skip this test.
#                 3. Find the "TravelAI" logo in the navigation bar.
#                     - Hover over the logo and check if it contains an anchor (`<a>`) tag.
#                     - If a URL is present, verify it matches the homepage URL.
#             """,
#         llm=llm,
#         sensitive_data=sensitive_data,
#     )

#     result = await agent.run()
#      # Start time for agent execution
#     step_start_time = time.time()
#     result = await agent.run()
#     step_end_time = time.time()

#     # End time for the entire process
#     overall_end_time = time.time()

#     print(result)
#     print(f"\nTime Taken for Agent Execution: {step_end_time - step_start_time:.2f} seconds")
#     print(f"Total Execution Time: {overall_end_time - overall_start_time:.2f} seconds")



# asyncio.run(main())

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent
import time
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini-2024-07-18",
    temperature=0.0,
)

async def main():
    sensitive_data = {
        'xyz_name': 'ashfiqulalam86@gmail.com',
        'xyz_password': 'topu596@Microsoft'
    }

    test_cases = [
        {
            "name": "TravelAI Logo Click Test",
            "task": """Please try a maximum of 3 times for each step. If any case fails thrice, skip the test and do not repeat it.)
               Open the TravelAI website. Click on each 'TravelAI' logo on the website and ensure that they correctly redirect to the TravelAI homepage."""
        },
        # {
        #     "name": "TravelAI Logo Hover Test",
        #     "task": """(Please try a maximum of 3 times for each step. If any case/Evaluation fails thrice, skip that and do not repeat the test case.)
        #        - Open the TravelAI website (https://www.travelai.com/).
        #        - HOVER TravelAi logo(DO NOT CLICK). Check if the anchor `<a>` tag contains the correct TravelAI homepage URL after hovering.
        #        - If the tooltip is not appearing, check the bottom-left corner of the page for the correct URL.
        #        - Verify that the URL matches the TravelAI homepage URL.
        #            """
        # },
        # {
        #     "name": "TravelAI Logo UI Test on Devices",
        #     "task": """(Please try a maximum of 3 times for each step. If any case fails thrice, skip the test and do not repeat it.)
        #        Open the TravelAI website. Check if the 'TravelAI' logo is displayed correctly on different devices (iPhone, iPad, Desktop).
        #        The logo should be fully visible, without distortion or missing elements, across all devices."""
        # }
    ]

    overall_start_time = time.time()  # Start time for the total process

    for test in test_cases:
        print(f"\nExecuting: {test['name']}")
        agent = Agent(task=test["task"], llm=llm, sensitive_data=sensitive_data)

        step_start_time = time.time()  # Start time for individual test case
        result = await agent.run()
        step_end_time = time.time()  # End time for individual test case

        # print(result)
        print(f"Time Taken for '{test['name']}': {step_end_time - step_start_time:.2f} seconds")

    overall_end_time = time.time()  # End time for the total process
    print(f"\nTotal Execution Time: {overall_end_time - overall_start_time:.2f} seconds")

asyncio.run(main())
