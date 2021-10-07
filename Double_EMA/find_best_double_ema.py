import os
import pandas as pd

list_path = os.path.abspath('.\\Double_EMA\\results')

result_list = os.listdir(list_path)

for result in result_list:
    result_path = os.path.join(list_path, result)
    
    result_df = pd.read_csv(result_path)

    result_df = result_df.sort_values(
        by='annual_return', ascending=False).reset_index()
    result_df = result_df.drop(columns=['index', 'Unnamed: 0', 'sqn', 'trades'])
    result_df.head().to_csv(
        f".\\Double_EMA\\best_double_ema\\best-{result[7:-4]}.csv")
