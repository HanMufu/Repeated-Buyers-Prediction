#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 00:15
# @Author  : qin yuxin
# @File    : qyxtest.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import os
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

monthly_log_saveDir = "monthly_log"
if not os.path.exists(monthly_log_saveDir):
    os.mkdir(monthly_log_saveDir)


# only use once
def save_monthly_log(log_df):
    for month in range(1, 13):
        month_df = log_df.loc[log_df['time_stamp'] // 100 == month]
        month_df.to_csv(os.path.join(monthly_log_saveDir, '{0}_user_log.csv'.format(month)), index=False)


# train_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/train_format1.csv', sep=',')
# print(train_df)

# user_log_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/user_log_format1.csv')
# user_log_df = user_log_df.rename(columns={'seller_id': 'merchant_id'})
# user_log_df[:101].to_csv('user_log_df_100_rows.csv')
# print(user_log_df[:101])


user_log_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/user_log_format1.csv')
save_monthly_log(user_log_df)  # only run once
for month in range(5, 12):
    click_dict = {}
    u_m_list = []
    click_times_list = []
    file_name = os.path.join(monthly_log_saveDir, '{0}_user_log.csv'.format(month))
    cur_month_log = pd.read_csv(file_name).loc[:, ['user_id', 'merchant_id', 'action_type']]
    cur_month_click = cur_month_log.loc[cur_month_log['action_type'] == 0]
    cur_month_click['user_merchant'] = cur_month_log['user_id'].map(str) + '-' + cur_month_log['merchant_id'].map(str)
    for u_m in cur_month_click['user_merchant'].unique():
        u_m_list.append(u_m)
        click_times_list.append(len(cur_month_click.loc[cur_month_click['user_merchant'] == u_m]))
    click_dict["u_m"] = u_m_list
    click_dict["click_times"] = click_times_list
    click_df = pd.DataFrame(click_dict)
    click_df.to_csv(os.path.join(monthly_log_saveDir, '{0}_user_click.csv').format(month))


#################### test code #########################################
# click_dict = {}
# user_list = []
# merchant_list = []
# click_times_list = []
# user_log_df = pd.read_csv('user_log_df_100_rows.csv').loc[:, ['user_id', 'merchant_id', 'action_type']]
# user_click = user_log_df.loc[user_log_df['action_type'] == 0]
# print(user_click)
# print("-----------------------------------------------")
# user_click['user_merchant'] = user_click['user_id'].map(str) + '-' + user_click['merchant_id'].map(str)
# for u_m in user_click['user_merchant'].unique():
#     user_list.append(u_m.split('-')[0])
#     merchant_list.append(u_m.split('-')[1])
#     click_times_list.append(len(user_click.loc[user_click['user_merchant'] == u_m]))
# click_dict["user_id"] = user_list
# click_dict["merchant_id"] = merchant_list
# click_dict["click_times"] = click_times_list
# click_df = pd.DataFrame(click_dict)
# click_df.to_csv('test100_user_click.csv')
#######################################################################

# user_info_df = pd.read_csv('/Users/Rosemary/Downloads/data_format1/user_info_format1.csv')
# print("This is user_info")
# print(user_info_df)

# train_with_user_info = pd.merge(train_df, user_info_df)
# print(train_with_user_info)

#  0:click; 1:add-to-cart; 2:purchase; 3:add-to-favourite


