import pandas as pd
import numpy as np
import seaborn as sns

#Read data
# Specify the path to your file
file_path = r"C:\Users\Maurits\PycharmProjects\ThesisFC\Data\First_data_18-01-2024.csv"
df = pd.read_csv(file_path, low_memory=False)

print(df.head(50))
