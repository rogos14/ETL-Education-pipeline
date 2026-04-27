from sqlalchemy import create_engine
from pathlib import Path
import pandas as pd

file_path = Path(r"INEI-Education\data\processed\processed_data.csv")
education_df = pd.read_csv(file_path,
                           encoding="latin-1",
                           low_memory=False,
                           index_col=0)

#Create the connection to database
engine = create_engine("postgresql://postgres:drakariuros14@localhost:5432/Education_2022")
print("Loading data...")
education_df.to_sql('education', engine,
                    if_exists="append",
                    index=False)
print("Done loading.")

