import pandas as pd

# Load multiple JSON files into a single DataFrame
file_paths = [
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020-2021_5.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020_3.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020_4.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2021-2022_6.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2022-2023_7.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2023_8.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2023-2024_9.json',
]

dataframes = [pd.read_json(fp) for fp in file_paths]
df = pd.concat(dataframes, ignore_index=True)

# Inspect the first rows
print(df.head())
