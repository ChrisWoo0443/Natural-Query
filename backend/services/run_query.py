import pandas as pd
import os



def load_dataframe(file_path):
    """Loads the dataset from CSV or Excel into a Pandas dataframe."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format.")

    return df


