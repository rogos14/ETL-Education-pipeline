import pandas as pd
from pathlib import Path

# Validate if file exists and not empty
# Read file 
file_path = Path(r"INEI-Education\data\raw\sample_education.csv")
if (file_path.is_file()):
    if (file_path.stat().st_size > 0):
        raw_data_df = pd.read_csv(file_path, 
                                encoding="latin-1",
                                low_memory=False)
        raw_data_df.to_csv(r"INEI-Education\data\raw\raw_education_2022.csv")
    else:
        print("File is empty")
else:
    print("File not found")