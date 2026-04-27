import pandas as pd
from pathlib import Path
import json

# Read file
file_path = Path(r"INEI-Education\data\raw\raw_education_2022.csv")
df = pd.read_csv(file_path, 
                encoding="latin-1",
                low_memory=False)

#Change column names
rename_df = df.rename(columns={"P300A":"idioma_materno", 
                            "P301A":"nivel_educacion",
                            "DOMINIO":"region",
                            "P208A":"edad"})

#Get new dataframe only with required columns
new_df = rename_df.loc[:, ['region', 
                         'edad', 
                         'idioma_materno', 
                         'nivel_educacion']]

#Add an ID column for the PK
new_df.insert(0, "id", range(1, len(new_df) + 1))

new_df = new_df.drop_duplicates()
new_df = new_df.dropna()

#Load JSON file
with open("INEI-Education\config\mapping.json", 
          "r", encoding="utf-8") as json_file:
    mappings = json.load(json_file)

for column, mapping in mappings.items():
    #Convert colum to string
    new_df[column] = new_df[column].astype(str)

    #Replace values
    new_df[column] = new_df[column].map(mapping)

new_df.to_csv(r"INEI-Education\data\processed\processed_data.csv")

print("Processed csv file created.")