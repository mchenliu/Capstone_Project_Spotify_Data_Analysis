import json
import pandas as pd

# list of JSON filr paths
file_paths = [
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020-2021_5.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020_3.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2020_4.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2021-2022_6.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2022-2023_7.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2023_8.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2023-2024_9.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2018-2019_0.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2019-2020_2.json',
    r'C:\Users\Administrator\Desktop\Streaming_History_Audio_2019_1.json'
]


try:
    # Load the JSON data from file using UTF-8 encoding
    dataframes = [pd.read_json(fp, encoding='utf-8') for fp in file_paths]


    # Convert JSON data to a DataFrame
    df = pd.concat(dataframes, ignore_index=True)
    if 'master_metadata_track_name' in df.columns:
        df = df.rename(columns={'master_metadata_track_name': 'new_column_name'})
        print(df.columns)  # Check if the column name was updated
    else:
        print("Column 'master_metadata_track_name' not found.")


except PermissionError as e:
    print(f"Permission Error: {e}")
except FileNotFoundError as e:
    print(f"File Not Found: {e}")
except UnicodeDecodeError as e:
    print(f"Encoding Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
   