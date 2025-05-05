from google import genai
from dotenv import load_dotenv
import pandas as pd
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


def extract_schema(file_path):
    """Reads the uploaded dataset (CSV or Excel) and returns the schema as column names + data types."""
    # Detect file extension
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

    schema = {col: str(df[col].dtype) for col in df.columns}
    return schema




def generate_query_code(query: str, filename: str):
    '''
    Generate SQL code to query a dataset using Gemini API
    '''
    response = client.models.generate_code(
        model="gemini-2.0-flash",
        contents=f"Generate SQL code to query the {filename} dataset with the following query: {query}"
    )
    return response.text