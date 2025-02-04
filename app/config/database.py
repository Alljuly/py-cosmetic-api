import pandas as pd
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(base_dir, "db.csv")

def load_csv() -> pd.DataFrame:
    try:
        return pd.read_csv(CSV_FILE_PATH)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame(columns=["id", "name", "brand", "rate", "description", "value"])
    
def save_csv(df: pd.DataFrame):
    df.to_csv(CSV_FILE_PATH, index=False)
