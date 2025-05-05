from google import genai

from KEYS import geminiAPIKEY

client = genai.Client(api_key=geminiAPIKEY)


'''
Simple example of using the Gemini API to generate content
'''
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Explain how AI works in a few words"
)
print(response.text)