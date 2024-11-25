import os
import openai
# import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

print(load_dotenv(find_dotenv()))

print(os.environ(["SAM"]))


# delimter = "####"
# system_message = f"""Act as BMW car sales and service assitant.\
#     You will be provided will be provided with customer queries.\
#     And the queries will be delimted by {delimter} characters.
    
#     Classify the queries in Sales and Service catagory.\
#     Provide the output as json format with keys : sales and service
#     """

# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "system", "content": system_message},
#                 {"role": "user", "content": f"{delimter}I have a dent as well as i need buy a new car {delimter}"}]
#     response = openai.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output 
#     )
#     return response.choices[0].message.content


# print(get_completion("Take the letters in lollipop and reverse them"))