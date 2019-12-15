import pandas as pd
import numpy as np

# train_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/train_format1.csv', sep=',')
train_df = pd.read_csv('/Users/hanmufu/Workspaces/Repeat_Buyers_Prediction/data_format1/train_format1.csv', sep=',')
print("train_format1 loaded successful")
print(train_df.head())

# user_log_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/user_log_format1.csv')
user_log_df = pd.read_csv('/Users/hanmufu/Workspaces/Repeat_Buyers_Prediction/data_format1/user_log_format1.csv')
print("user_log_format1 loaded successful")
print(user_log_df.head())

# user_info_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/user_info_format1.csv')
user_info_df = pd.read_csv('/Users/hanmufu/Workspaces/Repeat_Buyers_Prediction/data_format1/user_info_format1.csv')
print("user_info_format1 loaded successful")
print(user_info_df.head())

train_with_user_info = pd.merge(train_df, user_info_df)
print(train_with_user_info.head())