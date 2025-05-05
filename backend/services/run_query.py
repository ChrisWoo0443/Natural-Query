import pandas as pd
import os

def load_dataframe(file_path):
    """
    Loads the dataset from CSV or Excel into a Pandas dataframe.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format.")

    return df



def sanitize_code(code):
    """
    Basic check to prevent dangerous code execution.
    This is a naive implementation and should be improved for production use.
    """
    blocked_keywords = [
        'import', 'os', 'sys', 'subprocess', 'eval', 'exec',
        'open', 'write', 'remove', 'delete', '__', 'shutil'
    ]

    for word in blocked_keywords:
        if word in code:
            raise ValueError(f"Unsafe code detected: '{word}' found.")



def execute_query_code(code, filename):
    """
    Runs the AI-generated code on the df.
    """
    file_path = os.path.join("./temp", filename)

    df = load_dataframe(file_path)

    sanitize_code(code)

    local_vars = {'df': df}

    try:
        result = eval(code, {"__builtins__": {}}, local_vars)
    except Exception as e:
        result = f"Error executing code: {str(e)}"

    return result


'''Test Ussage'''
# from gemini import generate_query_code, extract_schema, format_prompt

# code = generate_query_code(format_prompt("Give me the first 5 spam messages", extract_schema("./temp/sms.csv")), "sms.csv")
# result = execute_query_code(code, "sms.csv")
# print(code)
# print("Result:", result)