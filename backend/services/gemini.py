from google import genai
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
geminiAPIKEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=geminiAPIKEY)



# response = client.models.generate_content(
#     model="gemini-2.0-flash", 
#     contents="Explain how AI works in a few words"
# )
# '''
# Simple example of using the Gemini API to generate content
# '''
# print(response.text)


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


def format_prompt(query, schema, mode="pandas"):
    schema_str = "\n".join([f"{col}: {dtype}" for col, dtype in schema.items()])
    if mode == "pandas":
        prompt = f"""
                    You are a Python Pandas expert. Given the following dataset schema:

                    {schema_str}

                    Generate Pandas code to answer the following natural language query:
                    "{query}"

                    Only return the code. Assume the dataframe has already been loaded as 'df'.

                    Do not include any extra text only the query. 

                    Do not include the word python, any variables, or print statements.
                    """
    elif mode == "sql":
        prompt = f"""
                    You are a SQL expert. Given the following dataset schema:

                    {schema_str}

                    Generate a SQL query to answer the following natural language query:
                    "{query}"

                    Only return the SQL query. Assume the table is called 'data'.
                    """
    else:
        raise ValueError("Mode must be either 'pandas' or 'sql'.")

    return prompt



def generate_query_code(query: str, filename: str):
    '''
    Generate SQL code to query a dataset using Gemini API
    '''
    file_path = os.path.join("./temp", filename)

    schema = extract_schema(file_path)
    prompt = format_prompt(query, schema)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text
