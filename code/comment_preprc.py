# -*- coding: utf-8 -*-

# 这是最常用的统计包
import pandas as pd

# os包里面主要用的是path 函数， 用来切换文件路径
import os

# 这是最常用的数学包，比如求个最大值啊，填充nan啊 都用这个包
import numpy as np

# 这是画图包，未来画data分布时会用到
import matplotlib.pyplot as plt

file_name = '天猫正品评论(1).csv'

# df意思是 data frame， 一个data frame就像excel里的一个sheet， 包含col， row的名字
# row的名字又叫 index
df = pd.read_csv(file_name)

# 这是你需要的data的column，直接用column名字来叫他们即可，也可以用列号
feature_columns = ['First Review','Follow Review','Seller Exp','ID']

# loc 和 iloc是 取df某一些行列最常用的两个函数
df = df.loc[:,feature_columns]
df.iloc[1,:].ID
# 我们还可能用到：
df.columns
df.rename(columns={'First Review': 'Reviews','Follow Review': 'SecondReview'})
TFflag = pd.DataFrame([1]*len(df),columns = ['TF'])    # 建立一列 用来存这个商品是真还是假，这个test.csv里存的都是天猫的 所以目前都是1 真货
new_df = pd.concat([df,TFflag],axis=1)
new_df.head()


new_df.to_csv('preproc.csv',encoding='utf_8_sig')