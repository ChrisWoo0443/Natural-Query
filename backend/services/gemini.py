from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
geminiAPIKEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=geminiAPIKEY)



response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Explain how AI works in a few words"
)
'''
Simple example of using the Gemini API to generate content
'''
print(response.text)



def generate_query_code(query: str, filename: str):
    '''
    Generate SQL code to query a dataset using Gemini API
    '''
    response = client.models.generate_code(
        model="gemini-2.0-flash",
        contents=f"Generate SQL code to query the {filename} dataset with the following query: {query}"
    )
    return response.text