# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:44:38 2018

@author: Duo Cao
"""

import jieba
import jieba.posseg as pseg
from optparse import OptionParser
import pandas as pd
## Import is now csv file


file_name = 'comment_t.csv'
df = pd.read_csv(file_name)
feature_columns = ['商品ID' , '初次评价' , '追评内容' , '卖家解释' ]
df = df.loc[:,feature_columns]
df = df.rename(columns={'初次评价': 'FR', '追评内容': 'Follow_Review','卖家解释':'Seller_Exp',
                        '商品ID':'ID'})

## Currently we only work on the First Review
df = df.loc[:,['ID','FR']]

nip_library = ['x','uj','ul','r']
dict_id = 0
dict_list = []
word_library = []

Brand_id_list = list(set(df.ID))  # set will drop all duplicates automatically
Brand_id_list = [int(x) for x in Brand_id_list if str(x) != 'nan']
result_df = pd.DataFrame()
for product_id in Brand_id_list:
    temp_library = {}
    working_df = df.loc[df.ID == product_id]
    for temp_str in list(working_df.FR):
        temp_str = str(temp_str)
        if temp_str == None or temp_str =='nan':
            continue
        seg_list = pseg.cut(temp_str)
        
        for word, flag1 in seg_list:
            if flag1 not in nip_library:
                if word in temp_library:
                    temp_library[word] += 1
                else:
                    temp_library[word] = 1
    temp_df = pd.DataFrame.from_dict(temp_library,orient='index')
    temp_df = temp_df.rename(columns={0: product_id})
    result_df = pd.merge(result_df,temp_df,how = 'outer',left_index = True, right_index = True)

result_df = result_df.transpose()
result_df = result_df.fillna(0) 
result_df.to_csv('build_frequency.csv',encoding='utf_8_sig')
